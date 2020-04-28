# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 673)
        MainWindow.setStyleSheet("#MainWindow\n"
"{\n"
"    background:black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    border:none;\n"
"    background-color:rgb(46, 52, 54);\n"
"    color:white;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color:black;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}")
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setDefault(False)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 11, 0, 1, 1)
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_dot.sizePolicy().hasHeightForWidth())
        self.pushButton_dot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setAutoFillBackground(False)
        self.pushButton_dot.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    border: none;\n"
"    background-color:rgb(46, 52, 54);\n"
"    color:white;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color:black;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}")
        self.pushButton_dot.setAutoDefault(False)
        self.pushButton_dot.setDefault(False)
        self.pushButton_dot.setFlat(False)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.gridLayout.addWidget(self.pushButton_dot, 14, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    border:none;\n"
"    background-color:rgb(46, 52, 54);\n"
"    color:white;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color:black;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}")
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 12, 2, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setAutoFillBackground(False)
        self.pushButton_0.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    border: none;\n"
"    background-color:rgb(46, 52, 54);\n"
"    color:white;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color:black;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}")
        self.pushButton_0.setAutoDefault(False)
        self.pushButton_0.setDefault(False)
        self.pushButton_0.setFlat(False)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 14, 0, 1, 2)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setAutoFillBackground(False)
        self.pushButton_1.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    border: none;\n"
"    background-color:rgb(46, 52, 54);\n"
"    color:white;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color:black;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}")
        self.pushButton_1.setAutoDefault(False)
        self.pushButton_1.setDefault(False)
        self.pushButton_1.setFlat(False)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 13, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    border: none;\n"
"    background-color:rgb(46, 52, 54);\n"
"    color:white;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color:black;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 13, 0, 1, 1)
        self.pushButton_clr = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clr.sizePolicy().hasHeightForWidth())
        self.pushButton_clr.setSizePolicy(sizePolicy)
        self.pushButton_clr.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_clr.setObjectName("pushButton_clr")
        self.gridLayout.addWidget(self.pushButton_clr, 6, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    border: none;\n"
"    background-color:rgb(46, 52, 54);\n"
"    color:white;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color:black;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}")
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 12, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    border: none;\n"
"    background-color:rgb(46, 52, 54);\n"
"    color:white;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color:black;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}")
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 11, 1, 1, 1)
        self.pushButton_eql = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_eql.sizePolicy().hasHeightForWidth())
        self.pushButton_eql.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_eql.setFont(font)
        self.pushButton_eql.setAutoFillBackground(False)
        self.pushButton_eql.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_eql.setAutoDefault(False)
        self.pushButton_eql.setDefault(False)
        self.pushButton_eql.setFlat(False)
        self.pushButton_eql.setObjectName("pushButton_eql")
        self.gridLayout.addWidget(self.pushButton_eql, 14, 3, 1, 1)
        self.pushButton_sub = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sub.sizePolicy().hasHeightForWidth())
        self.pushButton_sub.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setAutoFillBackground(False)
        self.pushButton_sub.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_sub.setAutoDefault(False)
        self.pushButton_sub.setDefault(False)
        self.pushButton_sub.setFlat(False)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout.addWidget(self.pushButton_sub, 11, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    border:none;\n"
"    background-color:rgb(46, 52, 54);\n"
"    color:white;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color:black;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}")
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 11, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    border: none;\n"
"    background-color:rgb(46, 52, 54);\n"
"    color:white;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color:black;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 13, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    border: none;\n"
"    background-color:rgb(46, 52, 54);\n"
"    color:white;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(136, 138, 133);\n"
"    color:black;\n"
"    font: 16pt \"DejaVu Sans Mono\";\n"
"}")
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 12, 1, 1, 1)
        self.pushButton_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_mul.sizePolicy().hasHeightForWidth())
        self.pushButton_mul.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setAutoFillBackground(False)
        self.pushButton_mul.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_mul.setAutoDefault(False)
        self.pushButton_mul.setDefault(False)
        self.pushButton_mul.setFlat(False)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout.addWidget(self.pushButton_mul, 13, 3, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_div.sizePolicy().hasHeightForWidth())
        self.pushButton_div.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setAutoFillBackground(False)
        self.pushButton_div.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_div.setAutoDefault(False)
        self.pushButton_div.setDefault(False)
        self.pushButton_div.setFlat(False)
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout.addWidget(self.pushButton_div, 12, 3, 1, 1)
        self.pushButton_per = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_per.sizePolicy().hasHeightForWidth())
        self.pushButton_per.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_per.setFont(font)
        self.pushButton_per.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_per.setObjectName("pushButton_per")
        self.gridLayout.addWidget(self.pushButton_per, 6, 1, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setAutoFillBackground(False)
        self.pushButton_add.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_add.setAutoDefault(False)
        self.pushButton_add.setDefault(False)
        self.pushButton_add.setFlat(False)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 6, 2, 1, 1)
        self.pushButton_ac = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ac.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ac.sizePolicy().hasHeightForWidth())
        self.pushButton_ac.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_ac.setFont(font)
        self.pushButton_ac.setAutoFillBackground(False)
        self.pushButton_ac.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:rgb(209, 44, 44);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 16pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(214, 81, 81);\n"
"    color:black;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_ac.setAutoDefault(False)
        self.pushButton_ac.setDefault(False)
        self.pushButton_ac.setFlat(False)
        self.pushButton_ac.setObjectName("pushButton_ac")
        self.gridLayout.addWidget(self.pushButton_ac, 6, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(500, 120))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color:rgb(238, 238, 236);\n"
"\n"
"font: 40pt \"SF Compact Text\";\n"
"")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 19))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(8)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setVisible(True)
        self.actionReset.setObjectName("actionReset")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_clr.pressed.connect(self.label.clear)
        self.pushButton_ac.pressed.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_clr.setText(_translate("MainWindow", "CLEAR"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_eql.setText(_translate("MainWindow", "="))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_mul.setText(_translate("MainWindow", "x"))
        self.pushButton_div.setText(_translate("MainWindow", "/"))
        self.pushButton_per.setText(_translate("MainWindow", "%"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_ac.setText(_translate("MainWindow", "AC"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

