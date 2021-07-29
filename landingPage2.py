# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Landing_Page_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget
# from FormTambahV1 import *
import chart_rc
import pymysql
import pymysql.cursors

class Ui_LandingPage2(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 689)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameSideBar = QtWidgets.QFrame(self.centralwidget)
        self.frameSideBar.setGeometry(QtCore.QRect(0, 0, 111, 661))
        self.frameSideBar.setStyleSheet("background-color: rgb(20, 122, 214);\n"
                                        "color: rgb(255, 255, 255);")
        self.frameSideBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSideBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSideBar.setObjectName("frameSideBar")

        self.label = QtWidgets.QLabel(self.frameSideBar)
        self.label.setGeometry(QtCore.QRect(10, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.frameSideBar)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")

        self.framePajangan = QtWidgets.QFrame(self.centralwidget)
        self.framePajangan.setGeometry(QtCore.QRect(170, 20, 341, 291))
        self.framePajangan.setStyleSheet("border: 5px solid;\n"
                                         "border-color: rgb(197, 197, 197);")
        self.framePajangan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePajangan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePajangan.setObjectName("framePajangan")

        self.labelPieChart = QtWidgets.QLabel(self.framePajangan)
        self.labelPieChart.setGeometry(QtCore.QRect(70, 20, 201, 191))
        self.labelPieChart.setStyleSheet("image: url(:/pie chart/Screenshot 2021-07-15 212925.jpg);\n"
                                         "border-color: rgb(255, 255, 255);\n"
                                         "border: 0px")
        self.labelPieChart.setText("")
        self.labelPieChart.setObjectName("labelPieChart")

        self.label_2 = QtWidgets.QLabel(self.framePajangan)
        self.label_2.setGeometry(QtCore.QRect(20, 240, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 0px;")
        self.label_2.setObjectName("label_2")

        self.dateTimeUpdate = QtWidgets.QDateEdit(self.framePajangan)
        self.dateTimeUpdate.setGeometry(QtCore.QRect(140, 240, 196, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateTimeUpdate.setFont(font)
        self.dateTimeUpdate.setStyleSheet("border: 3px solid;\n"
                                          "\n"
                                          "border-color: rgb(0, 0, 0);")
        self.dateTimeUpdate.setObjectName("dateTimeUpdate")

        self.tableWidgetProgress = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetProgress.setGeometry(QtCore.QRect(570, 10, 541, 591))
        self.tableWidgetProgress.setObjectName("tableWidgetProgress")
        self.tableWidgetProgress.setColumnCount(3)
        self.tableWidgetProgress.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidgetProgress.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProgress.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProgress.setHorizontalHeaderItem(2, item)

        self.labelNamaProgress = QtWidgets.QLabel(self.centralwidget)
        self.labelNamaProgress.setGeometry(QtCore.QRect(120, 350, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelNamaProgress.setFont(font)
        self.labelNamaProgress.setObjectName("labelNamaProgress")

        self.lineEditNamaKegiatan = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNamaKegiatan.setGeometry(QtCore.QRect(330, 350, 231, 23))
        self.lineEditNamaKegiatan.setObjectName("lineEditNamaKegiatan")

        self.labelKategori = QtWidgets.QLabel(self.centralwidget)
        self.labelKategori.setGeometry(QtCore.QRect(120, 420, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelKategori.setFont(font)
        self.labelKategori.setObjectName("labelKategori")

        self.lineEditKategori = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditKategori.setGeometry(QtCore.QRect(330, 420, 231, 23))
        self.lineEditKategori.setObjectName("lineEditKategori")

        self.labelKategori_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelKategori_2.setGeometry(QtCore.QRect(120, 490, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelKategori_2.setFont(font)
        self.labelKategori_2.setObjectName("labelKategori_2")

        # self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.progressBar.setGeometry(QtCore.QRect(120, 530, 441, 21))
        # self.progressBar.setProperty("value", 24)
        # self.progressBar.setObjectName("progressBar")

        self.buttonEdit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEdit.setGeometry(QtCore.QRect(130, 580, 111, 41))
        self.buttonEdit.setObjectName("buttonEdit")

        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAdd.setGeometry(QtCore.QRect(260, 580, 111, 41))
        self.buttonAdd.setObjectName("buttonAdd")

        self.buttonDelete = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDelete.setGeometry(QtCore.QRect(410, 580, 111, 41))
        self.buttonDelete.setObjectName("buttonDelete")

        # self.sliderProgress = QtWidgets.QSlider(self.centralwidget)
        # self.sliderProgress.setGeometry(QtCore.QRect(120, 540, 431, 22))
        # self.sliderProgress.setOrientation(QtCore.Qt.Horizontal)
        # self.sliderProgress.setMinimum(0)
        # self.sliderProgress.setMaximum(100)
        # self.sliderProgress.setObjectName("sliderProgress")

        # self.lcdProgress = QtWidgets.QLCDNumber(self.centralwidget)
        # self.lcdProgress.setGeometry(QtCore.QRect(380, 480, 81, 41))
        # self.lcdProgress.setObjectName("lcdProgress")

        self.lineEditProgress = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditProgress.setGeometry(QtCore.QRect(330, 490, 231, 23))
        self.lineEditProgress.setObjectName("lineEditProgress")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.dateTimeUpdate.setDisplayFormat('dddd dd/MM/yyyy')
        self.dateTimeUpdate.setDate(QDate.currentDate())
        self.dateTimeUpdate.setEnabled(False)

        self.read()

        self.tableWidgetProgress.itemClicked.connect(self.get)

        self.buttonAdd.clicked.connect(self.add)

        self.buttonEdit.clicked.connect(self.edit)

        self.buttonDelete.clicked.connect(self.delete)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pro"))
        self.label_3.setText(_translate("MainWindow", "No"))
        self.label_2.setText(_translate("MainWindow", "Last Update:"))
        item = self.tableWidgetProgress.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nama Kegiatan Progress"))
        item = self.tableWidgetProgress.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Kategori Kegiatan Progress"))
        item = self.tableWidgetProgress.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Progress Kegiatan"))
        self.labelNamaProgress.setText(_translate("MainWindow", "Nama Kegiatan Progress: "))
        self.labelKategori.setText(_translate("MainWindow", "Kategori Kegiatan Progress:"))
        self.labelKategori_2.setText(_translate("MainWindow", "Progress Kegiatan [PERSEN]: "))
        self.buttonEdit.setText(_translate("MainWindow", "Edit"))
        self.buttonDelete.setText(_translate("MainWindow", "Delete"))
        self.buttonAdd.setText(_translate("MainWindow", "Add"))

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def read(self):
        con = pymysql.connect(db='prono', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        result = cur.execute("SELECT nama_activity, kategori_progress, progres_activity FROM activity_log")
        self.tableWidgetProgress.setRowCount(0)

        for row_number, row_data in enumerate(cur):
            self.tableWidgetProgress.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetProgress.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(data))

    def get(self):
        self.lineEditNamaKegiatan.setEnabled(True)
        self.lineEditKategori.setEnabled(True)
        self.lineEditProgress.setEnabled(True)
        indexes = []
        for selectionRange in self.tableWidgetProgress.selectedRanges():
            indexes.extend(range(selectionRange.topRow(), selectionRange.bottomRow() + 1))
        for i in indexes:
            self.lineEditNamaKegiatan.setText(self.tableWidgetProgress.item(i, 0).text())
            self.lineEditKategori.setText(self.tableWidgetProgress.item(i, 1).text())
            self.lineEditProgress.setText(self.tableWidgetProgress.item(i, 2).text())
            # self.sliderProgress.setValue(self.tableWidgetProgress.item(i, 2).text())

    def add(self):
        nama = self.lineEditNamaKegiatan.text()
        progres = self.lineEditProgress.text()
        kategori = self.lineEditKategori.text()
        insert = (nama, progres, kategori)
        print(insert)
        if self.lineEditNamaKegiatan.text() and self.lineEditProgress.text() and self.lineEditKategori.text():
            con = pymysql.connect(db='prono', user='root', passwd='', host='localhost', port=3306, autocommit=True)
            cur = con.cursor()
            sql = "INSERT INTO activity_log(nama_activity, progres_activity, kategori_progress)" + "VALUES"+ str(insert)
            data = cur.execute(sql)
            self.messagebox("SUKSES", "Data Berhasil Ditambahkan")
            self.read()
            self.clear()
        else:
            self.messagebox("GAGAL", "Mohon lengkapi form ")

    def edit(self):
        nama = self.lineEditNamaKegiatan.text()
        progres = self.lineEditProgress.text()
        kategori = self.lineEditKategori.text()
        con = pymysql.connect(db='prono', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "UPDATE activity_log SET nama_activity=%s, kategori_progress=%s, progres_activity=%s" \
              "WHERE nama_activity=%s"
        data = cur.execute(sql, (nama, kategori, progres, nama))
        if (data):
            self.messagebox("SUKSES", "Data Progress Berhasil Di Edit")
        else:
            self.messagebox("GAGAL", "Data Progress Gagal Di Edit")
        self.read()
        self.clear()

    def delete(self):
        nama = self.lineEditNamaKegiatan.text()
        con = pymysql.connect(db='prono', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "DELETE FROM activity_log where nama_activity=%s"
        data = cur.execute(sql, (nama))
        if (data):
            self.messagebox("SUKSES", "Data Progress Berhasil Di Hapus")
        else:
            self.messagebox("GAGAL", "Data Progress Gagal Di Hapus")
        self.read()
        self.clear()

    def clear(self):
        self.lineEditNamaKegiatan.clear()
        self.lineEditKategori.clear()
        self.lineEditProgress.clear()

# class formTambah(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.formTambah = Ui_FormTambahV1()
#         self.formTambah.setupUi(self)
#         self.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LandingPage2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
