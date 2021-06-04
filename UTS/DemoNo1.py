import sys
from formMahasiswa import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class DemoNo1(QDialog):
    def __init__(self,parent = None):
        QDialog. __init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.bt_edit.clicked.connect(self.editClicked)
        self.ui.bt_tambah.clicked.connect(self.addClicked)
        self.ui.bt_clear.clicked.connect(self.clearClicked)

    def editClicked(self):
        QMessageBox.information(self, 'Edit', 'Data %s telah diubah!' %self.ui.lineEdit_2.text())
    def addClicked(self):
        QMessageBox.information(self, 'Add', 'Data %s telah ditambah!' %self.ui.lineEdit_2.text())
    def clearClicked(self):
        QMessageBox.information(self, 'Clear', 'Data %s telah diclear!' %self.ui.lineEdit_2.text())

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = DemoNo1()
    form.show()
    a.exec_()