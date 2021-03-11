import sys
from PyQt5.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QVBoxLayout,
    QMessageBox
)

class CustomDialog(QDialog):
    icon_dict = {
        'info' : QMessageBox.Information,
        'question' : QMessageBox.Question,
        'warning' : QMessageBox.Warning,
        'critical' : QMessageBox.Critical
    }

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self,text):
        self._text = text

    @classmethod
    def init(cls,win = None,title = "Notice!",text ="A dialog box"):
        instance = cls(win)
        instance.title = title
        instance.text = text
        return instance

    @classmethod
    def init_message(cls,title = "Notice!",text ="A dialog box",type = 'info'):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setIcon(cls.icon_dict.get(type,QMessageBox.Information))
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        return msg

    def show(self):
        self.setWindowTitle(self._title)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel(self._text)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        return self.exec_()


    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._title = "Notice!"
        self._text = "A dialog box"


    # def button_clicked(self, s):
    #     print("click", s)
    #
    #     dlg = CustomDialog()  # If you pass self, the dialog will be centered over the main window as before.
    #     if dlg.exec_():
    #         print("Success!")
    #     else:
    #         print("Cancel!")

