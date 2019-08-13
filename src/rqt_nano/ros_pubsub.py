#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Version PYQT5

import os
import rospy
import rospkg
import math

from PyQt5 import QtCore
from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget,QApplication
from python_qt_binding.QtCore import *
from python_qt_binding.QtGui import *
from std_msgs.msg import Int16,Int16MultiArray,Int16,String,UInt8MultiArray,Float64MultiArray
from sensor_msgs.msg import LaserScan,Imu
import tf
import numpy as np
import cv2 as cv

class ROSdata(QWidget):

    updata_pic = QtCore.pyqtSignal()

    def __init__(self,context):
        super(ROSdata, self).__init__()
        ui_file = os.path.join(rospkg.RosPack().get_path('rqt_nano'), 'resource', 'MyPlugin.ui')
        loadUi(ui_file, self)
        self.cnt=0
        self.warn=0
        self.point=0
        self.timer = QTimer(self)
        self.timer2 = QTimer(self)
        self.timer3 = QTimer(self)
        self.timer.timeout.connect(self.timeslot)
        self.timer2.timeout.connect(self.timeslot2)
        self.timer3.timeout.connect(self.timeslot3)


        self.subscriber_group()
        #self.publisher_group()

        #self.pushButton.clicked.connect(self.startCount)

        #self.pushButton_2.clicked.connect(self.stopCount)
        self.updata_pic.connect(self.slotpic)

    #def publisher_group(self):


    def subscriber_group(self):
        rospy.Subscriber("/alarm",Int16, self.callback)
        #self.timer.start(1000)



    def timeslot(self):
        self.label.setPixmap(QPixmap("/home/denny3/new_work/src/rqt_nano/LOGOtest4.png"))
        self.cnt=self.cnt+1
        self.lcdNumber.display(self.cnt)
        self.timer.stop()

    def timeslot2(self):
        self.label.setPixmap(QPixmap("/home/denny3/new_work/src/rqt_nano/LOGOtest1.png"))
        self.timer2.stop()
    def timeslot3(self):
        if self.point ==1:
            self.label.setPixmap(QPixmap("/home/denny3/new_work/src/rqt_nano/LOGOtest5.png"))
            self.timer3.stop()
        elif self.point ==0:
            self.label.setPixmap(QPixmap("/home/denny3/new_work/src/rqt_nano/LOGOtest1.png"))
            self.timer3.stop()

        print("point:" + str(self.point))

    def callback(self,alarm):

        self.warn = alarm.data
        print("alarm:" + str(alarm.data))
        if alarm.data ==1:

            pass

            #self.label.setPixmap(QPixmap("/home/denny3/new_work/src/rqt_nano/LOGOtest5.png"))

         #self.label.setPixmap(QPixmap("/home/denny3/new_work/src/rqt_nano/LOGOtest4.png"))
        else :
            #self.label.setPixmap(QPixmap("/home/denny3/new_work/src/rqt_nano/LOGOtest1.png"))
            pass
        self.updata_pic.emit()
    def slotpic(self):
        if self.warn == 1:
            self.gif = QMovie('/home/denny3/new_work/src/rqt_nano/LOGO_gif_final.gif')
            self.gif.setSpeed(300)
            self.gif.setScaledSize(QSize(431,390))
            self.label.setMovie(self.gif)
            self.gif.start()
            #self.point=1
            #self.timer3.start(100)

            #self.timer3.start(1)
        else:
            pass
            #self.point=0
            self.timer3.start(900)

