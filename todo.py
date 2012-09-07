#!/usr/bin/env python3
from PyQt4 import QtCore, QtGui
import  sys
import ServerCommunicator
from TaskWidget import TaskWidget
from functools import partial
import todoEvents

class ModelStack(QtGui.QStackedWidget):
    """
        Main Window which could be used to switch between
        different windows.
    """
    def __init__(self, parent = None):
        super(ModelStack, self).__init__(parent)
        self.mainWindow = MainWindow(self)
        self.addWidget(self.mainWindow)
        self.setCurrentWidget(self.mainWindow)


class MainWindow(QtGui.QWidget):
    """
        The main operating window.
    """
    def __init__(self, parent):
        super().__init__()
        self.paint()

    def onTaskWidgetDeleteClicked(self, taskWidget):
        self.taskVBox.removeWidget(taskWidget)

    def paint(self):
        """
            Defines how the main window looks like.
        """
        # Load tasks and create and add widgets.
        self.grid = QtGui.QGridLayout()
        self.taskVBox = QtGui.QVBoxLayout()
        self.currentTaskIndex = 0

        self.currentGridRow = 0
        tasks = ServerCommunicator.loadTasks()
        for task in tasks:
            newTask = TaskWidget(task)
            # Bind taskDeleteClicked to onTaskWidgetDeleteClicked where the additional
            # argument is the TaskWidget.
            newTask.taskDeleteClicked.connect(partial(self.onTaskWidgetDeleteClicked, newTask))


            # Set checked.
            # if task.isDone():
            #   checkbox.setCheckState(QtCore.Qt.Checked)
            #else:
            #    checkbox.setCheckState(QtCore.Qt.Unchecked)

            self.taskVBox.addWidget(newTask, self.currentTaskIndex)
            self.currentTaskIndex += 1

        # Buttons to edit your tasks.
        self.new = QtGui.QPushButton("New")
        self.new.clicked.connect(todoEvents.newEvent.__get__(self))

        self.grid.addLayout(self.taskVBox, 0, 1)
        self.grid.addWidget(self.new, 1, 1)

        self.setLayout(self.grid)
        self.move(300, 300)
        self.show()

    def addTask(self, taskModel):
        """ Adds a task to the task list. """
        Task = TaskWidget(taskModel)
        #if taskModel.isDone():
        #    checkbox.setCheckState(QtCore.Qt.Checked)
        #else:
        #    checkbox.setCheckState(QtCore.Qt.Unchecked)

        self.taskVBox.addWidget(Task)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = ModelStack()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
