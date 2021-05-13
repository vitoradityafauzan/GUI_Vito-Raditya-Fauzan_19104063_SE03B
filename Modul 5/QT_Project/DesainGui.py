# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(627, 631)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(144, 110, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.namaEdit = QtWidgets.QLineEdit(Form)
        self.namaEdit.setGeometry(QtCore.QRect(110, 220, 421, 22))
        self.namaEdit.setObjectName("namaEdit")
        self.hallo = QtWidgets.QPushButton(Form)
        self.hallo.setGeometry(QtCore.QRect(160, 290, 93, 28))
        self.hallo.setObjectName("hallo")
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(380, 290, 93, 28))
        self.clear.setObjectName("clear")
        self.keluar = QtWidgets.QPushButton(Form)
        self.keluar.setGeometry(QtCore.QRect(270, 360, 93, 28))
        self.keluar.setObjectName("keluar")

        self.retranslateUi(Form)
        self.clear.clicked.connect(self.namaEdit.clear)
        self.keluar.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Masukan Nama Anda"))
        self.hallo.setText(_translate("Form", "Hallo"))
        self.clear.setText(_translate("Form", "Clear"))
        self.keluar.setText(_translate("Form", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

