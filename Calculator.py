from PyQt5.QtGui import *
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import *

from PyQt5 import QtWidgets
from calculator import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    firstNum = None
    SecondNumType = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_0.clicked.connect(self.button_pressed)
        self.pushButton_1.clicked.connect(self.button_pressed)
        self.pushButton_2.clicked.connect(self.button_pressed)
        self.pushButton_3.clicked.connect(self.button_pressed)
        self.pushButton_4.clicked.connect(self.button_pressed)
        self.pushButton_5.clicked.connect(self.button_pressed)
        self.pushButton_6.clicked.connect(self.button_pressed)
        self.pushButton_7.clicked.connect(self.button_pressed)
        self.pushButton_8.clicked.connect(self.button_pressed)
        self.pushButton_9.clicked.connect(self.button_pressed)

        self.pushButton_add.clicked.connect(self.binary_button_pressed)
        self.pushButton_sub.clicked.connect(self.binary_button_pressed)
        self.pushButton_div.clicked.connect(self.binary_button_pressed)
        self.pushButton_mul.clicked.connect(self.binary_button_pressed)

        self.pushButton_dot.clicked.connect(self.decimal_pressed)

        # self.pushButton_clear.clicked.connect(self.clear_button_pressed)

        self.pushButton_eql.clicked.connect(self.equal_pressed)

        # self.pushButton_backspace.clicked.connect(self.backspace_pressed)

        self.pushButton_add.setCheckable(True)
        self.pushButton_sub.setCheckable(True)
        self.pushButton_mul.setCheckable(True)
        self.pushButton_div.setCheckable(True)


    def button_pressed(self):
        button = self.sender()
        if ((self.pushButton_add.isChecked() or self.pushButton_sub.isChecked() or
                self.pushButton_mul.isChecked() or self.pushButton_div.isChecked())
                and (not self.SecondNumType)):
            newLabel = format(float(button.text()), '.20g')
            self.SecondNumType = True
        else:
            if (('.' in self.label.text()) and (button.text == '0')):
                newLabel = format(float(self.label.text() + button.text()), '.20')
            else:
                newLabel = format(float(self.label.text() + button.text()), '.20g')
        self.label.setText(newLabel)

    def binary_button_pressed(self):
        button = self.sender()
        self.firstNum = float(self.label.text())

        button.setChecked(True)

    def decimal_pressed(self):
        if ('.' in self.label.text()):
            newLabel = self.label.setText(self.label.text())
        else:
            newLabel = self.label.setText(self.label.text() + '.')


    def clear_button_pressed(self):
        self.pushButton_add.setChecked(False)
        self.pushButton_sub.setChecked(False)
        self.pushButton_div.setChecked(False)
        self.pushButton_mul.setChecked(False)

        self.SecondNumType = False
        self.label.setText('0')

    def equal_pressed(self):
        secondNum = float(self.label.text())
        if self.pushButton_add.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber, '.20g')
            self.label.setText(newLabel)
            self.pushButton_add.setChecked(False)

        elif self.pushButton_sub.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber, '.20g')
            self.label.setText(newLabel)
            self.pushButton_sub.setChecked(False)

        elif self.pushButton_div.isChecked():
            labelNumber = self.firstNum / secondNum
            newLabel = format(labelNumber, '.20g')
            self.label.setText(newLabel)
            self.pushButton_div.setChecked(False)

        elif self.pushButton_mul.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber, '.20g')
            self.label.setText(newLabel)
            self.pushButton_mul.setChecked(False)

            self.SecondNumType = False

    # def backspace_pressed(self):
    #     newLabel = self.label.text()[:-1]
    #     self.label.setText(newLabel)
if __name__=='__main__':
    app=QApplication([])
    app.setApplicationName('Calculator')
    window=MainWindow()
    window.show()
    app.exec()