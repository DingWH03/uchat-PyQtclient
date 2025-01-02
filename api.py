# api.py
import asyncio
import json
from utils import send_packet, read_packet
from typing import Optional
from protocol import LoginRequest, SendMessageRequest


class ChatClientAPI:
    def __init__(self):
        self.server_host = None
        self.server_port = None
        self.reader = None
        self.writer = None
        self.running = False

    async def send_packet(self, data: dict):
        await send_packet(self.writer, data)

    async def read_packet(self) -> Optional[dict]:
        return await read_packet(self.reader)

    async def connect(self):
        try:
            self.reader, self.writer = await asyncio.open_connection(self.server_host, self.server_port)
            self.running = True
            print("成功连接到服务器")
        except Exception as e:
            print(f"无法连接到服务器: {e}")
            self.running = False
            raise

    async def login(self, username: str, password: str) -> dict:
        if not self.running:
            raise ConnectionError("尚未连接到服务器")

        login_request = LoginRequest(
            action="login",
            username=username,
            password=password
        )
        await self.send_packet(json.loads(login_request.to_json()))
        response = await self.read_packet()
        return response

    async def register(self, username: str, password: str) -> dict:
        if not self.running:
            raise ConnectionError("尚未连接到服务器")

        login_request = LoginRequest(
            action="register",
            username=username,
            password=password
        )
        await self.send_packet(json.loads(login_request.to_json()))
        response = await self.read_packet()
        return response

    async def send_message(self, receiver: str, message: str):
        if not self.running:
            raise ConnectionError("尚未连接到服务器")

        send_msg_request = SendMessageRequest(
            action="send_message",
            receiver=receiver,
            message=message
        )
        await self.send_packet(json.loads(send_msg_request.to_json()))

    async def receive_messages(self, comm):
        if not self.running:
            return

        while self.running:
            try:
                msg = await self.read_packet()
                print(msg)
                if msg is None:
                    print("服务器断开连接")
                    self.running = False
                    comm.disconnected.emit()
                    break
                action = msg.get("action")
                if action == "receive_message":
                    comm.message_received.emit(msg)
                elif action == "error":
                    comm.error_received.emit(msg.get("message"))
                else:
                    print(f"\n未知消息: {msg}")
            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"接收消息时发生错误: {e}")
                comm.error_received.emit(str(e))
                break

    async def close(self):
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
        self.running = False
        print("连接已关闭")
