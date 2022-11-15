import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QFileDialog
from PyQt5.QtCore import QSize, Qt, QModelIndex

import design
import os
import pandas as pd
import numpy as np
import lasio
import table_model as tm


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btnSave.clicked.connect(self.save_click)
        self.btnSelectFile.clicked.connect(self.fill_table)
        self.btnAddRow.clicked.connect(self.add_row)
        self.btnAddColumn.clicked.connect(self.add_column)
        self.directory = ""
        self.selected_file = ""
        self.df = None

        self.las = lasio.read("example.las").df()


    def fill_table(self):
        central_widget = self.tableWidget  # Create a central widget
        las = lasio.read("example.las")
        # las = lasio.read("E:\\Work\\QGISProject\\Homework4\example.las")
        df = las.df()

        grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(grid_layout)  # Set this layout in central widget

        table = self.tableWidget  # Create a table
        table.setColumnCount(5)  # Set columns
        table.setRowCount(234)  # and rows
        table.setHorizontalHeaderLabels(["Depth", "Delta-T", "Resist.", "SP", "GR"])

        # Set the table headers
        table.setHorizontalHeaderLabels(["Depth", "Delta-T", "Resist.", "SP", "GR"])

        # Set the tooltips to headings
        table.horizontalHeaderItem(0).setToolTip("Depth")
        table.horizontalHeaderItem(1).setToolTip("Delta-T")
        table.horizontalHeaderItem(2).setToolTip("Resist.")
        table.horizontalHeaderItem(3).setToolTip("SP")
        table.horizontalHeaderItem(4).setToolTip("GR")

        # Fill the first line
        for i in range(table.rowCount()-1):
            table.setItem(i, 0, QTableWidgetItem(str(df.index[i])))
            table.setRowCount(table.rowCount())
            for j in range(table.columnCount()-1):
                table.setItem(i, j+1, QTableWidgetItem(str(df.values[i][j])))

        # Do the resize of the columns by content
        table.resizeColumnsToContents()

        grid_layout.addWidget(table, 0, 0)  # Adding the table to the grid

    def save_click(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save LASio file", "", "Lasio Files (*.las)")
        if fileName:
            print(fileName)
            f = open(fileName,'w')
            table = self.tableWidget
            for i in range (table.rowCount()):
                row = ''
                for j in range (table.columnCount()):
                    #QTableWidgetItem.text()
                    if table.item(i,j) is not None:
                        row = row + str(table.item(i,j).text())+ '   '
                string_for_save = str(row)+'\n'
                f.write(string_for_save)
            f.close()

    def add_row(self):
        if self.las is not None:
            table = self.tableWidget
            model = tm.LasTableModel("E:\\Work\\QGISProject\\Homework4\example.las")
            model.insertRows(table.rowCount(),1)
            self.save_click()

    def add_column(self):
        if self.las is not None:
            table = self.tableWidget
            model = tm.LasTableModel("E:\\Work\\QGISProject\\Homework4\example.las")
            model.insertColumns(table.columnCount(),1)
            self.save_click()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
