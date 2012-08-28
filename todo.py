
import sys
from PyQt4 import QtGui, QtCore


class ModelStack (QtGui.QStackedWidget): 
    """ 
        Main Window which could be used to switch between
        different pages.
    """
    def __init__(self, parent = None):

        super(ModelStack, self).__init__(parent)
        self.frontpage = FrontPage(self)
        self.addWidget(self.frontpage)
        self.setCurrentWidget(self.frontpage)


class FrontPage(QtGui.QWidget):
    """
        The main operating page.
    """ 
    def __init__(self, parent):

        super(FrontPage, self).__init__()
        self.FP_Model()

    def FP_Model(self):
        """
            Defines how the front page looks like
        """
        # Group box in order to group the displayed tasks in a frame
        self.groupbox = QtGui.QGroupBox("TO-DO-LIST")
        # GridLayout in order to place the buttons, tasks appropriately.
        self.grid = QtGui.QGridLayout()

        # Some sample tasks to show the general design concept.
        self.task1 = QtGui.QCheckBox("Do your homework", self)
        self.task2 = QtGui.QCheckBox("Play Counter-Strike till Midnight", self)
        self.task3 = QtGui.QCheckBox("Sleep till next day afternoon", self)

        # Buttons to edit your tasks.
        self.add = QtGui.QPushButton("Add")
        self.new = QtGui.QPushButton("New")
        self.cancel = QtGui.QPushButton("Cancel")

        # All Elements are add to the Layout and placed at a certain position.
        self.grid.addWidget(self.task1, 0, 1)
        self.grid.addWidget(self.task2, 1, 1)
        self.grid.addWidget(self.task3, 2, 1)

        self.grid.addWidget(self.add, 4, 1)
        self.grid.addWidget(self.new, 4, 2)
        self.grid.addWidget(self.cancel, 4, 3)

        self.setLayout(self.grid)
        self.move(300, 300)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = ModelStack()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


