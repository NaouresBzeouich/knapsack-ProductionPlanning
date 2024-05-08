import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel , QStackedLayout, QWidget , QPushButton , QLineEdit , QGroupBox
from PyQt6.uic import loadUi
import knapSac
import productionPlannuing
"""
todo : find children for all items in the planning production 
than figure out how to clone and add to the Allitems QgroupBox 

"""
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
        self.BoxCreator = self.findChild(QWidget, "BoxCreator")
        self.BoxCreator.add = self.BoxCreator.findChild(QPushButton , "add")
        self.BoxCreator.profit = self.BoxCreator.findChild(QLineEdit , "profit")
        self.BoxCreator.weight = self.BoxCreator.findChild(QLineEdit , "weight")
        self.BoxCreator.item = self.BoxCreator.findChild(QLineEdit , "item")
        self.productionPlanning2.Benefice = self.productionPlanning2.findChild(QLabel , "Benefice")
        self.productionPlanning2.items = self.productionPlanning2.findChild(QLabel , "items")
        self.productionPlanning2.resourceOn = self.productionPlanning2.findChild(QLabel , "resourceOn")
        self.BoxCreator.add.clicked.connect(self.addNewitem)
        self.productionPlanning2.error = self.productionPlanning2.findChild(QLabel , "error")

        self.BoxCreatordemande = self.findChild(QWidget, "BoxCreatordemande")
        self.BoxCreatordemande.add = self.BoxCreatordemande.findChild(QPushButton , "add")
        self.BoxCreatordemande.produit = self.BoxCreatordemande.findChild(QLineEdit , "produit")
        self.BoxCreatordemande.production = self.BoxCreatordemande.findChild(QLineEdit , "production")    
        self.productionPlanning3.error = self.productionPlanning3.findChild(QLabel , "error")
        self.productionPlanning3.Produits = self.productionPlanning3.findChild(QLabel , "Produits")
        self.productionPlanning3.productionDemande = self.productionPlanning3.findChild(QLabel , "productionDemande")
        self.productionPlanning3.toSolutionPage.clicked.connect(self.showPageSolutionFromProductionPlanning)
        self.BoxCreatordemande.add.clicked.connect(self.addNewDemande)
        print(self.BoxCreatordemande.add)
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
    def showPageproductionPlanning2(self):
        global capacity 
        capacity = 0
        global products
        products=[]
        global profits
        profits = {}
        global production_resources
        production_resources = {}   
        self.productionPlanning2.items.setText("")
        self.productionPlanning2.Benefice.setText("")
        self.productionPlanning2.resourceOn.setText("")
        self.productionPlanning2.error.setText("")  
        self.stacked_layout.setCurrentIndex(6)
    def showPageSolutionFromProductionPlanning(self):
        try : 
            print("hey this also ")
            print(str(capacity))
            result = ""
            if not result:
                result = self.productionPlanningResult(products, profits, production_resources, capacity ,demand)
            print(result)
            products.clear()
            demand.clear() 
            production_resources.clear()
            profits.clear()
            self.productionPlanning3.error.setText("")
            self.solutionPage.result.setText(result)
            self.stacked_layout.setCurrentIndex(4)
        except Exception as e : 
            print(e)
            e = str(e)
            self.productionPlanning3.error.setText("Error" + e )
    def addNewitem(self) :
        try : 
           
            product = (self.BoxCreator.item.text())
            profit = int(str(self.BoxCreator.profit.text()).strip())
            production_resource = int(str(self.BoxCreator.weight.text()).strip())
            products.append(product)
            profits[product] = profit
            production_resources[product] = production_resource
        
            x = self.productionPlanning2.items.text()
            y = self.productionPlanning2.Benefice.text()
            z = self.productionPlanning2.resourceOn.text()
            self.productionPlanning2.items.setText(x + str(product) + "\n")
            self.productionPlanning2.Benefice.setText(y+ str(profit) + "\n")
            self.productionPlanning2.resourceOn.setText(z + str(production_resource) + "\n")
            self.productionPlanning2.error.setText("")
        except Exception as e : 
            e = str(e) 
            self.productionPlanning2.error.setText("error" + e )
    def addNewDemande(self) :
        try : 
            product = (self.BoxCreatordemande.produit.text())
            production = int(str(self.BoxCreatordemande.production.text()).strip())
            if (product in products):
                demand[product] = production
            else : 
                x = str(products)
                raise Exception("les Produits valables sont : " + x )     
            x = self.productionPlanning3.Produits.text()
            y = self.productionPlanning3.productionDemande.text()
            self.productionPlanning3.Produits.setText(x + str(product) + "\n")
            self.productionPlanning3.productionDemande.setText(y+ str(production) + "\n")
            self.productionPlanning3.error.setText("")
        except Exception as e : 
            e = str(e) 
            print(e)
            self.productionPlanning3.error.setText("error : " + e )
        
    def showPageproductionPlanning3(self):
        global capacity
        capacity = self.productionPlanning2.capacity.text()
        capacity = int(capacity)
        global demand 
        demand = {}
        try :
            
            if (len(products) == 0 ) : 
                raise Exception("longeur > 0 ")
        except Exception as e : 
            print(e)
            e = str(e)
            self.productionPlanning2.error.setText("error : " + e )
            self.productionPlanning3.Produits.setText("")
            self.productionPlanning3.productionDemande.setText("")
            return
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

    def productionPlanningResult(self,products, profit,production_time, capacity,demand):
        result = productionPlannuing.solve_production_planning(products,profit,production_time,capacity,demand)
        return result
app = QApplication([])
window = MainWindow()
window.resize(1087, 1027)
window.show()
sys.exit(app.exec())
