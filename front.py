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
        # adding the first page   (0)
        self.page1 = loadUi("front.ui")
        self.stacked_layout.addWidget(self.page1)
        # adding the second page    (1)
        self.page2 = loadUi("page2.ui")
        self.stacked_layout.addWidget(self.page2)
        # adding the knapSack page 1  (2)
        self.knapSacpage1 = loadUi("knapSack.ui")
        self.stacked_layout.addWidget(self.knapSacpage1)
        # adding the knapSack page 2  (3)
        self.knapSacpage2 = loadUi("KanpSackSolution.ui")
        self.stacked_layout.addWidget(self.knapSacpage2)
        # adding the solution page    (4)
        self.solutionPage = loadUi("solutionPage.ui")
        self.stacked_layout.addWidget(self.solutionPage)
        # adding the productionPlanning page 1    (5)
        self.productionPlanning1 = loadUi("productionPlanning.ui")
        self.stacked_layout.addWidget(self.productionPlanning1)
        # adding the productionPlanning page 2    (6)
        self.productionPlanning2 = loadUi("productionPlanningSolution.ui")
        self.stacked_layout.addWidget(self.productionPlanning2)
        # adding the productionPlanning page 3      (7)
        self.productionPlanning3 = loadUi("productionPlanningSolution2.ui")
        self.stacked_layout.addWidget(self.productionPlanning3)

        # adding the btns functionalities
        # for the first page
        self.page1.nextPage.clicked.connect(self.showPage2)
        # for the second page
        self.page2.knapSack.clicked.connect(self.showPageKnapSack1)
        self.page2.planningProduction.clicked.connect(self.showPageplanningProduction1)
        # for knapSack pages
        self.knapSacpage1.toKnapSackPage.clicked.connect(self.showPageknapSac2)
        self.knapSacpage2.toSolutionPage.clicked.connect(self.showPageSolution)
        # for productionPlanning pages
        self.productionPlanning1.toProductionPlanningPage.clicked.connect(self.showPageproductionPlanning2)
        self.productionPlanning2.toProductionPlanningPage2.clicked.connect(self.showPageproductionPlanning3)
        self.productionPlanning3.toSolutionPage.clicked.connect(self.showPageSolution)
        # ofr the solution page
        self.solutionPage.nextPage.clicked.connect(self.showPage1)

    def showPage1(self):
        self.stacked_layout.setCurrentIndex(0)
    def showPage2(self):
        self.stacked_layout.setCurrentIndex(1)
    def showPageKnapSack1(self):
        self.stacked_layout.setCurrentIndex(2)
    def showPageplanningProduction1(self):
        self.stacked_layout.setCurrentIndex(5)
    def showPageknapSac2(self):
        self.stacked_layout.setCurrentIndex(3)
    def showPageSolution(self):
        self.stacked_layout.setCurrentIndex(4)
    def showPageproductionPlanning2(self):
        self.stacked_layout.setCurrentIndex(6)
    def showPageproductionPlanning3(self):
        self.stacked_layout.setCurrentIndex(7)

app = QApplication([])
window = MainWindow()
window.resize(1000, 900)
window.show()
sys.exit(app.exec())
