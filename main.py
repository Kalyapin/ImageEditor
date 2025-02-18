from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QTextEdit, \
    QLineEdit, QLabel, QMessageBox, QFileDialog
import os
import json
from PIL import Image, ImageQt, ImageFilter, ImageEnhance


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.pixmap = None
        self.image_path = None

    def show_image(self):
        pictures_label.hide()
        pictures_label.setPixmap(self.pixmap)
        pictures_label.show()

    def reload_pixmap(self):
        image_qt = ImageQt.ImageQt(self.image)
        self.pixmap = QPixmap.fromImage(image_qt)
        w, h = pictures_label.width(), pictures_label.height()
        self.pixmap = self.pixmap.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio)
        self.show_image()

    def load_image(self, filename):
        self.filename = filename
        self.image_path = os.path.join(workdir, filename)
        self.image = Image.open(self.image_path)
        # self.pixmap = QPixmap(self.image_path)
        self.reload_pixmap()

    def greyscale(self):
        self.image = self.image.convert('L')
        self.reload_pixmap()

    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.reload_pixmap()

    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.reload_pixmap()

    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.reload_pixmap()

    def contr(self):
        self.image = ImageEnhance.Contrast(self.image)
        self.image = self.image.enhance(1.5)
        self.reload_pixmap()

    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.reload_pixmap()

    def max_blur(self):
        self.image = self.image.filter(ImageFilter.MaxFilter)
        self.reload_pixmap()

    def sharpness(self):
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.reload_pixmap()

    def smooth(self):
        self.image = self.image.filter(ImageFilter.SMOOTH)
        self.reload_pixmap()

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
contr_button = QPushButton('Осветвление')
blur_button = QPushButton('Блюр')
max_blur_button = QPushButton('Макс. размытие')
sharpness_button = QPushButton('Резкость')
light_dark_button = QPushButton('Ч/Б')
effect_button = QPushButton('Анти-резкость')
main_layout = QHBoxLayout()
sub_layout1 = QVBoxLayout()
sub_layout2 = QVBoxLayout()
sub_sub_layout1 = QHBoxLayout()
sub_sub_layout2 = QHBoxLayout()

main_window.setLayout(main_layout)
main_layout.addLayout(sub_layout1)
main_layout.addLayout(sub_layout2)
sub_layout1.addWidget(open_folder_button)
sub_layout1.addWidget(pictures_list)
sub_layout2.addWidget(pictures_label)
sub_layout2.addLayout(sub_sub_layout1)
sub_layout2.addLayout(sub_sub_layout2)
sub_sub_layout1.addWidget(rotate_left_button)
sub_sub_layout1.addWidget(rotate_right_button)
sub_sub_layout1.addWidget(mirror_button)
sub_sub_layout1.addWidget(contr_button)
sub_sub_layout1.addWidget(light_dark_button)
sub_sub_layout2.addWidget(blur_button)
sub_sub_layout2.addWidget(max_blur_button)
sub_sub_layout2.addWidget(sharpness_button)
sub_sub_layout2.addWidget(effect_button)


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



pictures_list.itemClicked.connect(load_pic)
open_folder_button.clicked.connect(open_folder)
light_dark_button.clicked.connect(dirigeur.greyscale)
rotate_left_button.clicked.connect(dirigeur.rotate_left)
rotate_right_button.clicked.connect(dirigeur.rotate_right)
mirror_button.clicked.connect(dirigeur.mirror)
contr_button.clicked.connect(dirigeur.contr)
blur_button.clicked.connect(dirigeur.blur)
max_blur_button.clicked.connect(dirigeur.max_blur)
sharpness_button.clicked.connect(dirigeur.sharpness)
effect_button.clicked.connect(dirigeur.smooth)



main_window.show()
app.exec()
