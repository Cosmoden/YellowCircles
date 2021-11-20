import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Рисование')
        self.pushButton.clicked.connect(self.paint)
        self.flag = False

    def paint(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(227, 227, 113))
        r = randint(10, 200)
        x = randint(100, 200)
        y = randint(100, 200)
        qp.drawEllipse(x, y, r * 2, r * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
