# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tempUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(485, 207)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lcd1 = QtGui.QLCDNumber(self.centralwidget)
        self.lcd1.setGeometry(QtCore.QRect(120, 60, 91, 71))
        self.lcd1.setFrameShape(QtGui.QFrame.Box)
        self.lcd1.setFrameShadow(QtGui.QFrame.Plain)
        self.lcd1.setObjectName(_fromUtf8("lcd1"))
        self.lcd2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcd2.setGeometry(QtCore.QRect(300, 60, 91, 71))
        self.lcd2.setFrameShape(QtGui.QFrame.Box)
        self.lcd2.setFrameShadow(QtGui.QFrame.Plain)
        self.lcd2.setObjectName(_fromUtf8("lcd2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(117, 20, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 91, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Temperature", None))
        self.label_2.setText(_translate("MainWindow", "Humidity", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

