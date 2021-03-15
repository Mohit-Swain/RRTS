# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'residentInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from DB import residentTable

class Ui_residentInfo(object):
    def __init__(self,residentId = None):
        self.residentId = residentId

    def setupUi(self, residentInfo):
        residentInfo.setObjectName("residentInfo")
        residentInfo.resize(400, 293)
        self.buttonBox = QtWidgets.QDialogButtonBox(residentInfo)
        self.buttonBox.setGeometry(QtCore.QRect(0, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_5 = QtWidgets.QLabel(residentInfo)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 91, 21))
        self.label_5.setObjectName("label_5")
        self.label_ = QtWidgets.QLabel(residentInfo)
        self.label_.setGeometry(QtCore.QRect(10, 95, 91, 21))
        self.label_.setObjectName("label_5")
        self.name = QtWidgets.QLineEdit(residentInfo)
        self.name.setEnabled(False)
        self.name.setGeometry(QtCore.QRect(110, 70, 261, 22))
        self.name.setObjectName("name")
        self.phoneInput = QtWidgets.QLineEdit(residentInfo)
        self.phoneInput.setEnabled(False)
        self.phoneInput.setGeometry(QtCore.QRect(110, 120, 261, 22))
        self.phoneInput.setObjectName("phoneInput")
        self.idInput = QtWidgets.QLineEdit(residentInfo)
        self.idInput.setEnabled(False)
        self.idInput.setGeometry(QtCore.QRect(110, 95, 261, 22))
        self.idInput.setObjectName("phoneInput")
        self.label_3 = QtWidgets.QLabel(residentInfo)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 111, 21))
        self.label_3.setObjectName("label_3")
        self.idLabel = QtWidgets.QLabel(residentInfo)
        self.idLabel.setGeometry(QtCore.QRect(90, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("idLabel")
        self.label_6 = QtWidgets.QLabel(residentInfo)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 71, 21))
        self.label_6.setObjectName("label_6")
        self.addressInput = QtWidgets.QTextBrowser(residentInfo)
        self.addressInput.setGeometry(QtCore.QRect(100, 150, 281, 91))
        self.addressInput.setObjectName("addressInput")

        self.retranslateUi(residentInfo)
        self.buttonBox.accepted.connect(residentInfo.accept)
        self.buttonBox.rejected.connect(residentInfo.reject)
        QtCore.QMetaObject.connectSlotsByName(residentInfo)

    def retranslateUi(self, residentInfo):
        _translate = QtCore.QCoreApplication.translate
        residentInfo.setWindowTitle(_translate("residentInfo", "resident info"))
        self.label_5.setText(_translate("residentInfo", "phone No:"))
        self.label_.setText(_translate("residentInfo","Govt Id : "))
        # self.name.setText(_translate("residentInfo", "a"))
        # self.phoneInput.setText(_translate("residentInfo", "c"))
        self.label_3.setText(_translate("residentInfo", "Resident Name:"))
        # self.idLabel.setText(_translate("residentInfo", "Resident Id : "))
        self.label_6.setText(_translate("residentInfo", "Address:"))
        self.updateResident()

    def updateResident(self):
        if self.residentId is None:
            return
        val = residentTable.getResidentById(self.residentId)
        _translate = QtCore.QCoreApplication.translate
        if val is not None:
            self.idLabel.setText(_translate("residentInfo", "Resident Id : " + str(self.residentId)))
            self.name.setText(_translate("residentInfo", val[1]))
            self.idInput.setText(_translate("residnetInfo",val[2]))
            self.addressInput.setText(_translate("residentInfo",val[3]))
            self.phoneInput.setText(_translate("residentInfo", str(val[4])))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    residentInfo = QtWidgets.QDialog()
    ui = Ui_residentInfo(1)
    ui.setupUi(residentInfo)
    residentInfo.show()
    sys.exit(app.exec_())
