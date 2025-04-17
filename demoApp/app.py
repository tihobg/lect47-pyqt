import sys
from PyQt6 import QtWidgets as qtw
from demoApp.ui.loginForm import LoginForm
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from form import Ui_Form


class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create user input widgets
        user_name_input = qtw.QLineEdit()
        self.setWindowTitle('Demo App')
        self.setGeometry(100, 100, 500, 500)

        # create widgets
        btnRegistration = qtw.QPushButton('Registration')
        btnLogin = qtw.QPushButton('Login')

        # create main layout
        main_layout = qtw.QHBoxLayout(self)
        main_layout.addWidget(btnRegistration)
        main_layout.addWidget(btnLogin)

        self.show()


if __name__ == '__main__':

    app = qtw.QApplication(sys.argv)

    # window = QWidget()
    window = MainWindow()
    # window.setWindowTitle('demo App')
    # window.setGeometry(100, 100, 500, 500)

    # window.show()
    sys.exit(app.exec())

