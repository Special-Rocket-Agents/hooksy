# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from discord_webhook import DiscordWebhook


class Ui_Hooksy(object):
    def setupUi(self, Hooksy):
        Hooksy.setObjectName("Hooksy")
        Hooksy.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        Hooksy.setFont(font)
        Hooksy.setStyleSheet("background-color: #36393f;")
        self.centralwidget = QtWidgets.QWidget(Hooksy)
        self.centralwidget.setObjectName("centralwidget")
        self.webhookText = QtWidgets.QLabel(self.centralwidget)
        self.webhookText.setGeometry(QtCore.QRect(210, 220, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.webhookText.setFont(font)
        self.webhookText.setStyleSheet("color: white;")
        self.webhookText.setObjectName("webhookText")
        self.webhookURL = QtWidgets.QTextEdit(self.centralwidget)
        self.webhookURL.setGeometry(QtCore.QRect(210, 250, 531, 25))
        self.webhookURL.setFontPointSize(12)
        self.webhookURL.setStyleSheet("border: 1px solid rgb(88, 93, 103);\n"
"border-radius: 4px;\n"
"font-family: \'Segoe UI\';\n"
"color: white;")
        self.webhookURL.setObjectName("webhookURL")
        self.webhookURL.textChanged.connect(self.changeURLSize)
        self.contentText = QtWidgets.QLabel(self.centralwidget)
        self.contentText.setGeometry(QtCore.QRect(210, 310, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.contentText.setFont(font)
        self.contentText.setStyleSheet("color: white;")
        self.contentText.setObjectName("contentText")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(650, 480, 91, 31))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        self.sendButton.setFont(font)
        self.sendButton.clicked.connect(self.sendMessage)
        self.sendButton.setStyleSheet("background-color: #404eed;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-family: segoe ui;\n"
"font-size: 15px;\n"
"QPushButton::hover {\n"
"    background-color: #333ebc;\n"
"}")
        self.sendButton.setObjectName("sendButton")
        self.msgContent = QtWidgets.QTextEdit(self.centralwidget)
        self.msgContent.setGeometry(QtCore.QRect(210, 350, 531, 111))
        self.msgContent.setStyleSheet("border: 1px solid rgb(88, 93, 103);\n"
"border-radius: 4px;\n"
"font-family: \'Segoe UI\';\n"
"color: white;")
        self.msgContent.setObjectName("msgContent")
        self.msgContent.textChanged.connect(self.changeContentSize)
        Hooksy.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Hooksy)
        self.statusbar.setObjectName("statusbar")
        Hooksy.setStatusBar(self.statusbar)

        self.retranslateUi(Hooksy)
        QtCore.QMetaObject.connectSlotsByName(Hooksy)

    def retranslateUi(self, Hooksy):
        _translate = QtCore.QCoreApplication.translate
        Hooksy.setWindowTitle(_translate("Hooksy", "Hooksy"))
        self.webhookText.setText(_translate("Hooksy", "Webhook URL"))
        self.contentText.setText(_translate("Hooksy", "Content"))
        self.sendButton.setText(_translate("Hooksy", "Send"))

    def sendMessage(self):
        webhookMessage = DiscordWebhook()
        webhookMessage.content = self.msgContent.toPlainText()
        webhookMessage.url = self.webhookURL.toPlainText()
        webhookMessage.execute()

    def changeContentSize(self):
        self.msgContent.setFontPointSize(12)
    
    def changeURLSize(self):
        self.webhookURL.setFontPointSize(12)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hooksy = QtWidgets.QMainWindow()
    ui = Ui_Hooksy()
    ui.setupUi(Hooksy)
    Hooksy.show()
    sys.exit(app.exec_())