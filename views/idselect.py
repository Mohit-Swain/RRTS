# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'idselect.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Idselect(object):
    def __init__(self):
        self.maxValue = 10


    def setupUi(self, Idselect):
        Idselect.setObjectName("Idselect")
        Idselect.resize(275, 218)
        font = QtGui.QFont()
        font.setPointSize(9)
        Idselect.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Idselect)
        self.buttonBox.setGeometry(QtCore.QRect(20, 170, 251, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Idselect)
        self.label.setGeometry(QtCore.QRect(70, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.idBox = QtWidgets.QSpinBox(Idselect)
        self.idBox.setGeometry(QtCore.QRect(110, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.idBox.setFont(font)
        self.idBox.setMinimum(1)
        self.idBox.setMaximum(self.maxValue)
        self.idBox.setObjectName("idBox")

        self.retranslateUi(Idselect)
        self.buttonBox.accepted.connect(Idselect.accept)
        self.buttonBox.rejected.connect(Idselect.reject)
        QtCore.QMetaObject.connectSlotsByName(Idselect)

    def retranslateUi(self, Idselect):
        _translate = QtCore.QCoreApplication.translate
        Idselect.setWindowTitle(_translate("Idselect", "Dialog"))
        self.label.setText(_translate("Idselect", "Select index:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Idselect = QtWidgets.QDialog()
    ui = Ui_Idselect()
    ui.setupUi(Idselect)
    Idselect.show()
    sys.exit(app.exec_())
