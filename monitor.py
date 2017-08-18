#!/usr/bin/env python3

from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import tempUI

import serial
import time
import json

from sudo_exec import sudo_exec

s = None
class Window(QtGui.QMainWindow,tempUI.Ui_MainWindow ):
    def __init__(self,parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)

        self.thrClass = ThrClass()
        self.thrClass.start()
        #self.connect(self.thrClass, QtCore.SIGNAL('CPU'), self.updateProgressBar)
        self.connect(self.thrClass, QtCore.SIGNAL('TMP'), self.updateTMP)
        self.connect(self.thrClass, QtCore.SIGNAL('HUM'), self.updateHUM)

    def updateTMP(self,val):
        self.lcd1.display(val)
    def updateHUM(self,val):
        self.lcd2.display(val)


class ThrClass(QtCore.QThread):
    global s
    try:
        #Change to the appropirate Serial port
        s= serial.Serial("/dev/ttyACM0", 115200)
    except serial.serialutil.SerialException as e:

        if e.errno == 13:
            #The second part of parameter is the password of the system
            #It need to give admin password in order to communicate with serial 
            sudo_exec('sudo chmod 666 /dev/ttyACM0', 'WinLoYa28')



    def __init__(self, parent=None):
        super(ThrClass,self).__init__(parent)
        global s
        s = serial.Serial("/dev/ttyACM0", 115200)



    def run(self):
        last = 0
        lasthum = 0
        while True:
            time.sleep(2)
            s.write(b"/temperature'\r'\n")
            anb = s.readline()
            # print (anb)
            # print (type(anb))
            try:
                anb = str(anb, 'utf-8')
            # print (type(anb))
                print(anb)

                two = json.loads(anb)
                ans = two['temperature']
                print(ans)
                self.emit(QtCore.SIGNAL('TMP'), ans)
                last = ans
            except ValueError:
                print("Error")
                print(last)
                self.emit(QtCore.SIGNAL('TMP'), last)
            time.sleep(2)
            s.write(b"/humidity'\r'\n")
            # s.write(b"/humidity'\r'\n")
            try :
                anb1 = s.readline()
                anc = str(anb1, 'utf-8')
                two1 = json.loads(anc)
                ppp = two1['humidity']
                print(ppp)
                lasthum = ppp
                self.emit(QtCore.SIGNAL('HUM'), ppp)

            except ValueError:
                print ("Hum Error")
                print (lasthum)
                self.emit(QtCore.SIGNAL('HUM'), lasthum)

app = QtGui.QApplication(sys.argv)
gui = Window()
gui.show()
sys.exit(app.exec())
