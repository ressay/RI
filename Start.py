
import Main
from PyQt4 import QtGui, QtCore
import sys
import basicMethods as bm
import BasicUIMethods as buim
from TableModel import MyTableModel


class MainApp(QtGui.QMainWindow, Main.Ui_MainWindow):
    path = "Chek/D"
    N = 3
    def __init__(self, parent=None):
        self.models = {}
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        # self.listView.setModel(self.model)
        self.tableViews = {}

        self.freqs = bm.generateReversedFile(self.path,self.N)
        self.weights = bm.getWeights(self.freqs,self.N)
        self.tabs = {"term":self.tab,"doc":self.tab2,"bool":self.tab_2,"vec":self.tab_13}
        self.headers = {
            "term":['Document', 'frequence', 'poids'],
            "doc":['word','frequence','poids'],
            "bool":['Document'],
            "vec":['Document', 'Similarite']
                        }

        self.initTabs()
        self.initButtons()


    def initButtons(self):
        self.termButton.clicked.connect(self.termClickedCallBack)
        self.docButton.clicked.connect(self.docClickedCallBack)
        self.boolButton.clicked.connect(self.boolClickedCallBack)
        self.vecButton.clicked.connect(self.vecClickedCallBack)


    def initTabs(self):
        for key in self.tabs:
            tableView = QtGui.QTableView(self.tabs[key])
            tableView.setGeometry(QtCore.QRect(10, 140, 621, 341))
            tableView.setShowGrid(True)
            # tableView.setObjectName(Main._fromUtf8("t"))
            header = self.headers[key]
            model = MyTableModel([],header)
            tableView.setModel(model)

            # tableView.verticalHeader().setVisible(False)
            self.tableViews[key] = tableView
            self.models[key] = model

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
        self.addItemsToList("vec",buim.formatWeightsVec(self.freqs,
                                    str(self.vecEdit.toPlainText()),self.N,"yes"))

    def resetItems(self,key):
        model = self.models[key]
        model.arraydata = []

    def addItemsToList(self, key, values):
        model = self.models[key]
        tableView = self.tableViews[key]
        for value in values:
            model.arraydata.append(value)

        tableView.model().layoutChanged.emit()
        self.setTableWidth(tableView)


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()