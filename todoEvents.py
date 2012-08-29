
import sys
from PyQt4 import QtGui, QtCore
import ServerCommunicator
import todo

main = MainWindow()

def newEvent():
    text, ok = QtGui.QInputDialog.getText(self, 'New Task',
            'Enter the new Task:')

    if ok:
        newbox = QtGui.QCheckBox(str(text), main)
        main.grid.addWidget(newbox, main.currentGridRow, 1)

