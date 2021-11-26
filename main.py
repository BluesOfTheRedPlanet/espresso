import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()

        result = cur.execute(
            """SELECT ID, sort, roasted, grinding, description, price, size FROM aboutCoffee""").fetchall()
        print(result)
        for i, row in enumerate(result):
            this_id = row[0]
            sort = row[1]
            roasted = row[2]
            grinding = row[3]
            description = row[4]
            price = row[5]
            size = row[6]

            pos = self.tableWidget.rowCount()
            self.tableWidget.insertRow(pos)

            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(this_id)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(sort))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(roasted))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(grinding))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(description))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(size)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
