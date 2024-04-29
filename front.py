from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication

def play() :
    return 
app = QApplication([])
window = loadUi("front.ui")
window.PL.clicked.connect(play)
window.show()
app.exec()