# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 686)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSelectFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelectFile.setObjectName("btnSelectFile")
        self.horizontalLayout.addWidget(self.btnSelectFile)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnAddRow = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddRow.setObjectName("btnAddRow")
        self.horizontalLayout.addWidget(self.btnAddRow)
        self.btnAddColumn = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddColumn.setObjectName("btnAddColumn")
        self.horizontalLayout.addWidget(self.btnAddColumn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSelectFile.setText(_translate("MainWindow", "Загрузить данные"))
        self.btnSave.setText(_translate("MainWindow", "Сохранить"))
        self.btnAddRow.setText(_translate("MainWindow", "Добавить строку"))
        self.btnAddColumn.setText(_translate("MainWindow", "Добавить столбец"))
