import asyncio
import json
import struct
from typing import Optional

# Helper functions for sending and receiving packets
async def send_packet(writer: asyncio.StreamWriter, msg: dict):
    msg_bytes = json.dumps(msg).encode('utf-8')
    msg_length = len(msg_bytes)
    writer.write(struct.pack('>I', msg_length))
    writer.write(msg_bytes)
    # print(msg)
    await writer.drain()

async def read_packet(reader: asyncio.StreamReader) -> Optional[dict]:
    try:
        len_bytes = await reader.readexactly(4)
        msg_length = struct.unpack('>I', len_bytes)[0]
        msg_bytes = await reader.readexactly(msg_length)
        return json.loads(msg_bytes.decode('utf-8'))
    except asyncio.IncompleteReadError:
        print("Connection closed by the server.")
        return None
    except Exception as e:
        print(f"Error reading packet: {e}")
        return None
