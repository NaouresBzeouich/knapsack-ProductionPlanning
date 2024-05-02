import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget
from PyQt6.uic import loadUi
import knapSac

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
        self.knapSacpage2.toSolutionPage.clicked.connect(self.showPageSolutionFromKnapSack)
        # for productionPlanning pages
        self.productionPlanning1.toProductionPlanningPage.clicked.connect(self.showPageproductionPlanning2)
        self.productionPlanning2.toProductionPlanningPage2.clicked.connect(self.showPageproductionPlanning3)
        self.productionPlanning3.toSolutionPage.clicked.connect(self.showPageSolutionFromProductionPlanning)
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
    def showPageSolutionFromKnapSack(self):
        # getting the inputs
        # getting the capacity
        capacity = self.knapSacpage2.capacity.text()
        print(capacity)
        # getting the items checked and add their value
        keys = []
        values = {}
        pomme_checked = self.knapSacpage2.pomme.isChecked()
        if pomme_checked:
            keys.append("pomme")
            values["pomme"] = self.knapSacpage2.pommeValue.text()
        boutielleDEau_checked = self.knapSacpage2.boutielleDEau.isChecked()
        if boutielleDEau_checked:
            keys.append("bouteilleDEeau")
            values["bouteilleDEeau"] = self.knapSacpage2.bouteilleDEauValue.text()
        lampeDePoche_checked = self.knapSacpage2.lampeDePoche.isChecked()
        if lampeDePoche_checked:
            keys.append("lampe")
            values["lampe"] = self.knapSacpage2.lampeValue.text()
        carte_checked = self.knapSacpage2.carte.isChecked()
        if carte_checked:
            keys.append("carte")
            values["carte"] = self.knapSacpage2.carteValue.text()
        kitSecours_checked = self.knapSacpage2.kitSecours.isChecked()
        if kitSecours_checked:
            keys.append("kitSecours")
            values["kitSecours"] = self.knapSacpage2.kitSecoursValue.text()
        telephone_checked = self.knapSacpage2.telephone.isChecked()
        if telephone_checked:
            keys.append("telephone")
            values["telephone"] = self.knapSacpage2.telephoneValue.text()
        livre_checked = self.knapSacpage2.livre.isChecked()
        if livre_checked:
            keys.append("livre")
            values["livre"] = self.knapSacpage2.livreValue.text()
        sacDeCouchage_checked = self.knapSacpage2.sacDeCouchage.isChecked()
        if sacDeCouchage_checked:
            keys.append("sacDeCouchage")
            values["sacDeCouchage"] = self.knapSacpage2.sacDeCouchageValue.text()
        corde_checked = self.knapSacpage2.corde.isChecked()
        if corde_checked:
            keys.append("corde")
            values["corde"] = self.knapSacpage2.cordeValue.text()
        tente_checked = self.knapSacpage2.tente.isChecked()
        if tente_checked:
            keys.append("tente")
            values["tente"] = self.knapSacpage2.tenteValue.text()
        result = self.knapSacResult(keys, values, capacity)
        print(result)
        self.solutionPage.result.setText(result)
        self.stacked_layout.setCurrentIndex(4)
    def showPageSolutionFromProductionPlanning(self):
        # hawa jeyik
        self.stacked_layout.setCurrentIndex(4)
    def showPageproductionPlanning2(self):
        self.stacked_layout.setCurrentIndex(6)
    def showPageproductionPlanning3(self):
        capacity = self.productionPlanning2.productionCapacity

        products = []
        profit = {}
        production_time = {}

        print(products)
        print(profit)
        print(production_time)
        print(capacity)
        self.stacked_layout.setCurrentIndex(7)
    def knapSacResult(self,keys, values, capacity):
        # making sure that capacity is a positive number
        if not(capacity.isdigit()):
            return " le voyageur n'avait pas correctement saisir la capacité ! \n Félix ne pouvait pas trouver une solution \n "
        if int(capacity) <= 0:
            return " le voyageur avait donné un entier negative pour la capacité maximal ! \n la capacité maximal de son sac à dos doit etre un entier strictement positive \n "
        capacity = int(capacity)
        # making sure there's  min a key checked
        if not keys:
            return " aucune information etaint inserré ,\n comment Félix pourrait-il trouver une solution ? \n "
        # making sure that every value entered is an enteger
        for key in keys:
            if not (values[key].isdigit()):
                return " les valeurs données par le voyageurs etaient incorrect ! \n \n Félix ne pouvait pas trouver une solution \n"
            if int(values[key]) == 0:
                return " il y etait un valeur non saisie ! \n \n Félix ne pouvait pas trouver une solution \n"
            values[key] = int(values[key])
        print(values)
        print(capacity)
        return knapSac.knapsack_solver(keys,values,capacity)

app = QApplication([])
window = MainWindow()
window.resize(1000, 900)
window.show()
sys.exit(app.exec())
