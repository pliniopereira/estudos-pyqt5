#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a tooltip on
a window and a button.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button1', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        btn2 = QPushButton('Button2', self)
        btn2.setToolTip('This is a <b>QPushButton</b> widget')
        btn2.resize(btn.sizeHint())
        btn2.move(150, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

        def disableButton():
            if not text:
                btn.setEnabled(False)
            else:
                btn2.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
