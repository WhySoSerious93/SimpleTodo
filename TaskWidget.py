from PyQt4 import QtGui, QtCore

class TaskWidget(QtGui.QWidget):
    def __init__(self, taskModel, currentIndex):
        self.tModel = taskModel
        self.index = currentIndex
        super().__init__()

        self.hbox = QtGui.QHBoxLayout(self)

        self.paint()

    def paint(self):
        self.checkbox = QtGui.QCheckBox(self.tModel.getTitle(), self)
        self.eButton = QtGui.QPushButton("+")
        self.eButton.setFixedSize(50, 20)

        self.cButton = QtGui.QPushButton("X")
        self.cButton.setFixedSize(50, 20)

        self.eButton.clicked.connect(self.onEditClicked)
        self.cButton.clicked.connect(self.onDeleteClicked)

        self.hbox.addWidget(self.checkbox)
        self.hbox.addWidget(self.eButton)
        self.hbox.addWidget(self.cButton)

        self.setLayout(self.hbox)

    def onDeleteClicked(self):

        self.checkbox.setParent(None)
        self.eButton.setParent(None)
        self.cButton.setParent(None)

        self.index -= 1

    def onEditClicked(self):

        text, ok = QtGui.QInputDialog.getText(self, 'New Task',
            'Edit the current Task:')

        if ok:
            self.checkbox.setText(str(text))
            self.tModel.changeTitle(str(text))
            print ("Changes successful !")

