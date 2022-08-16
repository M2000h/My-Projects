from PyQt5 import QtWidgets, QtGui, QtCore
from nn import NeuralNetwork
import random
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def dsigmoid(y):
    return y * (1 - y)


nn = NeuralNetwork(0.01, sigmoid, dsigmoid, [2, 5, 5, 5, 2])


def fit(green_points, blue_points, window):
    i = 0
    for k in range(10000):
        r = random.randint(0, len(green_points) + len(blue_points) - 1)
        targets = [0, 0]  # TODO: возможен косяк
        if r < len(green_points):
            p = green_points[r]
            targets[0] = 1
        else:
            p = blue_points[r - len(green_points) - 1]
            targets[1] = 1

        nx = p[0] - 0.5
        ny = p[1] - 0.5
        if i == 0:
            i+=1
        nn.feedForward([nx, ny])
        nn.backpropagation(targets)


class ImageScroller(QtWidgets.QWidget):
    def __init__(self):
        self.green_points = []
        self.blue_points = []
        QtWidgets.QWidget.__init__(self)

    def paintEvent(self, paint_event):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen()
        pen.setWidth(10)

        gradient = QtGui.QLinearGradient(0, 0, 0, 400)
        for i in range(int(self.size().width() / 8)):
            for j in range(int(self.size().height() / 8)):
                nx = i / self.size().width() * 8 - 0.5
                ny = j / self.size().height() * 8 - 0.5
                outputs = nn.feedForward([nx, ny])
                green = max(0, min(1, outputs[0] - outputs[1] + 0.5))
                blue = 1 - green

                if green>blue:
                    pen.setColor(QtCore.Qt.GlobalColor.green)
                else:
                    pen.setColor(QtCore.Qt.GlobalColor.blue)
                color = QtGui.QColor(0, int(green*255), int(blue*255), 40)
                pen.setColor(color)
                painter.setPen(pen)
                painter.drawEllipse(i * 8, j * 8, 10, 10)

        pen.setColor(QtCore.Qt.GlobalColor.white)
        painter.setPen(pen)
        for pos in self.green_points + self.blue_points:
            painter.drawEllipse(int(pos[0] * self.size().width())-2, int(pos[1] * self.size().height())-2, 8, 8)

        pen.setColor(QtCore.Qt.GlobalColor.green)
        painter.setPen(pen)
        for pos in self.green_points:
            painter.drawEllipse(int(pos[0] * self.size().width()), int(pos[1] * self.size().height()), 4, 4)

        pen.setColor(QtCore.Qt.GlobalColor.blue)
        painter.setPen(pen)
        for pos in self.blue_points:
            painter.drawEllipse(int(pos[0] * self.size().width()), int(pos[1] * self.size().height()), 5, 5)

    def mouseReleaseEvent(self, cursor_event):
        x = cursor_event.x() / self.size().width()
        y = cursor_event.y() / self.size().height()
        if cursor_event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.blue_points.append((x, y))
        else:
            self.green_points.append((x, y))
        fit(self.green_points, self.blue_points, self)
        self.update()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = ImageScroller()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())
