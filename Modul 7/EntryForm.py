from PyQt5.QtWidgets import (QDialog, QGridLayout,QHBoxLayout, QLabel, QLineEdit, QPushButton)
# import sys
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *

class EntryForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(320, 280)
        self.setWindowTitle('Tambah/Ubah Kontak')
        self.mode = -1
        self.okButton = QPushButton('OK')
        self.cancelButton = QPushButton('Batal')
        hbox = QHBoxLayout()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        self.label1 = QLabel("Nama Lengkap:")
        self.nameLineEdit = QLineEdit()
        self.label2 = QLabel("Nomor HP:")
        self.phoneLineEdit = QLineEdit()

        if self.mode == 0:
            self.nameLineEdit.clear()
            self.phoneLineEdit.clear()

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.nameLineEdit, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.phoneLineEdit, 1, 1)
        layout.addLayout(hbox, 2, 1)
        self.setLayout(layout)
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)