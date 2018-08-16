#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arm_controller.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

# --------------
import rospy
# --------------

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
        MainWindow.resize(671, 566)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.j1_slider = QtGui.QSlider(self.centralwidget)
        self.j1_slider.setGeometry(QtCore.QRect(80, 330, 29, 160))
        self.j1_slider.setMaximum(300)
        self.j1_slider.setSingleStep(1)
        self.j1_slider.setProperty("value", 150)
        self.j1_slider.setOrientation(QtCore.Qt.Vertical)
        self.j1_slider.setObjectName(_fromUtf8("j1_slider"))
        self.j2_slider = QtGui.QSlider(self.centralwidget)
        self.j2_slider.setGeometry(QtCore.QRect(210, 270, 29, 160))
        self.j2_slider.setMaximum(300)
        self.j2_slider.setSingleStep(1)
        self.j2_slider.setProperty("value", 150)
        self.j2_slider.setOrientation(QtCore.Qt.Vertical)
        self.j2_slider.setObjectName(_fromUtf8("j2_slider"))
        self.j3_slider = QtGui.QSlider(self.centralwidget)
        self.j3_slider.setGeometry(QtCore.QRect(340, 190, 29, 160))
        self.j3_slider.setMaximum(300)
        self.j3_slider.setSingleStep(1)
        self.j3_slider.setProperty("value", 150)
        self.j3_slider.setOrientation(QtCore.Qt.Vertical)
        self.j3_slider.setObjectName(_fromUtf8("j3_slider"))
        self.j4_slider = QtGui.QSlider(self.centralwidget)
        self.j4_slider.setGeometry(QtCore.QRect(460, 110, 29, 160))
        self.j4_slider.setMaximum(300)
        self.j4_slider.setSingleStep(1)
        self.j4_slider.setProperty("value", 150)
        self.j4_slider.setOrientation(QtCore.Qt.Vertical)
        self.j4_slider.setObjectName(_fromUtf8("j4_slider"))
        self.j5_slider = QtGui.QSlider(self.centralwidget)
        self.j5_slider.setGeometry(QtCore.QRect(400, 470, 160, 29))
        self.j5_slider.setSingleStep(1)
        self.j5_slider.setProperty("value", 50)
        self.j5_slider.setOrientation(QtCore.Qt.Horizontal)
        self.j5_slider.setObjectName(_fromUtf8("j5_slider"))
        self.j1_label = QtGui.QLabel(self.centralwidget)
        self.j1_label.setGeometry(QtCore.QRect(10, 490, 181, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.j1_label.setFont(font)
        self.j1_label.setObjectName(_fromUtf8("j1_label"))
        self.j5_label = QtGui.QLabel(self.centralwidget)
        self.j5_label.setGeometry(QtCore.QRect(430, 440, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.j5_label.setFont(font)
        self.j5_label.setObjectName(_fromUtf8("j5_label"))
        self.j1_value = QtGui.QLabel(self.centralwidget)
        self.j1_value.setGeometry(QtCore.QRect(70, 300, 68, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.j1_value.setFont(font)
        self.j1_value.setObjectName(_fromUtf8("j1_value"))
        self.j2_value = QtGui.QLabel(self.centralwidget)
        self.j2_value.setGeometry(QtCore.QRect(210, 240, 68, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.j2_value.setFont(font)
        self.j2_value.setObjectName(_fromUtf8("j2_value"))
        self.j4_value = QtGui.QLabel(self.centralwidget)
        self.j4_value.setGeometry(QtCore.QRect(460, 90, 68, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.j4_value.setFont(font)
        self.j4_value.setObjectName(_fromUtf8("j4_value"))
        self.j3_value = QtGui.QLabel(self.centralwidget)
        self.j3_value.setGeometry(QtCore.QRect(340, 170, 68, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.j3_value.setFont(font)
        self.j3_value.setObjectName(_fromUtf8("j3_value"))
        self.j2_label = QtGui.QLabel(self.centralwidget)
        self.j2_label.setGeometry(QtCore.QRect(150, 430, 181, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.j2_label.setFont(font)
        self.j2_label.setObjectName(_fromUtf8("j2_label"))
        self.j3_label = QtGui.QLabel(self.centralwidget)
        self.j3_label.setGeometry(QtCore.QRect(280, 350, 151, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.j3_label.setFont(font)
        self.j3_label.setObjectName(_fromUtf8("j3_label"))
        self.j4_label = QtGui.QLabel(self.centralwidget)
        self.j4_label.setGeometry(QtCore.QRect(410, 270, 141, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.j4_label.setFont(font)
        self.j4_label.setObjectName(_fromUtf8("j4_label"))
        self.j5_value = QtGui.QLabel(self.centralwidget)
        self.j5_value.setGeometry(QtCore.QRect(570, 470, 68, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setPointSize(14)
        font.setItalic(True)
        self.j5_value.setFont(font)
        self.j5_value.setObjectName(_fromUtf8("j5_value"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # -------------------------------------------------------------------------------------
        self.joint_list = ['shoulder_pan_joint','shoulder_lift_joint','elbow_flex_joint','wrist_flex_joint','gripper_joint']
        
        
        self.connectJointValue()
    
    def connectJointValue(self):        
        self.j1_slider.valueChanged.connect(self.shoulder_panCB)
        self.j2_slider.valueChanged.connect(self.shoulder_liftCB)
        self.j3_slider.valueChanged.connect(self.elbow_flexCB)
        self.j4_slider.valueChanged.connect(self.wrist_flexCB)
        self.j5_slider.valueChanged.connect(self.gripperCB)

        self.setJV()
        
    def setJV(self):
        self.j1_value.setText(str(self.j1_slider.value())+"\'")
        self.j2_value.setText(str(self.j2_slider.value())+"\'")
        self.j3_value.setText(str(self.j3_slider.value())+"\'")
        self.j4_value.setText(str(self.j4_slider.value())+"\'")
        #self.j5_value.setText(str(self.j5_slider.value())+"\'")
        cm = self.change_cm( self.j5_slider.value() )
        self.j5_value.setText( str("%.1f cm"%cm) )

        val_1 = int(self.j1_slider.value())
        val_2 = int(self.j2_slider.value())
        val_3 = int(self.j3_slider.value())
        val_4 = int(self.j4_slider.value())
        val_5 = int(self.j5_slider.value())

        values =[val_1,val_2,val_3,val_4,val_5]
        for i in range(0,5):
            param = self.joint_list[i]+"/degree"
            rospy.set_param(param, values[i]) 

    def change_cm(self,x):
        y = (0.055*x)+ 0.083
        return y
    def shoulder_panCB(self):
        self.setJV()
    def shoulder_liftCB(self):
        self.setJV()
    def elbow_flexCB(self):
        self.setJV()
    def wrist_flexCB(self):
        self.setJV()
    def gripperCB(self):
        self.setJV()
    # -------------------------------------------------------------------------------------

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.j1_label.setText(_translate("MainWindow", "shoulder_pan_joint", None))
        self.j5_label.setText(_translate("MainWindow", "gripper_joint", None))
        self.j1_value.setText(_translate("MainWindow", "150\'", None))
        self.j2_value.setText(_translate("MainWindow", "150\'", None))
        self.j4_value.setText(_translate("MainWindow", "150\'", None))
        self.j3_value.setText(_translate("MainWindow", "150\'", None))
        self.j2_label.setText(_translate("MainWindow", "shoulder_lift_joint", None))
        self.j3_label.setText(_translate("MainWindow", "elbow_flex_joint", None))
        self.j4_label.setText(_translate("MainWindow", "wrist_flex_joint", None))
        self.j5_value.setText(_translate("MainWindow", "50\'", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

