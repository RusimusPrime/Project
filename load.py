from PyQt6.QtWidgets import QDialog
from PyQt6 import QtCore, QtWidgets


class LoadWidget(QDialog):
    def __init__(self, file, name):
        super().__init__()
        self.setObjectName("Load Dialog")
        self.resize(380, 140)
        self.slot1 = QtWidgets.QPushButton(self)
        self.slot1.setGeometry(QtCore.QRect(20, 20, 100, 100))
        self.slot1.setStyleSheet("QPushButton { background-color: rgba(255, 255, 255, 1); }\n"
                                 "QPushButton { color: rgba(0, 0, 0, 1); }")
        self.slot1.setObjectName("pushButton")
        self.slot2 = QtWidgets.QPushButton(self)
        self.slot2.setGeometry(QtCore.QRect(140, 20, 100, 100))
        self.slot2.setStyleSheet("QPushButton { background-color: rgba(0, 57, 166, 1); }")
        self.slot2.setObjectName("pushButton_2")
        self.slot3 = QtWidgets.QPushButton(self)
        self.slot3.setGeometry(QtCore.QRect(260, 20, 100, 100))
        self.slot3.setStyleSheet("QPushButton { background-color: rgba(213, 43, 30, 1); }")
        self.slot3.setObjectName("pushButton_3")
        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(QtCore.QRect(0, 0, 380, 140))
        self.background.setStyleSheet("QLabel { background-color: rgba(0, 33, 118, 1); }")
        self.background.setText("")
        self.background.setObjectName("label")
        self.background.raise_()
        self.slot1.raise_()
        self.slot2.raise_()
        self.slot3.raise_()

        QtCore.QMetaObject.connectSlotsByName(self)
        self.file = file
        self.name = name
        self.slot1.clicked.connect(self.load_game_slot1)
        self.slot1.setText("Load №1")
        self.slot2.setText("Load №2")
        self.slot3.setText("Load №3")
        self.slot2.clicked.connect(self.load_game_slot2)
        self.slot3.clicked.connect(self.load_game_slot3)

    def load_game_slot1(self):
        with open(f"data/states/{self.name.split('/')[-1] + "1.state"}",
                  "rb") as f:
            self.file.load_state(f)
            self.close()

    def load_game_slot2(self):
        with open(f"data/states/{self.name.split('/')[-1] + "2.state"}",
                  "rb") as f:
            self.file.load_state(f)
            self.close()

    def load_game_slot3(self):
        with open(f"data/states/{self.name.split('/')[-1] + "3.state"}",
                  "rb") as f:
            self.file.load_state(f)
            self.close()
