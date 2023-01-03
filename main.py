import sys
import time
import datetime

from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer,QTime,QDateTime
from PyQt5.QtWidgets import QApplication,QDialog,QWidget,QStackedWidget
from PyQt5.QtGui import QIcon

class ana(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        loadUi(r"C:\Users\bugra\OneDrive\Masaüstü\pythonProject\time.ui",self)
        self.timer = QTimer(self)

        self.timer.timeout.connect(self.current)
        #1 saniye 1000 milisaniye
        self.timer.start(1000)

    def current(self):
        now = datetime.datetime.now()
        zmn = datetime.datetime.strftime(now,"%D\t%X")

        self.label.setText("{}".format(zmn))
app = QApplication(sys.argv)
ana1 = ana()
widget = QStackedWidget()
widget.addWidget(ana1)
widget.setWindowTitle("Current Time")
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()
try:
    print("working ...")
    sys.exit(app.exec_())
except:
    print("exiting ...")