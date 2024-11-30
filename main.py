import sys
import cv2
import csv
import keyboard
import os
import sqlite3
from PyQt6.QtCore import Qt
from pyboy import PyBoy
from PIL import Image
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow, QButtonGroup, QSlider, QPushButton, QDialog


def game(name):
    boy = PyBoy(name)
    while boy.tick():
        if keyboard.is_pressed('z'):
            save_ex = SaveWidget(boy, name)
            save_ex.show()
        if keyboard.is_pressed('x'):
            load_ex = LoadWidget(boy, name)
            load_ex.show()
    boy.stop(False)


class SettingWidget(QDialog):
    def __init__(self, color):
        super().__init__()
        self.setObjectName("Setting dialog")
        self.resize(360, 212)
        self.lineEdit = QtWidgets.QLineEdit(parent=self)
        self.lineEdit.setGeometry(QtCore.QRect(200, 20, 131, 50))
        self.lineEdit.setStyleSheet("font: 20pt Comic Sans MS")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self)
        self.pushButton.setGeometry(QtCore.QRect(120, 170, 141, 28))
        self.pushButton.setStyleSheet("font:  Comic Sans MS")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=self)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 50))
        self.label.setStyleSheet("color: rgba(255, 255, 255, 1); font: 20pt Comic Sans MS")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 121, 50))
        self.label_2.setStyleSheet("color: rgba(255, 255, 255, 1); font: 20pt Comic Sans MS")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 90, 131, 50))
        self.lineEdit_2.setStyleSheet("font: 20pt Comic Sans MS")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(parent=self)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 360, 212))
        self.label_5.setStyleSheet(f"background-color: rgba({color}, 1)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.setText("Принять RGB цвета")
        self.label.setText("Main color")
        self.label_2.setText("color")
        self.lineEdit.setText('0, 33, 118')
        self.lineEdit_2.setText('252, 166, 3')
        self.pushButton.clicked.connect(self.action)

    def action(self):
        with open('data/csv files/settings.csv', 'w', newline='', encoding="utf8") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([self.lineEdit.text(), self.lineEdit_2.text()])
        self.close()


class SaveWidget(QDialog):
    def __init__(self, file, name):
        super().__init__()
        self.setObjectName("Save dialog")
        self.resize(380, 140)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 100, 100))
        self.pushButton.setStyleSheet("QPushButton { background-color: rgba(255, 255, 255, 1); }\n"
                                      "QPushButton { color: rgba(0, 0, 0, 1); }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 20, 100, 100))
        self.pushButton_2.setStyleSheet("QPushButton { background-color: rgba(0, 57, 166, 1); }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 20, 100, 100))
        self.pushButton_3.setStyleSheet("QPushButton { background-color: rgba(213, 43, 30, 1); }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 380, 140))
        self.label.setStyleSheet("QLabel { background-color: rgba(0, 33, 118, 1); }")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()

        QtCore.QMetaObject.connectSlotsByName(self)

        self.file = file
        self.name = name
        self.pushButton.setText('Save №1')
        self.pushButton_2.setText('Save №2')
        self.pushButton_3.setText('Save №3')
        self.pushButton.clicked.connect(self.action1)
        self.pushButton_2.clicked.connect(self.action2)
        self.pushButton_3.clicked.connect(self.action3)

    def action1(self):
        with open(f"data/states/{self.name.split('/')[-1] + '1.state'}",
                  "wb") as f:
            self.file.save_state(f)
            self.close()

    def action2(self):
        with open(f"data/states/{self.name.split('/')[-1] + '2.state'}",
                  "wb") as f:
            self.file.save_state(f)
            self.close()

    def action3(self):
        with open(f"data/states/{self.name.split('/')[-1] + '3.state'}",
                  "wb") as f:
            self.file.save_state(f)
            self.close()


class LoadWidget(QDialog):
    def __init__(self, file, name):
        super().__init__()
        self.setObjectName("Load Dialog")
        self.resize(380, 140)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 100, 100))
        self.pushButton.setStyleSheet("QPushButton { background-color: rgba(255, 255, 255, 1); }\n"
                                      "QPushButton { color: rgba(0, 0, 0, 1); }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 20, 100, 100))
        self.pushButton_2.setStyleSheet("QPushButton { background-color: rgba(0, 57, 166, 1); }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 20, 100, 100))
        self.pushButton_3.setStyleSheet("QPushButton { background-color: rgba(213, 43, 30, 1); }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 380, 140))
        self.label.setStyleSheet("QLabel { background-color: rgba(0, 33, 118, 1); }")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()

        QtCore.QMetaObject.connectSlotsByName(self)
        self.file = file
        self.name = name
        self.pushButton.clicked.connect(self.action1)
        self.pushButton.setText('Load №1')
        self.pushButton_2.setText('Load №2')
        self.pushButton_3.setText('Load №3')
        self.pushButton_2.clicked.connect(self.action2)
        self.pushButton_3.clicked.connect(self.action3)

    def action1(self):
        with open(f"data/states/{self.name.split('/')[-1] + '1.state'}",
                  "rb") as f:
            self.file.load_state(f)
            self.close()

    def action2(self):
        with open(f"data/states/{self.name.split('/')[-1] + '2.state'}",
                  "rb") as f:
            self.file.load_state(f)
            self.close()

    def action3(self):
        with open(f"data/states/{self.name.split('/')[-1] + '3.state'}",
                  "rb") as f:
            self.file.load_state(f)
            self.close()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.action_color()
        self.setObjectName("PyBoyQT")
        self.resize(640, 500)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 240, 150, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 430, 40, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 0, 580, 480))
        self.label_2.setStyleSheet(f"background-color: rgba({self.action_color()[0]}, 1)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 60, 480))
        self.label.setStyleSheet(f"background-color: rgba({self.action_color()[1]}, 1)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 300, 35))
        self.label_3.setStyleSheet("QLabel {color: rgba(255, 255, 255, 1); }")
        self.label_3.setObjectName("label_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 60, 40, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.action_setting)

        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.pushButton_6.raise_()
        self.label_3.raise_()
        self.pushButton_7.raise_()
        self.pushButton_5.raise_()
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(self)
        self.spisok_states = self.action_load_states()
        self.group = QButtonGroup(self.centralwidget)
        for i in range(len(self.spisok_states)):
            self.pushButton = QPushButton(self)
            self.pushButton.setGeometry(QtCore.QRect(80 + 140 * i, 80, 120, 120))
            self.pushButton.setObjectName("pushButton")
            self.pushButton.clicked.connect(
                self.action_rom(self.choose_path_rom(self.spisok_states[i])[0][0], self.spisok_states[i]))
            self.pushButton.setIcon(
                QIcon(self.action_cover(self.spisok_states[i])))  # Укажите путь к вашему изображению
            self.pushButton.setIconSize(self.pushButton.size())
            self.pushButton.raise_()
            self.group.addButton(self.pushButton)

        spisok = self.start_list()
        spisok1 = list(filter(lambda x: x != '', [spisok[4 * i:4 * i + 4] for i in range(len(spisok) // 4)] + [
            spisok[-(len(spisok) - len(spisok) // 4 * 4):] if len(spisok) % 4 != 0 else '']))
        self.group_button = QButtonGroup(self.centralwidget)
        self.list_buttons = []
        self.pushButton_5.setIcon(QIcon('data/icons/settings.png'))  # Укажите путь к вашему изображению
        self.pushButton_5.setIconSize(self.pushButton_5.size())
        self.pushButton_6.setIcon(QIcon('data/icons/turn off.png'))  # Укажите путь к вашему изображению
        self.pushButton_6.setIconSize(self.pushButton_6.size())
        x, y = 80, 310
        for j in range(len(spisok1)):
            for i in range(len(spisok1[j])):
                self.pushButton = QPushButton(self)
                self.pushButton.setGeometry(QtCore.QRect(80 + 140 * i, 310, 120, 120))
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.action_rom(spisok1[j][i][2], spisok1[j][i][0]))
                self.pushButton.setIcon(QIcon(self.action_cover(spisok1[j][i][0])))  # Укажите путь к вашему изображению
                self.pushButton.setIconSize(self.pushButton.size())
                self.pushButton.raise_()
                self.pushButton.hide()
                self.group_button.addButton(self.pushButton)
                self.list_buttons.append(self.pushButton)
                x, y = 80 + 140 * ((1 + i) if i < 3 else 0), 310

        for i, button in enumerate(self.list_buttons):
            button.setVisible(i + 1 <= 4)
        self.pushButton_9 = QtWidgets.QPushButton(self)
        self.pushButton_9.setGeometry(QtCore.QRect(x + 40, y + 40, 50, 50))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setIcon(QIcon("data/icons/plus.png"))
        self.pushButton_9.setIconSize(self.pushButton_9.size())
        self.pushButton_9.clicked.connect(self.action_plus)
        self.pushButton_9.raise_()
        self.group_button.addButton(self.pushButton_9)
        self.pushButton_9.hide()
        self.list_buttons.append(self.pushButton_9)

        self.slider = QSlider(self)
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setGeometry(270, 450, 160, 22)
        self.start_slider()
        self.slider.setRange(1, (self.start_slider() + 1) // 4 if
        (self.start_slider() + 1) % 4 == 0 else (self.start_slider() + 1) // 4 + 1)
        self.slider.setSingleStep(1)
        self.slider.setPageStep(1)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider.valueChanged.connect(self.action_change)
        self.label_3.setText('Продолжить игру')
        self.label_3.setStyleSheet("font: 20pt Comic Sans MS")
        self.label_4.setText('Все игры')
        self.label_4.setStyleSheet("font: 20pt Comic Sans MS")
        self.pushButton_7.setIcon(QIcon("data/icons/freddy.webp"))
        self.pushButton_7.setIconSize(self.pushButton_7.size())

        self.pushButton_6.clicked.connect(self.action_close)
        self.pushButton_7.clicked.connect(self.play_video_fullscreen)

    def action_setting(self):
        set_ex = SettingWidget(self.action_color()[0])
        set_ex.show()
        set_ex.exec()
        self.close()
        self.__init__()
        self.show()

    def action_color(self):
        with open('data/csv files/settings.csv', encoding="utf8") as csvfile:
            reader = list(csv.reader(csvfile, delimiter=';', quotechar='"'))
        return reader[0]

    def action_plus(self):
        self.choose_rom()
        self.choose_cover(self.start_slider())
        self.close()
        self.__init__()
        self.show()

    def play_video_fullscreen(self):
        cap = cv2.VideoCapture('data/video/videoplayback.mp4')
        if not cap.isOpened():
            print("Ошибка: Не удалось открыть видеофайл.")
            return
        # Создание окна для отображения
        cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def start_slider(self):
        con = sqlite3.connect('data/data.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM roms""").fetchall()
        return len(result)

    def start_list(self):
        con = sqlite3.connect('data/data.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM roms""").fetchall()
        return result

    def action_close(self):
        self.close()

    def choose_rom(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать файл', '')[0]
        con = sqlite3.connect('data/data.sqlite')
        con.execute("""INSERT INTO roms (id, name, path) VALUES(?, ?, ?)""", (
            self.start_slider() + 1, file_name.split('/')[-1],
            f"data/games/{file_name.split('/')[-1]}"))
        os.replace(file_name, f"data/games/{file_name.split('/')[-1]}")
        con.commit()

    def choose_cover(self, n):
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        img = Image.open(file_name)
        img.save(f"data/covers/{file_name.split('/')[-1]}")
        con = sqlite3.connect('data/data.sqlite')
        con.execute("""INSERT INTO covers (id, path) VALUES(?, ?)""",
                    (n, f"data/covers/{file_name.split('/')[-1]}"))
        con.commit()

    def action_rom(self, path, n):
        return lambda: (game(path), self.spisok_states.insert(0, n), self.action_save_states(self.spisok_states))

    def action_cover(self, n):
        con = sqlite3.connect('data/data.sqlite')
        cur = con.cursor()
        link = f"SELECT path FROM covers WHERE id == {str(n)}"
        result = cur.execute(link).fetchall()
        return result[0][0]

    def action_change(self, value):
        for i, button in enumerate(self.list_buttons):
            button.setVisible((value - 1) * 4 < i + 1 <= value * 4)

    def action_load_states(self):
        with open('data/csv files/states.csv', encoding="utf8") as csvfile:
            reader = list(csv.reader(csvfile, delimiter=';', quotechar='"'))
        return reader[0] if reader else reader

    def action_save_states(self, reader):
        with open('data/csv files/states.csv', 'w', newline='', encoding="utf8") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(reader[:4])
        self.close()
        self.__init__()
        self.show()

    def choose_path_rom(self, n):
        con = sqlite3.connect('data/data.sqlite')
        cur = con.cursor()
        link = f"SELECT path FROM roms WHERE id == {str(n)}"
        result = cur.execute(link).fetchall()
        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
