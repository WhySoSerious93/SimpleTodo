import sys
from PyQt4 import QtGui, QtCore


class BasicModel (QtGui.QStackedWidget): 
    """ 
        Main Window which could be used to switch between
        different pages.
    """
    def __init__(self, parent = None):

        super(BasicModel, self).__init__(parent)
        self.frontpage = FrontPage(self)
        self.addWidget(self.frontpage)
        self.setCurrentWidget(self.frontpage)


class FrontPage(QtGui.QWidget):
    """
        The main operating page
    """ 
    def __init__(self, parent):

        super(FrontPage, self).__init__()
        self.FP_Model()

    def FP_Model(self):

        self.add = QtGui.QPushButton("Add")
        self.new = QtGui.QPushButton("New")
        self.cancel = QtGui.QPushButton("Cancel")