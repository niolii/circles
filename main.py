import random as r
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.print_circle)
        self.pcircle = False

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.pcircle:
            DIO = r.randint(50, 300)
            painter = QtGui.QPainter(self)
            painter.setPen(QPen(Qt.green, 8, Qt.SolidLine))
            painter.drawEllipse(100, 100, DIO, DIO)

    def print_circle(self):
        self.pcircle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())