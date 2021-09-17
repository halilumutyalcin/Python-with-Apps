from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "../../Downloads/mathematics-operation-addition-manic-math-multiplication-and-division-flashcard-math-games-mathematics.jpg"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.push_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_5.sizePolicy().hasHeightForWidth())
        self.push_5.setSizePolicy(sizePolicy)
        self.push_5.setStyleSheet("QPushButton{\n"
                                  "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                  "    \n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "border-radius:30px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "background-color: rgb(52, 157, 77);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "color: rgb(185, 185, 185);\n"
                                  "}")
        self.push_5.setObjectName("push_5")
        self.gridLayout.addWidget(self.push_5, 3, 1, 1, 1)
        self.push_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_3.sizePolicy().hasHeightForWidth())
        self.push_3.setSizePolicy(sizePolicy)
        self.push_3.setStyleSheet("QPushButton{\n"
                                  "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                  "    \n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "border-radius:30px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "background-color: rgb(52, 157, 77);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "color: rgb(185, 185, 185);\n"
                                  "}")
        self.push_3.setObjectName("push_3")
        self.gridLayout.addWidget(self.push_3, 2, 2, 1, 1)
        self.push_equal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_equal.sizePolicy().hasHeightForWidth())
        self.push_equal.setSizePolicy(sizePolicy)
        self.push_equal.setStyleSheet("QPushButton{\n"
                                      "font: 75 36pt \"MS Shell Dlg 2\";\n"
                                      "    color: rgb(255, 255, 127);\n"
                                      "border-radius:30px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(230, 230, 0);\n"
                                      "}\n"
                                      "\n"
                                      "QPushBotton{\n"
                                      "color: rgb(232, 77, 0);\n"
                                      "}")
        self.push_equal.setObjectName("push_equal")
        self.gridLayout.addWidget(self.push_equal, 5, 3, 1, 1)
        self.push_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_clear.sizePolicy().hasHeightForWidth())
        self.push_clear.setSizePolicy(sizePolicy)
        self.push_clear.setStyleSheet("QPushButton{\n"
                                      "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                      "    \n"
                                      "    \n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "border-radius:30px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgb(185, 0, 0);\n"
                                      "}\n"
                                      "\n"
                                      "QPushBotton:pressed{\n"
                                      "\n"
                                      "    \n"
                                      "    color: rgb(27, 0, 0);\n"
                                      "}")
        self.push_clear.setShortcut("")
        self.push_clear.setObjectName("push_clear")
        self.gridLayout.addWidget(self.push_clear, 1, 0, 1, 2)
        self.push_min = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_min.sizePolicy().hasHeightForWidth())
        self.push_min.setSizePolicy(sizePolicy)
        self.push_min.setStyleSheet("QPushButton{\n"
                                    "font: 75 36pt \"MS Shell Dlg 2\";\n"
                                    "    color: rgb(255, 255, 127);\n"
                                    "border-radius:30px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "    background-color: rgb(230, 230, 0);\n"
                                    "}\n"
                                    "\n"
                                    "QPushBotton{\n"
                                    "color: rgb(232, 77, 0);\n"
                                    "}")
        self.push_min.setObjectName("push_min")
        self.gridLayout.addWidget(self.push_min, 2, 3, 1, 1)
        self.push_del = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_del.sizePolicy().hasHeightForWidth())
        self.push_del.setSizePolicy(sizePolicy)
        self.push_del.setStyleSheet("QPushButton{\n"
                                    "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                    "    \n"
                                    "    \n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "border-radius:30px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "background-color: rgb(185, 0, 0);\n"
                                    "}\n"
                                    "\n"
                                    "QPushBotton:pressed{\n"
                                    "\n"
                                    "    \n"
                                    "    color: rgb(27, 0, 0);\n"
                                    "}")
        self.push_del.setObjectName("push_del")
        self.gridLayout.addWidget(self.push_del, 1, 2, 1, 1)
        self.push_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_point.sizePolicy().hasHeightForWidth())
        self.push_point.setSizePolicy(sizePolicy)
        self.push_point.setStyleSheet("QPushButton{\n"
                                      "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                      "    \n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "border-radius:30px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgb(52, 157, 77);\n"
                                      "}\n"
                                      "\n"
                                      "QPushBotton{\n"
                                      "color: rgb(185, 185, 185);\n"
                                      "}")
        self.push_point.setObjectName("push_point")
        self.gridLayout.addWidget(self.push_point, 5, 2, 1, 1)
        self.push_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_1.sizePolicy().hasHeightForWidth())
        self.push_1.setSizePolicy(sizePolicy)
        self.push_1.setStyleSheet("QPushButton{\n"
                                  "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                  "    \n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "border-radius:30px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "background-color: rgb(52, 157, 77);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "color: rgb(185, 185, 185);\n"
                                  "}")
        self.push_1.setObjectName("push_1")
        self.gridLayout.addWidget(self.push_1, 2, 0, 1, 1)
        self.push_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_2.sizePolicy().hasHeightForWidth())
        self.push_2.setSizePolicy(sizePolicy)
        self.push_2.setStyleSheet("QPushButton{\n"
                                  "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                  "    \n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "border-radius:30px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "background-color: rgb(52, 157, 77);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton:pressed{\n"
                                  "color: rgb(185, 185, 185);\n"
                                  "}")
        self.push_2.setObjectName("push_2")
        self.gridLayout.addWidget(self.push_2, 2, 1, 1, 1)
        self.push_mult = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_mult.sizePolicy().hasHeightForWidth())
        self.push_mult.setSizePolicy(sizePolicy)
        self.push_mult.setStyleSheet("QPushButton{\n"
                                     "font: 75 36pt \"MS Shell Dlg 2\";\n"
                                     "    color: rgb(255, 255, 127);\n"
                                     "border-radius:30px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(230, 230, 0);\n"
                                     "}\n"
                                     "\n"
                                     "QPushBotton{\n"
                                     "color: rgb(232, 77, 0);\n"
                                     "}")
        self.push_mult.setObjectName("push_mult")
        self.gridLayout.addWidget(self.push_mult, 3, 3, 1, 1)
        self.push_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_9.sizePolicy().hasHeightForWidth())
        self.push_9.setSizePolicy(sizePolicy)
        self.push_9.setStyleSheet("QPushButton{\n"
                                  "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                  "    \n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "border-radius:30px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "background-color: rgb(52, 157, 77);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "color: rgb(185, 185, 185);\n"
                                  "}")
        self.push_9.setObjectName("push_9")
        self.gridLayout.addWidget(self.push_9, 4, 2, 1, 1)
        self.push_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_8.sizePolicy().hasHeightForWidth())
        self.push_8.setSizePolicy(sizePolicy)
        self.push_8.setStyleSheet("QPushButton{\n"
                                  "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                  "    \n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "border-radius:30px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "background-color: rgb(52, 157, 77);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "color: rgb(185, 185, 185);\n"
                                  "}")
        self.push_8.setObjectName("push_8")
        self.gridLayout.addWidget(self.push_8, 4, 1, 1, 1)
        self.push_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_4.sizePolicy().hasHeightForWidth())
        self.push_4.setSizePolicy(sizePolicy)
        self.push_4.setStyleSheet("QPushButton{\n"
                                  "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                  "    \n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "border-radius:30px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "background-color: rgb(52, 157, 77);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "color: rgb(185, 185, 185);\n"
                                  "}")
        self.push_4.setObjectName("push_4")
        self.gridLayout.addWidget(self.push_4, 3, 0, 1, 1)
        self.push_zero = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_zero.sizePolicy().hasHeightForWidth())
        self.push_zero.setSizePolicy(sizePolicy)
        self.push_zero.setStyleSheet("QPushButton{\n"
                                     "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                     "    \n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "border-radius:30px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "background-color: rgb(52, 157, 77);\n"
                                     "}\n"
                                     "\n"
                                     "QPushBotton{\n"
                                     "color: rgb(185, 185, 185);\n"
                                     "}")
        self.push_zero.setObjectName("push_zero")
        self.gridLayout.addWidget(self.push_zero, 5, 0, 1, 2)
        self.push_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_6.sizePolicy().hasHeightForWidth())
        self.push_6.setSizePolicy(sizePolicy)
        self.push_6.setStyleSheet("QPushButton{\n"
                                  "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                  "    \n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "border-radius:30px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "background-color: rgb(52, 157, 77);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "color: rgb(185, 185, 185);\n"
                                  "}")
        self.push_6.setObjectName("push_6")
        self.gridLayout.addWidget(self.push_6, 3, 2, 1, 1)
        self.push_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_div.sizePolicy().hasHeightForWidth())
        self.push_div.setSizePolicy(sizePolicy)
        self.push_div.setStyleSheet("QPushButton{\n"
                                    "font: 75 36pt \"MS Shell Dlg 2\";\n"
                                    "    color: rgb(255, 255, 127);\n"
                                    "border-radius:30px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "    background-color: rgb(230, 230, 0);\n"
                                    "}\n"
                                    "\n"
                                    "QPushBotton{\n"
                                    "color: rgb(232, 77, 0);\n"
                                    "}")
        self.push_div.setObjectName("push_div")
        self.gridLayout.addWidget(self.push_div, 4, 3, 1, 1)
        self.push_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_plus.sizePolicy().hasHeightForWidth())
        self.push_plus.setSizePolicy(sizePolicy)
        self.push_plus.setStyleSheet("QPushButton{\n"
                                     "font: 75 36pt \"MS Shell Dlg 2\";\n"
                                     "    color: rgb(255, 255, 127);\n"
                                     "border-radius:30px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(230, 230, 0);\n"
                                     "}\n"
                                     "\n"
                                     "QPushBotton:pressed{\n"
                                     "color: rgb(232, 77, 0);\n"
                                     "}")
        self.push_plus.setObjectName("push_plus")
        self.gridLayout.addWidget(self.push_plus, 1, 3, 1, 1)
        self.push_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_7.sizePolicy().hasHeightForWidth())
        self.push_7.setSizePolicy(sizePolicy)
        self.push_7.setStyleSheet("QPushButton{\n"
                                  "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                  "    \n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "border-radius:30px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "background-color: rgb(52, 157, 77);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "color: rgb(185, 185, 185);\n"
                                  "}")
        self.push_7.setObjectName("push_7")
        self.gridLayout.addWidget(self.push_7, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 75 36pt \"MS Shell Dlg 2\";\n"
                                 "\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 341, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.push_1.clicked.connect(self.method_1)
        self.push_2.clicked.connect(self.method_2)
        self.push_3.clicked.connect(self.method_3)
        self.push_4.clicked.connect(self.method_4)
        self.push_5.clicked.connect(self.method_5)
        self.push_6.clicked.connect(self.method_6)
        self.push_7.clicked.connect(self.method_7)
        self.push_8.clicked.connect(self.method_8)
        self.push_9.clicked.connect(self.method_9)
        self.push_zero.clicked.connect(self.method_zero)
        self.push_point.clicked.connect(self.method_point)
        self.push_plus.clicked.connect(self.method_plus)
        self.push_min.clicked.connect(self.method_min)
        self.push_mult.clicked.connect(self.method_mult)
        self.push_div.clicked.connect(self.method_div)
        self.push_equal.clicked.connect(self.method_equal)
        self.push_clear.clicked.connect(self.method_clear)
        self.push_del.clicked.connect(self.method_del)

    def method_1(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def method_2(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def method_3(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def method_4(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def method_5(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def method_6(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def method_7(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def method_8(self):
        text = self.label.text()
        self.label.setText(text + "8")

    def method_9(self):
        text = self.label.text()
        self.label.setText(text + "9")

    def method_zero(self):
        text = self.label.text()
        self.label.setText(text + "0")

    def method_point(self):
        text = self.label.text()
        self.label.setText(text + ".")

    def method_plus(self):
        text = self.label.text()
        self.label.setText(text + "+")

    def method_min(self):
        text = self.label.text()
        self.label.setText(text + "-")

    def method_mult(self):
        text = self.label.text()
        self.label.setText(text + "*")

    def method_div(self):
        text = self.label.text()
        self.label.setText(text + "/")

    def method_clear(self):
        self.label.setText("")

    def method_del(self):
        text = self.label.text()
        self.label.setText(text[:len(text) - 1])

    def method_equal(self):
        text = self.label.text()

        try:
            ans = eval(text)
            self.label.setText(str(ans))
        except:
            self.label.setText("Wrong Input")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator - HY"))
        self.push_5.setText(_translate("MainWindow", "5"))
        self.push_5.setShortcut(_translate("MainWindow", "5"))
        self.push_3.setText(_translate("MainWindow", "3"))
        self.push_3.setShortcut(_translate("MainWindow", "3"))
        self.push_equal.setText(_translate("MainWindow", "="))
        self.push_equal.setShortcut(_translate("MainWindow", "="))
        self.push_clear.setText(_translate("MainWindow", "Clear"))
        self.push_min.setText(_translate("MainWindow", "-"))
        self.push_min.setShortcut(_translate("MainWindow", "-"))
        self.push_del.setText(_translate("MainWindow", "Del"))
        self.push_del.setShortcut(_translate("MainWindow", "Backspace"))
        self.push_point.setText(_translate("MainWindow", "."))
        self.push_point.setShortcut(_translate("MainWindow", "."))
        self.push_1.setText(_translate("MainWindow", "1"))
        self.push_1.setShortcut(_translate("MainWindow", "1"))
        self.push_2.setText(_translate("MainWindow", "2"))
        self.push_2.setShortcut(_translate("MainWindow", "2"))
        self.push_mult.setText(_translate("MainWindow", "x"))
        self.push_mult.setShortcut(_translate("MainWindow", "*"))
        self.push_9.setText(_translate("MainWindow", "9"))
        self.push_9.setShortcut(_translate("MainWindow", "9"))
        self.push_8.setText(_translate("MainWindow", "8"))
        self.push_8.setShortcut(_translate("MainWindow", "8"))
        self.push_4.setText(_translate("MainWindow", "4"))
        self.push_4.setShortcut(_translate("MainWindow", "4"))
        self.push_zero.setText(_translate("MainWindow", "0"))
        self.push_zero.setShortcut(_translate("MainWindow", "0"))
        self.push_6.setText(_translate("MainWindow", "6"))
        self.push_6.setShortcut(_translate("MainWindow", "6"))
        self.push_div.setText(_translate("MainWindow", "÷"))
        self.push_div.setShortcut(_translate("MainWindow", "/"))
        self.push_plus.setText(_translate("MainWindow", "+"))
        self.push_plus.setShortcut(_translate("MainWindow", "+"))
        self.push_7.setText(_translate("MainWindow", "7"))
        self.push_7.setShortcut(_translate("MainWindow", "7"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
