# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from views.supervisor.residentInfo import Ui_residentInfo

class Ui_ShowInfo(object):
    def __init__(self,*args):
        self.idVal = None
        self.locVal = None
        self.startVal = None
        self.endVal = None
        self.residentId = None
        self.priorityVal = None
        self.rawMaterialVal = None
        self.machinesVal = None
        self.statisticsVal = None
        if len(args) == 1 and  len(args[0]) == 10:
            args = args[0]
            self.idVal = str(args[0])
            self.locVal = args[1]
            self.startVal = args[2]
            self.endVal = args[3]
            self.residentId = args[4]
            self.priorityVal = str(args[6])
            self.rawMaterialVal = args[7]
            self.machinesVal = args[8]
            self.statisticsVal = args[9]


    def setupUi(self, ShowInfo):
        ShowInfo.setObjectName("ShowInfo")
        ShowInfo.resize(530, 679)
        font = QtGui.QFont()
        font.setPointSize(9)
        ShowInfo.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(ShowInfo)
        self.buttonBox.setGeometry(QtCore.QRect(410, 630, 91, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(ShowInfo)
        self.label.setGeometry(QtCore.QRect(180, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(ShowInfo)
        self.line.setGeometry(QtCore.QRect(40, 50, 441, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(ShowInfo)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 91, 21))
        self.label_3.setObjectName("label_3")
        self.idInput = QtWidgets.QLineEdit(ShowInfo)
        self.idInput.setEnabled(False)
        self.idInput.setGeometry(QtCore.QRect(120, 90, 113, 22))
        self.idInput.setObjectName("idInput")
        self.label_4 = QtWidgets.QLabel(ShowInfo)
        self.label_4.setGeometry(QtCore.QRect(260, 90, 71, 21))
        self.label_4.setObjectName("label_4")
        self.roadInput = QtWidgets.QLineEdit(ShowInfo)
        self.roadInput.setEnabled(False)
        self.roadInput.setGeometry(QtCore.QRect(342, 90, 151, 22))
        self.roadInput.setObjectName("roadInput")
        self.label_5 = QtWidgets.QLabel(ShowInfo)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 91, 21))
        self.label_5.setObjectName("label_5")
        self.startInput = QtWidgets.QLineEdit(ShowInfo)
        self.startInput.setEnabled(False)
        self.startInput.setGeometry(QtCore.QRect(102, 140, 141, 22))
        self.startInput.setObjectName("startInput")
        self.label_6 = QtWidgets.QLabel(ShowInfo)
        self.label_6.setGeometry(QtCore.QRect(260, 140, 91, 21))
        self.label_6.setObjectName("label_6")
        self.endInput = QtWidgets.QLineEdit(ShowInfo)
        self.endInput.setEnabled(False)
        self.endInput.setGeometry(QtCore.QRect(342, 140, 151, 22))
        self.endInput.setObjectName("endInput")
        self.line_2 = QtWidgets.QFrame(ShowInfo)
        self.line_2.setGeometry(QtCore.QRect(120, 220, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.priorityInput = QtWidgets.QLineEdit(ShowInfo)
        self.priorityInput.setEnabled(False)
        self.priorityInput.setGeometry(QtCore.QRect(260, 250, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.priorityInput.setFont(font)
        self.priorityInput.setObjectName("priorityInput")
        self.label_7 = QtWidgets.QLabel(ShowInfo)
        self.label_7.setGeometry(QtCore.QRect(160, 250, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.residentBtn = QtWidgets.QPushButton(ShowInfo)
        self.residentBtn.setGeometry(QtCore.QRect(190, 180, 141, 31))
        self.residentBtn.setObjectName("residentBtn")
        self.residentBtn.clicked.connect(self.showResidents)
        if not self.residentId:
            self.residentBtn.setEnabled(False)
        self.label_2 = QtWidgets.QLabel(ShowInfo)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 91, 31))
        self.label_2.setObjectName("label_2")
        self.rawMaterialInput = QtWidgets.QTextBrowser(ShowInfo)
        self.rawMaterialInput.setGeometry(QtCore.QRect(120, 290, 381, 91))
        self.rawMaterialInput.setObjectName("rawMaterialInput")
        self.machinesInput = QtWidgets.QTextBrowser(ShowInfo)
        self.machinesInput.setGeometry(QtCore.QRect(120, 400, 381, 91))
        self.machinesInput.setObjectName("machinesInput")
        self.label_8 = QtWidgets.QLabel(ShowInfo)
        self.label_8.setGeometry(QtCore.QRect(20, 390, 91, 31))
        self.label_8.setObjectName("label_8")
        self.statisticsInput = QtWidgets.QTextBrowser(ShowInfo)
        self.statisticsInput.setGeometry(QtCore.QRect(120, 500, 381, 91))
        self.statisticsInput.setObjectName("statisticsInput")
        self.label_9 = QtWidgets.QLabel(ShowInfo)
        self.label_9.setGeometry(QtCore.QRect(20, 490, 91, 31))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(ShowInfo)
        self.buttonBox.accepted.connect(ShowInfo.accept)
        self.buttonBox.rejected.connect(ShowInfo.reject)
        QtCore.QMetaObject.connectSlotsByName(ShowInfo)

    def retranslateUi(self, ShowInfo):
        _translate = QtCore.QCoreApplication.translate
        ShowInfo.setWindowTitle(_translate("ShowInfo", "show repair info"))
        self.label.setText(_translate("ShowInfo", "Road Repair Info"))
        self.label_3.setText(_translate("ShowInfo", "Complaint Id:"))
        self.idInput.setText(_translate("ShowInfo", self.idVal))
        self.label_4.setText(_translate("ShowInfo", "Road Loc:"))
        self.roadInput.setText(_translate("ShowInfo", self.locVal))
        self.label_5.setText(_translate("ShowInfo", "StartLoc:"))
        self.startInput.setText(_translate("ShowInfo", self.startVal))
        self.label_6.setText(_translate("ShowInfo", "EndLoc:"))
        self.endInput.setText(_translate("ShowInfo", self.endVal))
        self.priorityInput.setText(_translate("ShowInfo", self.priorityVal))
        self.label_7.setText(_translate("ShowInfo", "Priority:"))
        self.residentBtn.setText(_translate("ShowInfo", "Show Resident"))
        self.label_2.setText(_translate("ShowInfo", "Raw Material:"))
        self.rawMaterialInput.setText(_translate("ShowInfo",self.rawMaterialVal))
        self.label_8.setText(_translate("ShowInfo", "Machines:"))
        self.machinesInput.setText(_translate("ShowInfo",self.machinesVal))
        self.label_9.setText(_translate("ShowInfo", "Statistics:"))
        self.statisticsInput.setText(_translate("ShowInfo",self.statisticsVal))

    def showResidents(self):
        residentInfo = QtWidgets.QDialog()
        ui = Ui_residentInfo(self.residentId)
        ui.setupUi(residentInfo)
        residentInfo.show()
        residentInfo.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShowInfo = QtWidgets.QDialog()
    ui = Ui_ShowInfo()
    ui.setupUi(ShowInfo)
    ShowInfo.show()
    sys.exit(app.exec_())
