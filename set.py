import csv

from PyQt6.QtWidgets import QDialog
from PyQt6 import QtCore, QtWidgets


class SettingWidget(QDialog):
    def __init__(self, color):
        super().__init__()
        self.setObjectName("Setting dialog")
        self.resize(360, 212)
        self.FirstColor = QtWidgets.QLineEdit(parent=self)
        self.FirstColor.setGeometry(QtCore.QRect(200, 20, 131, 50))
        self.FirstColor.setStyleSheet("font: 20pt Comic Sans MS")
        self.FirstColor.setObjectName("lineEdit")
        self.ChooseColor = QtWidgets.QPushButton(parent=self)
        self.ChooseColor.setGeometry(QtCore.QRect(120, 170, 141, 28))
        self.ChooseColor.setStyleSheet("font:  Comic Sans MS")
        self.ChooseColor.setObjectName("pushButton")
        self.MainColor = QtWidgets.QLabel(parent=self)
        self.MainColor.setGeometry(QtCore.QRect(20, 20, 161, 50))
        self.MainColor.setStyleSheet("color: rgba(255, 255, 255, 1); font: 20pt Comic Sans MS")
        self.MainColor.setObjectName("label")
        self.SecondColor = QtWidgets.QLabel(parent=self)
        self.SecondColor.setGeometry(QtCore.QRect(20, 90, 121, 50))
        self.SecondColor.setStyleSheet("color: rgba(255, 255, 255, 1); font: 20pt Comic Sans MS")
        self.SecondColor.setObjectName("label_2")
        self.SecondColor = QtWidgets.QLineEdit(parent=self)
        self.SecondColor.setGeometry(QtCore.QRect(200, 90, 131, 50))
        self.SecondColor.setStyleSheet("font: 20pt Comic Sans MS")
        self.SecondColor.setObjectName("lineEdit_2")
        self.background = QtWidgets.QLabel(parent=self)
        self.background.setGeometry(QtCore.QRect(0, 0, 360, 212))
        self.background.setStyleSheet(f"background-color: rgba({color}, 1)")
        self.background.setText("")
        self.background.setObjectName("label_5")
        self.background.raise_()
        self.FirstColor.raise_()
        self.ChooseColor.raise_()
        self.MainColor.raise_()
        self.SecondColor.raise_()
        self.SecondColor.raise_()
        self.ChooseColor.setText("Принять RGB цвета")
        self.MainColor.setText("Main color")
        self.SecondColor.setText("color")
        self.FirstColor.setText('0, 33, 118')
        self.SecondColor.setText('252, 166, 3')
        self.ChooseColor.clicked.connect(self.action)

    def action(self):
        with open("data/csv files/settings.csv", "w", newline="", encoding="utf8") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([self.FirstColor.text(), self.SecondColor.text()])
        self.close()
