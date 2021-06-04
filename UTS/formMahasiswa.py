# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_Mahasiswa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(687, 695)
        Form.setStyleSheet("background-color: rgb(231, 230, 255);")

        # Label Judul
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 30, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # List Widget
        # self.isi = QtWidgets.QPlainTextEdit(Form)
        self.isi = QtWidgets.QListWidget(Form)
        self.isi.setGeometry(QtCore.QRect(90, 90, 501, 351))
        self.isi.setStyleSheet("\n" "background-color: rgb(255, 255, 255);")
        self.isi.setObjectName("isi")

        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 590, 399, 30))
        self.layoutWidget.setObjectName("layoutWidget")

        # Layout untuk Tombol-Tombol
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Tombol Tambah
        self.bt_tambah = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bt_tambah.setFont(font)
        self.bt_tambah.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.bt_tambah.setObjectName("bt_tambah")
        self.horizontalLayout.addWidget(self.bt_tambah)

        # Tombol Edit
        self.bt_edit = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bt_edit.setFont(font)
        self.bt_edit.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.bt_edit.setObjectName("bt_edit")
        self.horizontalLayout.addWidget(self.bt_edit)

        # Tombol Clear
        self.bt_clear = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bt_clear.setFont(font)
        self.bt_clear.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.bt_clear.setObjectName("bt_clear")
        self.horizontalLayout.addWidget(self.bt_clear)

        # Tombol Keluar
        self.bt_keluar = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bt_keluar.setFont(font)
        self.bt_keluar.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.bt_keluar.setObjectName("bt_keluar")
        self.horizontalLayout.addWidget(self.bt_keluar)

        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(90, 470, 501, 111))
        self.layoutWidget_2.setObjectName("layoutWidget_2")

        # Layout untuk lineEdit
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget_2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        # Label untuk nim
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)

        # Label untuk Nama
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)

        # Label untuk Jurusan
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)

        # Label untuk No.Tlp
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)

        # lineEdit untuk Nim
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)

        # lineEdit untuk Nama
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)

        # lineEdit untuk Jurusan
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)

        # lineEdit untuk No.tlp
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)

        # Interaksi tombol Keluar
        self.bt_keluar.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "DATA MAHASISWA"))
        self.bt_tambah.setText(_translate("Form", "Tambah"))
        self.bt_edit.setText(_translate("Form", "Edit"))
        self.bt_clear.setText(_translate("Form", "Clear"))
        self.bt_keluar.setText(_translate("Form", "Exit"))
        self.label_2.setText(_translate("Form", "NIM"))
        self.label_3.setText(_translate("Form", "Nama"))
        self.label_4.setText(_translate("Form", "Jurusan"))
        self.label_5.setText(_translate("Form", "No. Tlp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

