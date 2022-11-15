import sys
# import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidget, QLineEdit


# from mywindow import Ui_MainWindow      ???????????????????????????????


class RC(QtWidgets.QMainWindow):
    def __init__(self):
        super(RC, self).__init__()
        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)  # +++

        self.lineEdit_x = QLineEdit(placeholderText="введите: x")
        self.lineEdit_y = QLineEdit(placeholderText="введите: y")
        self.lineEdit_z = QLineEdit(placeholderText="введите: z")

        self.pushButton = QtWidgets.QPushButton("Click me")
        self.pushButton.clicked.connect(self.add_row)

        self.grid = QtWidgets.QGridLayout(centralWidget)
        self.grid.addWidget(self.tableWidget, 0, 0, 1, 3)
        self.grid.addWidget(self.lineEdit_x, 1, 0)
        self.grid.addWidget(self.lineEdit_y, 1, 1)
        self.grid.addWidget(self.lineEdit_z, 1, 2)
        self.grid.addWidget(self.pushButton, 2, 0, 1, 3)

    def add_row(self):
        x = self.lineEdit_x.text()
        y = self.lineEdit_y.text()
        z = self.lineEdit_z.text()

        rowPosition = self.tableWidget.rowCount()  # +++
        self.tableWidget.insertRow(rowPosition)  # +++

        # # Add text to the row  vvvvvvvvvvv
        self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(x))  # rowPosition
        self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(y))
        self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(z))

        self.lineEdit_x.clear()  # +++
        self.lineEdit_y.clear()
        self.lineEdit_z.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    w = RC()
    w.setWindowTitle('Подбор')
    w.show()
    sys.exit(app.exec_())