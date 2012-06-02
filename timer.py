#!/usr/bin/env python2.6
import sys
from PyQt4 import QtGui, QtCore
from ui.timerUI import Ui_Timer

class SetupUI(QtGui.QDialog):
	def __init__(self, parent):
		QtGui.QDialog.__init__(self, None)
		self.ui = Ui_Timer()
		self.ui.setupUi(self)
		self.parent = parent

		self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.setValues)

	def setValues(self):
		hours = self.ui.HourSpin.value()
		minutes = self.ui.MinuteSpin.value()
		seconds = self.ui.SecondSpin.value()

		total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds

		msg = self.ui.PopupEdit.text()
		self.parent.setValues(total_seconds, msg)
		self.hide()

class SystemTrayIcon(QtGui.QSystemTrayIcon):

	def __init__(self, icon, parent=None):
		QtGui.QSystemTrayIcon.__init__(self, icon, parent)
		self.parent = parent
		menu = QtGui.QMenu(parent)

		
		startAction = menu.addAction("Start")
		self.connect(startAction, QtCore.SIGNAL("triggered()"), self.startTimer)
		self.setContextMenu(menu)
		
		startAction = menu.addAction("Stop")
		self.connect(startAction, QtCore.SIGNAL("triggered()"), self.stopTimer)
		self.setContextMenu(menu)
		
		startAction = menu.addAction("Setup")
		self.connect(startAction, QtCore.SIGNAL("triggered()"), self.setup)
		self.setContextMenu(menu)

		menu.addSeparator()

		exitAction = menu.addAction("Exit")
		self.connect(exitAction, QtCore.SIGNAL("triggered()"), self.exit)
		self.setContextMenu(menu)

		self.setupDialog = None
		self.timeout = 0
		self.msg = "Default timeout message"
		self.timer = QtCore.QTimer(self)
		self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.endTimer)
		self.timerID = None

		self.onIcon = QtGui.QIcon("res/TimerOn.png")
		self.offIcon = QtGui.QIcon("res/TimerOff.png")

	def exit(self):
		sys.exit(0)
	
	def startTimer(self):
		if self.timeout < 1:
			QtGui.QMessageBox.information(None,
					"Timeless",
					("Timeout is less than 1 second. Can't have that"),
					QtGui.QMessageBox.Ok)
			return
		if self.timer.isActive() is False:
			self.timerID = self.timer.start(self.timeout)
			self.setIcon(self.onIcon)

	def stopTimer(self):
		if self.timer is not None:
			self.timer.stop()
			self.setIcon(self.offIcon)
	
	def endTimer(self):
		confirm = QtGui.QMessageBox.information(None,
        			"Time's up!",
					(self.msg + "\nOK to restart. Cancel to close this dialog"),
					QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
		if confirm == QtGui.QMessageBox.Ok:
			self.startTimer()
		else:
			self.stopTimer()
	
	def setup(self):
		if self.setupDialog is None:
			self.setupDialog = SetupUI(self)
			self.setupDialog.show()
		else:
			self.setupDialog.show()

	def setValues(self, seconds, msg):
		self.timeout = seconds * 1000
		self.msg = msg


def main():
	app = QtGui.QApplication(sys.argv)
	app.setQuitOnLastWindowClosed(False)
	w = QtGui.QWidget()
	trayIcon = SystemTrayIcon(QtGui.QIcon("res/TimerOff.png"), w)

	trayIcon.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

