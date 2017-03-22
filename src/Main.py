#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(250, 150)
    window.move(300, 300)
    window.setWindowTitle('Simple')
    window.show()

    sys.exit(app.exec_())
