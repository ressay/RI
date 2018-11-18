
import Main
from PyQt4 import QtGui, QtCore
import sys
import basicMethods as bm
import BasicUIMethods as buim
from TableModel import MyTableModel
from VectorialModel import scoreInnerProduct, scoreCoefDice, scoreCosin, scoreJaccard
from check import checkTable
import subprocess

class MainApp(QtGui.QMainWindow, Main.Ui_MainWindow):
    path = "prof/D"
    N = 4
    def __init__(self, parent=None):
        self.models = {}
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        # self.listView.setModel(self.model)
        self.tableViews = {}

        self.freqs = bm.generateReversedFile(self.path,self.N)
        self.weights = bm.getWeights(self.freqs,self.N)
        self.methodsMap = {
            "produit interne" : scoreInnerProduct,
            "coefficient dice":scoreCoefDice,
            "cosinus":scoreCosin,
            "Jaccard":scoreJaccard
        }
        methods = ["produit interne","coefficient dice","cosinus","Jaccard"]
        methods = [self.tr(st) for st in methods]
        self.vecCombo.addItems(methods)
        self.probCombo.addItems(methods)
        self.tabs = {
            "term":self.tab,
            "doc":self.tab2,
            "bool":self.tab_2,
            "vec":self.tab_13,
            "prob":self.tab_3
        }
        self.headers = {
            "term":['Document', 'Frequence', 'Poids'],
            "doc":['Mot','Frequence','Poids'],
            "bool":['Document'],
            "vec":['Document', 'Similarite'],
            "prob":['Pertinence','Document', 'Similarite']
                        }
        self.modelsList = {
            "term": MyTableModel([],self.headers["term"]),
            "doc": MyTableModel([],self.headers["doc"]),
            "bool": MyTableModel([],self.headers["bool"]),
            "vec": MyTableModel([],self.headers["vec"]),
            "prob": checkTable(self,[],self.headers["prob"])
        }
        self.initTabs()
        self.initButtons()
        self.savedProbaText = ""



    def initButtons(self):
        self.termButton.clicked.connect(self.termClickedCallBack)
        self.docButton.clicked.connect(self.docClickedCallBack)
        self.boolButton.clicked.connect(self.boolClickedCallBack)
        self.vecButton.clicked.connect(self.vecClickedCallBack)
        self.probButton.clicked.connect(self.probClickedCallBack)
        self.probButton2.clicked.connect(self.prob2ClickedCallBack)
        self.probButton2.setVisible(False)
        self.probButton2.setEnabled(False)


    def initTabs(self):
        for key in self.tabs:
            tableView = QtGui.QTableView(self.tabs[key])
            tableView.doubleClicked.connect(lambda x, key=key: self.tableClickedCallBack(x, key))
            tableView.setGeometry(QtCore.QRect(10, 140, 621, 300))
            tableView.setShowGrid(True)
            # tableView.setObjectName(Main._fromUtf8("t"))
            model = self.modelsList[key]
            tableView.setModel(model)

            # tableView.verticalHeader().setVisible(False)
            self.tableViews[key] = tableView
            self.models[key] = model
            tableView.model().layoutChanged.emit()
            self.setTableWidth(tableView)


    def setTableWidth(self,table):
        header = table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)



    def termClickedCallBack(self):
        if self.termEdit.toPlainText() == "":
            return
        self.resetItems("term")
        self.addItemsToList("term",buim.formatDocWeightsOutput(self.weights,self.freqs,
                                                               str(self.termEdit.toPlainText()),self.N))

    def docClickedCallBack(self):
        print (self.docEdit.toPlainText())
        if self.docEdit.toPlainText() == "":
            return
        self.resetItems("doc")
        self.addItemsToList("doc",buim.formatWeightsPerDocOutput(self.weights,self.freqs,
                                                               int(self.docEdit.toPlainText()),self.N))
        print("finally")

    def boolClickedCallBack(self):
        if self.boolEdit.toPlainText() == "":
            return
        self.resetItems("bool")
        self.addItemsToList("bool",buim.formatWeightsBoolean(self.freqs,
                                                               str(self.boolEdit.toPlainText()),self.N))

    def vecClickedCallBack(self):
        if self.vecEdit.toPlainText() == "":
            return
        self.resetItems("vec")
        method = str(self.vecCombo.currentText())
        method = self.methodsMap[method]
        self.addItemsToList("vec",buim.formatWeightsVec(self.freqs,
                                    str(self.vecEdit.toPlainText()),self.N,method))

    def probClickedCallBack(self):
        if self.probEdit.toPlainText() == "":
            return
        self.resetItems("prob")
        method = str(self.probCombo.currentText())
        method = self.methodsMap[method]
        self.savedProbaText = str(self.probEdit.toPlainText())
        self.addItemsToList("prob",buim.formatWeightsProb(self.freqs,
                                    self.savedProbaText,self.N,method))
        self.probButton2.setVisible(True)
        self.probButton2.setEnabled(True)

    def prob2ClickedCallBack(self):
        checked = self.models["prob"].getChecked()
        self.resetItems("prob")
        self.addItemsToList("prob", buim.formatWeightsProb2(self.freqs,
                                                           self.savedProbaText, self.N, checked))

    def resetItems(self,key):
        model = self.models[key]
        model.clear()

    def addItemsToList(self, key, values):
        model = self.models[key]
        tableView = self.tableViews[key]
        for value in values:
            model.addRow(value)

        tableView.model().layoutChanged.emit()
        self.setTableWidth(tableView)

    def tableClickedCallBack(self,mi,key):
        row = mi.row()
        column = mi.column()
        print(key)
        print(str(self.models[key].getData(row,column)))
        if self.headers[key][column] == 'Document':
            self.openFile(str(self.models[key].getData(row,column)))

    def openFile(self,d):
        name = self.path+d+".txt"
        subprocess.Popen(['gedit', name])

def main():
    app = QtGui.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()