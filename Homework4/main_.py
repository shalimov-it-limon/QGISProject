from PyQt5.QtWidgets import QApplication, QTableView
from table_model import LasTableModel


def las_table():
    model = LasTableModel('table_model_view/example.las')
    model.insertRows(5, 4)
    table = QTableView()
    table.setModel(model)
    table.resize(600, 600)
    return table


if __name__ == '__main__':
    app = QApplication([])
    widget = las_table()
    widget.show()
    app.exec()