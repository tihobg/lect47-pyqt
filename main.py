import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from form import Ui_Form

class MyMainApp(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)

# window = QWidget()
window = MyMainApp()
window.setWindowTitle('PyQt6 App Works')
window.setGeometry(100, 100, 500, 500)

window.show()
sys.exit(app.exec())

