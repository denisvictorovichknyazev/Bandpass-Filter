# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PlotWidget import *
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1570, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 270, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 190, 151, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 241, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 231, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 130, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 10, 151, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 231, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 231, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 70, 151, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 310, 761, 400))
        self.widget.setObjectName("widget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(790, 0, 16, 711))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.layout = QtWidgets.QVBoxLayout(self.widget)
        self.m = PlotCanvas(self.widget, width=self.widget.width(), height=self.widget.height() - 50)
        self.layout.addWidget(self.m)
        self.toolbar = NavigationToolbar(self.m, self)
        self.layout.addWidget(self.toolbar)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(790, 0, 16, 711))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(800, 10, 761, 331))
        self.widget_2.setObjectName("widget_2")
        self.layout1 = QtWidgets.QVBoxLayout(self.widget_2)
        self.sig = PlotCanvas(self.widget, width=self.widget_2.width(), height=self.widget_2.height())
        self.layout1.addWidget(self.sig)
        self.toolbar1 = NavigationToolbar(self.sig, self)
        self.layout1.addWidget(self.toolbar1)

        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(800, 350, 761, 351))
        self.widget_3.setObjectName("widget_3")
        self.layout2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.n_sig = PlotCanvas(self.widget, width=self.widget_3.width(), height=self.widget_3.height())
        self.layout2.addWidget(self.n_sig)
        self.toolbar2 = NavigationToolbar(self.n_sig, self)
        self.layout2.addWidget(self.toolbar2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1570, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Рассчет фильтра"))
        self.label_2.setText(_translate("MainWindow", "Правая граница полосы пропускания,Гц"))
        self.label.setText(_translate("MainWindow", "Левая граница полосы пропускания,Гц"))
        self.label_3.setText(_translate("MainWindow", "Частота дискретизации"))
        self.label_4.setText(_translate("MainWindow", "Ширина полосы перехода"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action_2.setText(_translate("MainWindow", "Открыть"))

