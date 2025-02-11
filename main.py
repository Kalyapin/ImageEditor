from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QTextEdit, \
    QLineEdit, QLabel, QMessageBox, QFileDialog
import os
import json
from PIL import Image


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.pixmap = None
        self.image_path = None

    def load_image(self, filename):
        self.filename = filename
        self.image_path = os.path.join(workdir, filename)
        self.image = Image.open(self.image_path)
        self.pixmap = QPixmap(self.image_path)

    def show_image(self):
        pictures_label.hide()
        pictures_label.setPixmap(self.pixmap)
        pictures_label.show()

dirigeur = ImageProcessor()
workdir = ''
app = QApplication([])
main_window = QWidget()
main_window.setFixedSize(800, 600)
main_window.setWindowTitle('Image Editor')
pictures_label = QLabel('Тут будет картинка')
pictures_list = QListWidget()
open_folder_button = QPushButton('Папка')
rotate_left_button = QPushButton('Лево')
rotate_right_button = QPushButton('Право')
mirror_button = QPushButton('Зеркало')
contr_button = QPushButton('Резкость')
light_dark_button = QPushButton('Ч/Б')
main_layout = QHBoxLayout()
sub_layout1 = QVBoxLayout()
sub_layout2 = QVBoxLayout()
sub_sub_layout1 = QHBoxLayout()

main_window.setLayout(main_layout)
main_layout.addLayout(sub_layout1)
main_layout.addLayout(sub_layout2)
sub_layout1.addWidget(open_folder_button)
sub_layout1.addWidget(pictures_list)
sub_layout2.addWidget(pictures_label)
sub_layout2.addLayout(sub_sub_layout1)
sub_sub_layout1.addWidget(rotate_left_button)
sub_sub_layout1.addWidget(rotate_right_button)
sub_sub_layout1.addWidget(mirror_button)
sub_sub_layout1.addWidget(contr_button)
sub_sub_layout1.addWidget(light_dark_button)


def select_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def filter(files, extensions):
    result = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result


def open_folder():
    select_workdir()
    files = os.listdir(workdir)
    extensions = ['.jpg', '.png', '.jpeg', '.gif']
    files = filter(files, extensions)
    pictures_list.clear()
    pictures_list.addItems(files)





def load_pic():
    name = pictures_list.selectedItems()[0].text()
    dirigeur.load_image(name)
    dirigeur.show_image()

pictures_list.itemClicked.connect(load_pic)
open_folder_button.clicked.connect(open_folder)

main_window.show()
app.exec()
