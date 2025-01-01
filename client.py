# client.py
import sys
import asyncio
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Signal, QObject, QTimer

from ui_form import Ui_client
from api import ChatClientAPI
from qasync import QEventLoop, asyncSlot


class Communicate(QObject):
    message_received = Signal(dict)
    error_received = Signal(str)
    disconnected = Signal()


class Client(QWidget):
    def __init__(self, comm, parent=None):
        super().__init__(parent)
        self.ui = Ui_client()
        self.ui.setupUi(self)

        # Communication signals
        self.comm = comm
        self.comm.message_received.connect(self.display_message)
        self.comm.error_received.connect(self.display_error)
        self.comm.disconnected.connect(self.handle_disconnection)

        # ChatClientAPI instance
        self.api = ChatClientAPI()

        # Connect UI elements to functions
        self.ui.pushButton_connect.clicked.connect(self.connect_to_server)
        self.ui.pushButton_login.clicked.connect(self.login)
        self.ui.pushButton_send.clicked.connect(self.send_message)

        # Schedule the receiver task after the event loop starts
        QTimer.singleShot(0, self.start_receiving)

    def start_receiving(self):
        print("运行接收线程")
        asyncio.create_task(self.api.receive_messages(self.comm))

    @asyncSlot()
    async def connect_to_server(self):
        server_ip = self.ui.lineEdit.text()
        if not server_ip:
            QMessageBox.warning(self, "错误", "请输入服务器地址")
            return

        inputip = server_ip.split(":")
        if len(inputip) != 2:
            QMessageBox.warning(self, "错误", "服务器地址格式应为 IP:端口")
            return

        self.api.server_host = inputip[0]
        try:
            self.api.server_port = int(inputip[1])
        except ValueError:
            QMessageBox.warning(self, "错误", "端口必须是整数")
            return

        try:
            await self.api.connect()
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
        except Exception as e:
            QMessageBox.critical(self, "连接失败", f"无法连接到服务器: {e}")

    @asyncSlot()
    async def login(self):
        username = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()
        if not username or not password:
            QMessageBox.warning(self, "错误", "用户名和密码不能为空")
            return

        try:
            response = await self.api.login(username, password)
            print(response)
            if response.get("status") == "success":
                QMessageBox.information(self, "登录成功", "欢迎进入聊天系统！")
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_chat)
            else:
                QMessageBox.warning(self, "登录失败", response.get("message"))
        except Exception as e:
            QMessageBox.critical(self, "登录失败", f"发生错误: {e}")

    @asyncSlot()
    async def send_message(self):
        target_user = self.ui.lineEdit_targetuser.text()
        message = self.ui.plainTextEdit_editmessage.toPlainText()
        if not target_user or not message:
            QMessageBox.warning(self, "错误", "接收用户和消息内容不能为空")
            return

        try:
            await self.api.send_message(target_user, message)
            self.ui.plainTextEdit_editmessage.clear()
        except Exception as e:
            QMessageBox.critical(self, "发送失败", f"发送消息时发生错误: {e}")

    def display_message(self, msg):
        sender = msg.get("sender")
        message = msg.get("message")
        timestamp = msg.get("timestamp")
        self.ui.plainTextEdit.appendPlainText(f"[{timestamp}] {sender}: {message}")

    def display_error(self, error_msg):
        QMessageBox.critical(self, "接收错误", f"接收消息时发生错误: {error_msg}")

    def handle_disconnection(self):
        QMessageBox.warning(self, "断开连接", "与服务器的连接已断开")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_connect)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set up the qasync event loop
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    comm = Communicate()

    widget = Client(comm)
    widget.show()

    with loop:
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass
