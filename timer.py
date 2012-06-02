#!/usr/bin/env python2.6
import sys
from PyQt4 import QtGui, QtCore
from ui.timerUI import Ui_Timer
import datetime
import ConfigParser
import os

class SetupUI(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, None)
        self.ui = Ui_Timer()
        self.ui.setupUi(self)
        self.parent = parent

        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.setTimerValues)
    
    def setValues(self, time, msg):
        time = str(datetime.timedelta(seconds=time/1000)).split(':')
        hours = int(time[0])
        minutes = int(time[1])
        seconds = int(time[2])

        self.ui.HourSpin.setValue(hours)
        self.ui.MinuteSpin.setValue(minutes)
        self.ui.SecondSpin.setValue(seconds)
        self.ui.PopupEdit.setText(msg)

    def setTimerValues(self):
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

        self.loadConfig()

    def loadConfig(self):
        self.useConfig = True
        configPath = os.path.expanduser(os.path.join("~", ".config", "easytimer"))
        if not os.path.exists(configPath):
            try:
                os.makedirs(configPath)
            except:
                self.useConfig = False
                return

        self.configFile = os.path.join(configPath, "conf")

        self.config = ConfigParser.ConfigParser()
        opened_files = self.config.read(self.configFile)
        if len(opened_files) == 0:
            self.config.add_section("main")
            try:
                f = open(self.configFile, 'w+')
                f.close()
            except:
                self.useConfig = False
                pass
        else:
            self.timeout = self.config.getint("main", "seconds")
            self.msg = self.config.get("main", "msg")

    def exit(self):
        sys.exit(0)

    def error(self, msg):
         QtGui.QMessageBox.warning(None,
                    "Error",
                    (msg),
                    QtGui.QMessageBox.Ok)
    
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
        
        self.setupDialog.setValues(self.timeout, self.msg)
        self.setupDialog.show()
        self.setupDialog.raise_()

    def setValues(self, seconds, msg):
        self.timeout = seconds * 1000
        self.msg = msg

        if self.useConfig:
            self.config.set("main", "seconds", self.timeout)
            self.config.set("main", "msg", self.msg)

            with open(self.configFile, 'wb') as config_fh:
                self.config.write(config_fh)

def main():
    app = QtGui.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    w = QtGui.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon("res/TimerOff.png"), w)

    trayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

