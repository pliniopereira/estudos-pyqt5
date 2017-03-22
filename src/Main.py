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
    try:
        app = QApplication(sys.argv)

        window = QWidget()
        window.resize(500, 500)
        window.setWindowTitle('CCD3')
        window.show()

        sys.exit(app.exec_())

    except Exception as e:
        print(e)
