from PySide6.QtWidgets import QVBoxLayout, QWidget, QScrollArea, QPushButton
from PySide6.QtCore import QRect, QCoreApplication

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(400, 450)

        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setGeometry(QRect(10, 10, 381, 231))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)

        self.pushButton = QPushButton(Widget)
        self.pushButton.setGeometry(QRect(10, 250, 381, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QPushButton(Widget)
        self.pushButton1.setGeometry(QRect(10, 300, 381, 41))
        self.pushButton1.setObjectName("pushButton1")

        self.pushButton2 = QPushButton(Widget)
        self.pushButton2.setGeometry(QRect(10, 350, 381, 41))
        self.pushButton2.setObjectName("pushButton2")

        self.pushButton3 = QPushButton(Widget)
        self.pushButton3.setGeometry(QRect(10, 400, 381, 41))
        self.pushButton3.setObjectName("pushButton3")

        self.retranslateUi(Widget)
        QCoreApplication.translate

    def retranslateUi(self, Widget):
        _translate = QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.pushButton.setText(_translate("Widget", "Open local folder to scan"))
        self.pushButton1.setText(_translate("Widget", "Open remote folder to scan"))
        self.pushButton2.setText(_translate("Widget", "Api scan"))
        self.pushButton3.setText(_translate("Widget", "Scan port"))
