import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget
from PyQt6.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.stacked_layout = QStackedLayout()
        self.central_widget.setLayout(self.stacked_layout)
        # adding the first page
        self.page1 = loadUi("front.ui")
        self.stacked_layout.addWidget(self.page1)
        # adding the second page
        self.page2 = loadUi("page2.ui")
        self.stacked_layout.addWidget(self.page2)
        # adding the knapSack page
        self.knapSacpage1 = loadUi("knapSack.ui")
        self.stacked_layout.addWidget(self.knapSacpage1)
        # adding the btns functionalities
        self.page1.nextPage.clicked.connect(self.showPage2)
        self.page2.knapSack.clicked.connect(self.showPageKnapSack1)


    def showPage2(self):
        self.stacked_layout.setCurrentIndex(1)
    def showPageKnapSack1(self):
        self.stacked_layout.setCurrentIndex(2)

app = QApplication([])
window = MainWindow()
window.resize(1000, 900)
window.show()
sys.exit(app.exec())
