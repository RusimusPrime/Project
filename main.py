import os
import csv
import sys
import sqlite3

import cv2
import keyboard

from PyQt6.QtCore import Qt
from pyboy import PyBoy
from PIL import Image
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow, QButtonGroup, QSlider, QPushButton, QDialog, \
    QInputDialog

from set import SettingWidget
from save import SaveWidget
from load import LoadWidget


def game(name):
    boy = PyBoy(name)
    while boy.tick():
        if keyboard.is_pressed("z"):
            save_ex = SaveWidget(boy, name)
            save_ex.show()
        if keyboard.is_pressed("x"):
            load_ex = LoadWidget(boy, name)
            load_ex.show()
    boy.stop(False)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.action_color()
        self.setObjectName("PyBoyQT")
        self.resize(640, 500)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.AllGames = QtWidgets.QLabel(self.centralwidget)
        self.AllGames.setGeometry(QtCore.QRect(70, 240, 150, 31))
        self.AllGames.setStyleSheet("color: rgb(255, 255, 255);")
        self.AllGames.setObjectName("label_4")
        self.powerOff = QtWidgets.QPushButton(self.centralwidget)
        self.powerOff.setGeometry(QtCore.QRect(10, 430, 40, 40))
        self.powerOff.setObjectName("pushButton_6")
        self.MainColor = QtWidgets.QLabel(self.centralwidget)
        self.MainColor.setGeometry(QtCore.QRect(60, 0, 580, 480))
        self.MainColor.setStyleSheet(f"background-color: rgba({self.action_color()[0]}, 1)")
        self.MainColor.setText("")
        self.MainColor.setObjectName("label_2")
        self.SecondColor = QtWidgets.QLabel(self.centralwidget)
        self.SecondColor.setGeometry(QtCore.QRect(0, 0, 60, 480))
        self.SecondColor.setStyleSheet(f"background-color: rgba({self.action_color()[1]}, 1)")
        self.SecondColor.setText("")
        self.SecondColor.setObjectName("label")
        self.ContinueGame = QtWidgets.QLabel(self.centralwidget)
        self.ContinueGame.setGeometry(QtCore.QRect(70, 20, 300, 35))
        self.ContinueGame.setStyleSheet("QLabel {color: rgba(255, 255, 255, 1); }")
        self.ContinueGame.setObjectName("label_3")
        self.Secret = QtWidgets.QPushButton(self.centralwidget)
        self.Secret.setGeometry(QtCore.QRect(10, 60, 40, 40))
        self.Secret.setObjectName("pushButton_7")
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.settings.setObjectName("pushButton_5")
        self.settings.clicked.connect(self.action_setting)

        self.DeleteGame = QtWidgets.QPushButton(self)
        self.DeleteGame.setGeometry(QtCore.QRect(10, 110, 40, 40))
        self.DeleteGame.raise_()
        self.DeleteGame.show()
        self.DeleteGame.setIcon(QIcon("data/icons/delate.png"))  # Укажите путь к вашему изображению
        self.DeleteGame.setIconSize(self.DeleteGame.size())
        self.DeleteGame.clicked.connect(self.delate)

        self.SecondColor.raise_()
        self.MainColor.raise_()
        self.AllGames.raise_()
        self.powerOff.raise_()
        self.ContinueGame.raise_()
        self.Secret.raise_()
        self.settings.raise_()
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

        spisok = self.data()
        spisok1 = list(filter(lambda x: x != '', [spisok[4 * i:4 * i + 4] for i in range(len(spisok) // 4)] + [
            spisok[-(len(spisok) - len(spisok) // 4 * 4):] if len(spisok) % 4 != 0 else '']))
        self.group_button = QButtonGroup(self.centralwidget)
        self.list_buttons = []
        self.settings.setIcon(QIcon("data/icons/settings.png"))  # Укажите путь к вашему изображению
        self.settings.setIconSize(self.settings.size())
        self.powerOff.setIcon(QIcon("data/icons/turn off.png"))  # Укажите путь к вашему изображению
        self.powerOff.setIconSize(self.powerOff.size())
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
        self.NewGame = QtWidgets.QPushButton(self)
        self.NewGame.setGeometry(QtCore.QRect(x + 40, y + 40, 50, 50))
        self.NewGame.setObjectName("pushButton_9")
        self.NewGame.setIcon(QIcon("data/icons/plus.png"))
        self.NewGame.setIconSize(self.NewGame.size())
        self.NewGame.clicked.connect(self.new_game)
        self.NewGame.raise_()
        self.group_button.addButton(self.NewGame)
        self.NewGame.hide()
        self.list_buttons.append(self.NewGame)

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
        self.ContinueGame.setText("Продолжить игру")
        self.ContinueGame.setStyleSheet("font: 20pt Comic Sans MS")
        self.AllGames.setText("Все игры")
        self.AllGames.setStyleSheet("font: 20pt Comic Sans MS")
        self.Secret.setIcon(QIcon("data/icons/freddy.webp"))
        self.Secret.setIconSize(self.Secret.size())

        self.powerOff.clicked.connect(self.action_close)
        self.Secret.clicked.connect(self.play_video_fullscreen)

    def action_setting(self):
        set_ex = SettingWidget(self.action_color()[0])
        set_ex.show()
        set_ex.exec()
        self.close()
        self.__init__()
        self.show()

    def delate(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Введите номер игры, которую хотите удалить:')
        print(text, ok)
        if ok:
            con = sqlite3.connect("data/data.sqlite")
            cur = con.cursor()
            cur.execute(
                """DELETE from roms WHERE id = ?""", (text,))
            cur.execute(
                """DELETE from covers WHERE id = ?""", (text,))
            con.commit()
            con.close()
            self.close()
            self.__init__()
            self.show()

    def action_color(self):
        with open("data/csv files/settings.csv", encoding="utf8") as csvfile:
            reader = list(csv.reader(csvfile, delimiter=';', quotechar='"'))
        return reader[0]

    def new_game(self):
        self.choose_rom()
        self.choose_cover(self.start_slider())
        self.close()
        self.__init__()
        self.show()

    def play_video_fullscreen(self):
        cap = cv2.VideoCapture("data/video/videoplayback.mp4")
        if not cap.isOpened():
            print("Ошибка: Не удалось открыть видеофайл.")
            return
        # Создание окна для отображения
        cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Video", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break
        cap.release()
        cv2.destroyAllWindows()

    def start_slider(self):
        con = sqlite3.connect("data/data.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM roms""").fetchall()
        return len(result)

    def data(self):
        con = sqlite3.connect("data/data.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM roms""").fetchall()
        return result

    def action_close(self):
        self.close()

    def choose_rom(self):
        file_name = QFileDialog.getOpenFileName(self, "Выбрать файл", "")[0]
        con = sqlite3.connect("data/data.sqlite")
        con.execute("""INSERT INTO roms (id, name, path) VALUES(?, ?, ?)""", (
            self.start_slider() + 1, file_name.split("/")[-1],
            f"data/games/{file_name.split("/")[-1]}"))
        os.replace(file_name, f"data/games/{file_name.split("/")[-1]}")
        con.commit()

    def choose_cover(self, n):
        file_name = QFileDialog.getOpenFileName(self, "Выбрать картинку", "")[0]
        img = Image.open(file_name)
        img.save(f"data/covers/{file_name.split("/")[-1]}")
        con = sqlite3.connect("data/data.sqlite")
        con.execute("""INSERT INTO covers (id, path) VALUES(?, ?)""",
                    (n, f"data/covers/{file_name.split("/")[-1]}"))
        con.commit()

    def action_rom(self, path, n):
        return lambda: (game(path), self.spisok_states.insert(0, n), self.action_save_states(self.spisok_states))

    def action_cover(self, n):
        con = sqlite3.connect("data/data.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT path FROM covers WHERE id = ?""", (n,)).fetchall()
        return result[0][0]

    def action_change(self, value):
        for i, button in enumerate(self.list_buttons):
            button.setVisible((value - 1) * 4 < i + 1 <= value * 4)

    def action_load_states(self):
        with open("data/csv files/states.csv", encoding="utf8") as csvfile:
            reader = list(csv.reader(csvfile, delimiter=";", quotechar='"'))
        return reader[0] if reader else reader

    def action_save_states(self, reader):
        with open("data/csv files/states.csv", "w", newline="", encoding="utf8") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(reader[:4])
        self.close()
        self.__init__()
        self.show()

    def choose_path_rom(self, n):
        con = sqlite3.connect("data/data.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT path FROM roms WHERE id = ?""", (n,)).fetchall()
        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
