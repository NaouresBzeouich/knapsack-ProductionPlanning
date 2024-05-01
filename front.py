import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QDialog


def play():
    dialog2 = QDialog()
    ui = loadUi("page2.ui", dialog2)
    dialog2.show()


app = QApplication(sys.argv)
window = loadUi("front.ui")
window.nextPage.clicked.connect(play)
window.show()
sys.exit(app.exec())
