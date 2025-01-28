from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QTextEdit, \
    QLineEdit, QLabel, QMessageBox
import os
import json

app = QApplication([])
main_window = QWidget()
main_window.setFixedSize(800, 600)
main_window.setWindowTitle('Image Editor')
pictures_label =  QLabel('Тут будет картинка')
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





main_window.show()
app.exec()
