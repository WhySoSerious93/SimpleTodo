
import sys
from PyQt4 import QtGui, QtCore
import ServerCommunicator
from todo import MainWindow


def newEvent(parent, currentGrid):
    text, ok = QtGui.QInputDialog.getText(parent, 'New Task',
            'Enter the new Task:')

    if ok:
        newbox = QtGui.QCheckBox(str(text), parent)
        parent.grid.addWidget(newbox, currentGrid, 1)

