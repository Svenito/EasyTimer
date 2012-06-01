# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer.ui'
#
# Created: Fri Jun  1 10:11:11 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Timer(object):
    def setupUi(self, Timer):
        Timer.setObjectName("Timer")
        Timer.resize(339, 129)
        self.gridLayout_2 = QtGui.QGridLayout(Timer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.TimerLabel = QtGui.QLabel(Timer)
        self.TimerLabel.setObjectName("TimerLabel")
        self.gridLayout.addWidget(self.TimerLabel, 0, 0, 1, 1)
        self.HourSpin = QtGui.QSpinBox(Timer)
        self.HourSpin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.HourSpin.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.HourSpin.setMaximum(24)
        self.HourSpin.setObjectName("HourSpin")
        self.gridLayout.addWidget(self.HourSpin, 0, 1, 1, 1)
        self.MinuteSpin = QtGui.QSpinBox(Timer)
        self.MinuteSpin.setMaximum(59)
        self.MinuteSpin.setObjectName("MinuteSpin")
        self.gridLayout.addWidget(self.MinuteSpin, 0, 2, 1, 1)
        self.SecondSpin = QtGui.QSpinBox(Timer)
        self.SecondSpin.setMaximum(59)
        self.SecondSpin.setObjectName("SecondSpin")
        self.gridLayout.addWidget(self.SecondSpin, 0, 3, 1, 1)
        self.PopupLabel = QtGui.QLabel(Timer)
        self.PopupLabel.setObjectName("PopupLabel")
        self.gridLayout.addWidget(self.PopupLabel, 1, 0, 1, 1)
        self.PopupEdit = QtGui.QLineEdit(Timer)
        self.PopupEdit.setObjectName("PopupEdit")
        self.gridLayout.addWidget(self.PopupEdit, 1, 1, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Timer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.TimerLabel.setBuddy(self.HourSpin)
        self.PopupLabel.setBuddy(self.PopupEdit)

        self.retranslateUi(Timer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Timer.hide)
        QtCore.QMetaObject.connectSlotsByName(Timer)

    def retranslateUi(self, Timer):
        Timer.setWindowTitle(QtGui.QApplication.translate("Timer", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.TimerLabel.setText(QtGui.QApplication.translate("Timer", "Timer interval H:M:S", None, QtGui.QApplication.UnicodeUTF8))
        self.PopupLabel.setText(QtGui.QApplication.translate("Timer", "Popup Text", None, QtGui.QApplication.UnicodeUTF8))

