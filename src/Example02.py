#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we determine the event sender
object.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015

http://stackoverflow.com/questions/17055481/trouble-disabling-buttons-in-pyqt4#17413830
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked1)
        btn2.clicked.connect(self.buttonClicked2)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked1(self):
        sender = self.sender()
        self.btn2.setEnabled(False)
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def buttonClicked2(self):
            sender = self.sender()
            self.statusBar().showMessage(sender.text() + ' was pressed')

    def Traiter1(self):

        self.Qbtn.setEnabled(False)
        self.btn1.setEnabled(False)

        self.Qbtn.setEnabled(True)
        self.btnTraiter.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())