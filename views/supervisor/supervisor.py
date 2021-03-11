# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'supervisor.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from DB import scheduleTable
from views.idselect import Ui_Idselect
from views.supervisor.showInfo import Ui_ShowInfo
from views.supervisor.editInfo import Ui_EditInfo
class Ui_MainSupervisor(object):
    def __init__(self):
        self.schedule = ()

    def setupUi(self, MainSupervisor):
        MainSupervisor.setObjectName("MainSupervisor")
        MainSupervisor.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainSupervisor.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainSupervisor)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 521, 451))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(194, 194, 194))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(194, 194, 194))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(194, 194, 194))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(194, 194, 194))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(194, 194, 194))
        self.tableWidget.setHorizontalHeaderItem(4, item)


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(600, 120, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.showButton.setFont(font)
        self.showButton.setObjectName("showButton")
        self.showButton.clicked.connect(self.showInfo)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(600, 230, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editButton.setFont(font)
        self.editButton.setObjectName("editButton")
        self.editButton.clicked.connect(lambda : self.editInfo(MainSupervisor))
        MainSupervisor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainSupervisor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainSupervisor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainSupervisor)
        self.statusbar.setObjectName("statusbar")
        MainSupervisor.setStatusBar(self.statusbar)
        self.actionDevelopers = QtWidgets.QAction(MainSupervisor)
        self.actionDevelopers.setObjectName("actionDevelopers")
        self.menuAbout.addAction(self.actionDevelopers)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainSupervisor)
        QtCore.QMetaObject.connectSlotsByName(MainSupervisor)

    def retranslateUi(self, MainSupervisor):
        _translate = QtCore.QCoreApplication.translate
        MainSupervisor.setWindowTitle(_translate("MainSupervisor", "MainWindow"))
        self.label.setText(_translate("MainSupervisor", "Supervisor"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainSupervisor", "CompId"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainSupervisor", "RoadLoc"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainSupervisor", "Start Loc"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainSupervisor", "End Loc"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainSupervisor", "Priority"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.updateTable()
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainSupervisor", "Road Repair Schedule:"))
        self.showButton.setText(_translate("MainSupervisor", "Show Info"))
        self.editButton.setText(_translate("MainSupervisor", "Edit Info"))
        self.menuMain.setTitle(_translate("MainSupervisor", "Main"))
        self.menuAbout.setTitle(_translate("MainSupervisor", "About"))
        self.actionDevelopers.setText(_translate("MainSupervisor", "Developers"))

    def updateTable(self):
        _translate = QtCore.QCoreApplication.translate
        self.schedule = scheduleTable.getSchedule()

        self.tableWidget.setRowCount(len(self.schedule))
        getitems = (0,1,2,3,6)
        for i,t in enumerate(self.schedule):
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i+1))
            self.tableWidget.setVerticalHeaderItem(i, item)
            for j,idx in enumerate(getitems):
                item = QtWidgets.QTableWidgetItem()
                item.setText(_translate("MainSupervisor", str(t[idx])))
                self.tableWidget.setItem(i, j, item)

    def getIndex(self):
        Idselect = QtWidgets.QDialog()
        ui = Ui_Idselect()
        ui.maxValue = len(self.schedule)
        ui.setupUi(Idselect)
        Idselect.show()
        if Idselect.exec_():
            return int(ui.idBox.text()) - 1

        return None

    def showInfo(self):
        idx = self.getIndex()
        if idx is not None:
            ShowInfo = QtWidgets.QDialog()
            ui = Ui_ShowInfo(self.schedule[idx])
            ui.setupUi(ShowInfo)
            ShowInfo.show()
            ShowInfo.exec_()

    def editInfo(self,win):
        idx = self.getIndex()
        if idx is not None:
            editInfo = QtWidgets.QDialog()
            ui = Ui_EditInfo(self.schedule[idx])
            ui.setupUi(editInfo)
            editInfo.show()
            editInfo.exec_()
            self.updateTable()
            self.retranslateUi(win)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainSupervisor = QtWidgets.QMainWindow()
    ui = Ui_MainSupervisor()
    ui.setupUi(MainSupervisor)
    MainSupervisor.show()
    sys.exit(app.exec_())
