# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 651, 561))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.termLabel = QtGui.QLabel(self.tab)
        self.termLabel.setGeometry(QtCore.QRect(290, 10, 64, 20))
        self.termLabel.setObjectName(_fromUtf8("termLabel"))
        self.termEdit = QtGui.QTextEdit(self.tab)
        self.termEdit.setGeometry(QtCore.QRect(210, 40, 201, 21))
        self.termEdit.setObjectName(_fromUtf8("termEdit"))
        self.termButton = QtGui.QPushButton(self.tab)
        self.termButton.setGeometry(QtCore.QRect(340, 80, 71, 32))
        self.termButton.setObjectName(_fromUtf8("termButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.docButton = QtGui.QPushButton(self.tab2)
        self.docButton.setGeometry(QtCore.QRect(340, 80, 71, 32))
        self.docButton.setObjectName(_fromUtf8("docButton"))
        self.docEdit = QtGui.QTextEdit(self.tab2)
        self.docEdit.setGeometry(QtCore.QRect(210, 40, 201, 21))
        self.docEdit.setObjectName(_fromUtf8("docEdit"))
        self.docLabel = QtGui.QLabel(self.tab2)
        self.docLabel.setGeometry(QtCore.QRect(290, 10, 81, 20))
        self.docLabel.setObjectName(_fromUtf8("docLabel"))
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.boolButton = QtGui.QPushButton(self.tab_2)
        self.boolButton.setGeometry(QtCore.QRect(340, 80, 71, 32))
        self.boolButton.setObjectName(_fromUtf8("boolButton"))
        self.boolEdit = QtGui.QTextEdit(self.tab_2)
        self.boolEdit.setGeometry(QtCore.QRect(210, 40, 201, 21))
        self.boolEdit.setObjectName(_fromUtf8("boolEdit"))
        self.boolLabel = QtGui.QLabel(self.tab_2)
        self.boolLabel.setGeometry(QtCore.QRect(290, 10, 81, 20))
        self.boolLabel.setObjectName(_fromUtf8("boolLabel"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_13 = QtGui.QWidget()
        self.tab_13.setObjectName(_fromUtf8("tab_13"))
        self.vecButton = QtGui.QPushButton(self.tab_13)
        self.vecButton.setGeometry(QtCore.QRect(340, 80, 71, 32))
        self.vecButton.setObjectName(_fromUtf8("vecButton"))
        self.vecEdit = QtGui.QTextEdit(self.tab_13)
        self.vecEdit.setGeometry(QtCore.QRect(210, 40, 201, 21))
        self.vecEdit.setObjectName(_fromUtf8("vecEdit"))
        self.vecLabel = QtGui.QLabel(self.tab_13)
        self.vecLabel.setGeometry(QtCore.QRect(290, 10, 81, 20))
        self.vecLabel.setObjectName(_fromUtf8("vecLabel"))
        self.vecCombo = QtGui.QComboBox(self.tab_13)
        self.vecCombo.setGeometry(QtCore.QRect(480, 40, 151, 23))
        self.vecCombo.setObjectName(_fromUtf8("vecCombo"))
        self.tabWidget.addTab(self.tab_13, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.probButton = QtGui.QPushButton(self.tab_3)
        self.probButton.setGeometry(QtCore.QRect(340, 80, 71, 32))
        self.probButton.setStyleSheet(_fromUtf8(""))
        self.probButton.setObjectName(_fromUtf8("probButton"))
        self.probLabel = QtGui.QLabel(self.tab_3)
        self.probLabel.setGeometry(QtCore.QRect(290, 10, 81, 20))
        self.probLabel.setObjectName(_fromUtf8("probLabel"))
        self.probEdit = QtGui.QTextEdit(self.tab_3)
        self.probEdit.setGeometry(QtCore.QRect(210, 40, 201, 21))
        self.probEdit.setObjectName(_fromUtf8("probEdit"))
        self.probCombo = QtGui.QComboBox(self.tab_3)
        self.probCombo.setGeometry(QtCore.QRect(480, 40, 151, 23))
        self.probCombo.setObjectName(_fromUtf8("probCombo"))
        self.probButton2 = QtGui.QPushButton(self.tab_3)
        self.probButton2.setGeometry(QtCore.QRect(310, 440, 141, 32))
        self.probButton2.setObjectName(_fromUtf8("probButton2"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.termLabel.setText(_translate("MainWindow", "Terme", None))
        self.termButton.setText(_translate("MainWindow", "OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Terme", None))
        self.docButton.setText(_translate("MainWindow", "OK", None))
        self.docLabel.setText(_translate("MainWindow", "Document", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Document", None))
        self.boolButton.setText(_translate("MainWindow", "OK", None))
        self.boolLabel.setText(_translate("MainWindow", "Booleen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Booleen", None))
        self.vecButton.setText(_translate("MainWindow", "OK", None))
        self.vecLabel.setText(_translate("MainWindow", "Vectoriel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("MainWindow", "Vectoriel", None))
        self.probButton.setText(_translate("MainWindow", "OK", None))
        self.probLabel.setText(_translate("MainWindow", "Probabiliste", None))
        self.probButton2.setText(_translate("MainWindow", "requête proba", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Probabiliste", None))

