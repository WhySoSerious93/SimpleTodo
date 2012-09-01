
import sys
from PyQt4 import QtGui, QtCore
import ServerCommunicator
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

    def paint(self):
        """
            Defines how the main window looks like.
        """
        # Group box in order to group the displayed tasks in a frame
        self.groupbox = QtGui.QGroupBox("TO-DO-LIST")
        # GridLayout in order to place the buttons, tasks appropriately.
        self.grid = QtGui.QGridLayout()
        # VBoxLayout holding the tasks.
        self.taskVBox = QtGui.QVBoxLayout()
        self.currentTaskIndex = 0

        tasks = ServerCommunicator.loadTasks()
        for task in tasks:
            self.addTask(task)

        # Buttons to edit your tasks.
        self.edit = QtGui.QPushButton("Edit")
        self.new = QtGui.QPushButton("New")
        self.cancel = QtGui.QPushButton("Cancel")

        # When new Button clicked, call todoEvents.newEvent where the first argument is this MainWindow.
        self.new.clicked.connect(todoEvents.newEvent.__get__(self))
        self.edit.clicked.connect(self.call_editEvent)

        self.grid.addLayout(self.taskVBox, 0, 1)
        self.grid.addWidget(self.edit,     1, 1)
        self.grid.addWidget(self.new,      1, 2)
        self.grid.addWidget(self.cancel,   1, 3)

        self.setLayout(self.grid)
        self.move(300, 300)
        self.show()

    def addTask(self, taskModel):
        """ Adds a task to the task list. """
        checkbox = QtGui.QCheckBox(taskModel.getTitle(), self)
        if taskModel.isDone():
            checkbox.setCheckState(QtCore.Qt.Checked)
        else:
            checkbox.setCheckState(QtCore.Qt.Unchecked)

        self.taskVBox.addWidget(checkbox, self.currentTaskIndex)
        self.currentTaskIndex += 1

    def call_editEvent(self):
        todoEvents.editEvent(self, self.currentGridRow, self.grid)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = ModelStack()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
