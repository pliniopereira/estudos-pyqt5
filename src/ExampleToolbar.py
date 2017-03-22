#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program creates a toolbar.
The toolbar has one action, which
terminates the application, if triggered.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QSettings
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('web.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(app.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()

    def startEvent(self):
        self.settings = QSettings(QSettings.IniFormat, QSettings.SystemScope, '__MyBiz', '__settings')
        self.settings.setFallbacksEnabled(False)  # File only, not registry or or.

        # setPath() to try to save to current working directory
        self.settings.setPath(QSettings.IniFormat, QSettings.SystemScope, './__settings.ini')

        # Initial window size/pos last saved
        self.resize(self.settings.value("size", QSize(270, 225)))
        self.move(self.settings.value("pos", QPoint(50, 50)))


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                         "Are you sure to quit?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        self.settings.setValue("size", self.size())
        self.settings.setValue("pos", self.pos())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
