
import sys
from PyQt4 import QtGui, QtCore
import ServerCommunicator
from todo import MainWindow


def newEvent(parent):
    text, ok = QtGui.QInputDialog.getText(parent, 'New Task',
            'Enter the new Task:')

    if ok:
        # Create new TaskModel and add it to the window.
        newTask = ServerCommunicator.createNewTask(text)
        parent.addTask(newTask)

def editEvent(parent, currentGrid, layout):
    for i in range(0, currentGrid):
        if layout.itemAtPosition(parent, i, 1) == QtGui.QCheckBox(parent):
            box = layout.itemAtPosition(parent, i, 1)

            if box.isChecked(parent) == True:
                text, ok = QtGui.QInputDialog.getText(parent, 'Edit Task',
                'Edit your current Task:')

            if ok:
                box.setText(str(text))


