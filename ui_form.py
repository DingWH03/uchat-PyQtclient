# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_client(object):
    def setupUi(self, client):
        if not client.objectName():
            client.setObjectName(u"client")
        client.resize(1273, 856)
        self.gridLayout = QGridLayout(client)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(client)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_connect = QWidget()
        self.page_connect.setObjectName(u"page_connect")
        self.verticalLayout = QVBoxLayout(self.page_connect)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page_connect)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 388, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.page_connect)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_connect = QPushButton(self.page_connect)
        self.pushButton_connect.setObjectName(u"pushButton_connect")

        self.horizontalLayout.addWidget(self.pushButton_connect)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 388, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_connect)
        self.page_chat = QWidget()
        self.page_chat.setObjectName(u"page_chat")
        self.verticalLayout_7 = QVBoxLayout(self.page_chat)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.plainTextEdit = QPlainTextEdit(self.page_chat)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_6.addWidget(self.plainTextEdit)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.plainTextEdit_editmessage = QPlainTextEdit(self.page_chat)
        self.plainTextEdit_editmessage.setObjectName(u"plainTextEdit_editmessage")

        self.horizontalLayout_6.addWidget(self.plainTextEdit_editmessage)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.page_chat)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit_targetuser = QLineEdit(self.page_chat)
        self.lineEdit_targetuser.setObjectName(u"lineEdit_targetuser")

        self.horizontalLayout_5.addWidget(self.lineEdit_targetuser)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.pushButton_send = QPushButton(self.page_chat)
        self.pushButton_send.setObjectName(u"pushButton_send")

        self.verticalLayout_5.addWidget(self.pushButton_send)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.page_chat)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.horizontalLayout_4 = QHBoxLayout(self.page_login)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(411, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_username = QLabel(self.page_login)
        self.label_username.setObjectName(u"label_username")

        self.verticalLayout_2.addWidget(self.label_username)

        self.label_password = QLabel(self.page_login)
        self.label_password.setObjectName(u"label_password")

        self.verticalLayout_2.addWidget(self.label_password)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit_username = QLineEdit(self.page_login)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.verticalLayout_3.addWidget(self.lineEdit_username)

        self.lineEdit_password = QLineEdit(self.page_login)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.verticalLayout_3.addWidget(self.lineEdit_password)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButton_login = QPushButton(self.page_login)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.horizontalLayout_3.addWidget(self.pushButton_login)

        self.pushButton_signup = QPushButton(self.page_login)
        self.pushButton_signup.setObjectName(u"pushButton_signup")

        self.horizontalLayout_3.addWidget(self.pushButton_signup)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(411, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.stackedWidget.addWidget(self.page_login)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(client)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(client)
    # setupUi

    def retranslateUi(self, client):
        client.setWindowTitle(QCoreApplication.translate("client", u"client", None))
        self.label.setText(QCoreApplication.translate("client", u"\u8fde\u63a5\u5230\u670d\u52a1\u5668", None))
        self.lineEdit.setText(QCoreApplication.translate("client", u"127.0.0.1:8080", None))
        self.pushButton_connect.setText(QCoreApplication.translate("client", u"\u8fde\u63a5", None))
        self.label_2.setText(QCoreApplication.translate("client", u"\u53d1\u9001\u7ed9", None))
        self.pushButton_send.setText(QCoreApplication.translate("client", u"\u53d1\u9001", None))
        self.label_username.setText(QCoreApplication.translate("client", u"\u7528\u6237\u540d", None))
        self.label_password.setText(QCoreApplication.translate("client", u"\u5bc6\u7801", None))
        self.pushButton_login.setText(QCoreApplication.translate("client", u"\u767b\u9646", None))
        self.pushButton_signup.setText(QCoreApplication.translate("client", u"\u6ce8\u518c", None))
    # retranslateUi

