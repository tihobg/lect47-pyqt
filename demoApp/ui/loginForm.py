# import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6 import QtWidgets as qtw

from form import Ui_Form

class LoginForm(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create user input widgets
        user_name_input = qtw.QLineEdit()
        self.show()
        # self.setupUi(self)