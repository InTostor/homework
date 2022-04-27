import sys
import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtGui
import PyQt5.QtCore
import random


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt paint - pythonspot.com"
        self.left = 300
        self.top = 300
        self.width = 512
        self.height = 512
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0, 0)
        self.m.resize(self.width, self.height)

        self.show()


class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)

        qp.setPen(Qt.black)
        size = self.size()

        for x in range(255):
            for y in range(255):
                qp.setPen(QColor(x, y, 100))
                mainWindow = QtGui.QWidget()
                width = mainWindow.frameGeometry().width()
                height = mainWindow.frameGeometry().height()
                qx, qy = x / 255, y / 255

                qp.drawPoint(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
