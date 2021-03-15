# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from views.residents.selectResidents import Ui_ResidentsWindow
from views.clerk.clerk import Ui_ClerkWindow
from views.adminstration.adminstratior import Ui_MainAdminstrator
from views.supervisor.supervisor import Ui_MainSupervisor
from views.mayor.mayor import Ui_MainMayor
from views.dialog import CustomDialog


class Ui_AppWindow(object):
    def setupUi(self, AppWindow):
        AppWindow.setObjectName("AppWindow")
        AppWindow.resize(384, 478)
        font = QtGui.QFont()
        font.setPointSize(9)
        AppWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(AppWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.residentBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.residentBtn.setGeometry(QtCore.QRect(110, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.residentBtn.setFont(font)
        self.residentBtn.setObjectName("residentBtn")
        self.clerkBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.clerkBtn.setGeometry(QtCore.QRect(110, 130, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clerkBtn.setFont(font)
        self.clerkBtn.setObjectName("clerkBtn")
        self.supervisorBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.supervisorBtn.setGeometry(QtCore.QRect(110, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.supervisorBtn.setFont(font)
        self.supervisorBtn.setObjectName("supervisorBtn")
        self.AdministratorBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.AdministratorBtn.setGeometry(QtCore.QRect(110, 210, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.AdministratorBtn.setFont(font)
        self.AdministratorBtn.setObjectName("AdministratorBtn")
        self.mayorBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.mayorBtn.setGeometry(QtCore.QRect(110, 260, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mayorBtn.setFont(font)
        self.mayorBtn.setObjectName("mayorBtn")
        self.goBtn = QtWidgets.QPushButton(self.centralwidget)
        self.goBtn.setGeometry(QtCore.QRect(130, 340, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.goBtn.setFont(font)
        self.goBtn.clicked.connect(lambda : self.launch(AppWindow))
        self.goBtn.setObjectName("goBtn")
        AppWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AppWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 384, 26))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuAbout_2 = QtWidgets.QMenu(self.menubar)
        self.menuAbout_2.setObjectName("menuAbout_2")
        AppWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AppWindow)
        self.statusbar.setObjectName("statusbar")
        AppWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuAbout_2.menuAction())

        self.retranslateUi(AppWindow)
        QtCore.QMetaObject.connectSlotsByName(AppWindow)

    def retranslateUi(self, AppWindow):
        _translate = QtCore.QCoreApplication.translate
        AppWindow.setWindowTitle(_translate("AppWindow", "MainWindow"))
        self.label.setText(_translate("AppWindow", "Pick an occupation"))
        self.residentBtn.setText(_translate("AppWindow", "Resident"))
        self.clerkBtn.setText(_translate("AppWindow", "Clerk"))
        self.supervisorBtn.setText(_translate("AppWindow", "Supervisor"))
        self.AdministratorBtn.setText(_translate("AppWindow", "Administrator"))
        self.mayorBtn.setText(_translate("AppWindow", "Mayor"))
        self.goBtn.setText(_translate("AppWindow", "Go"))
        self.menuAbout.setTitle(_translate("AppWindow", "Menu"))
        self.menuAbout_2.setTitle(_translate("AppWindow", "About"))

    def launch(self,win):
        self.launchWindow = QtWidgets.QMainWindow(win)
        if self.residentBtn.isChecked():
            ui = Ui_ResidentsWindow()
            ui.setupUi(self.launchWindow)
            self.launchWindow.show()
        elif self.clerkBtn.isChecked():
            ui = Ui_ClerkWindow()
            ui.setupUi(self.launchWindow)
            self.launchWindow.show()
        elif self.supervisorBtn.isChecked():
            ui = Ui_MainSupervisor()
            ui.setupUi(self.launchWindow)
            self.launchWindow.show()
        elif self.AdministratorBtn.isChecked():
            ui = Ui_MainAdminstrator()
            ui.setupUi(self.launchWindow)
            self.launchWindow.show()
        elif self.mayorBtn.isChecked():
            ui = Ui_MainMayor()
            ui.setupUi(self.launchWindow)
            self.launchWindow.show()
        else:
            msg = CustomDialog.init_message('Warning','No option is selected','warning')
            msg.exec_()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AppWindow = QtWidgets.QMainWindow()
    ui = Ui_AppWindow()
    ui.setupUi(AppWindow)
    AppWindow.show()
    sys.exit(app.exec_())
