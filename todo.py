
import sys
from PyQt4 import QtGui, QtCore
import ServerCommunicator

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
        super(MainWindow, self).__init__()
        self.FP_Model()

    def FP_Model(self):
        """
            Defines how the main window looks like.
        """
        # Group box in order to group the displayed tasks in a frame
        self.groupbox = QtGui.QGroupBox("TO-DO-LIST")
        # GridLayout in order to place the buttons, tasks appropriately.
        self.grid = QtGui.QGridLayout()

        # Load tasks and create and add widgets.
        currentGridRow = 0
        tasks = ServerCommunicator.loadTasks()
        for task in tasks:
            checkbox = QtGui.QCheckBox(task.getTitle(), self)

            # Set checked.
            if task.isDone():
                checkbox.setCheckState(QtCore.Qt.Checked)
            else:
                checkbox.setCheckState(QtCore.Qt.Unchecked)

            self.grid.addWidget(checkbox, currentGridRow, 1)
            currentGridRow += 1

        # Buttons to edit your tasks.
        self.add = QtGui.QPushButton("Add")
        self.new = QtGui.QPushButton("New") # TODO: What is the difference between "Add" and "New"?
        self.cancel = QtGui.QPushButton("Cancel")

        self.grid.addWidget(self.add,    currentGridRow + 1, 1)
        self.grid.addWidget(self.new,    currentGridRow + 1, 2)
        self.grid.addWidget(self.cancel, currentGridRow + 1, 3)

        self.setLayout(self.grid)
        self.move(300, 300)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = ModelStack()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
