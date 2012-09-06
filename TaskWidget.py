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
        self.editButton = QtGui.QPushButton("+")
        self.editButton.setFixedSize(50, 20)

        self.deleteButton = QtGui.QPushButton("X")
        self.deleteButton.setFixedSize(50, 20)

        self.editButton.clicked.connect(self.onEditClicked)
        self.deleteButton.clicked.connect(self.onDeleteClicked)

        self.hbox.addWidget(self.checkbox)
        self.hbox.addWidget(self.editButton)
        self.hbox.addWidget(self.deleteButton)

        self.setLayout(self.hbox)

    def onDeleteClicked(self):

        self.checkbox.setParent(None)
        self.editButton.setParent(None)
        self.deleteButton.setParent(None)

        self.index -= 1

    def onEditClicked(self):

        text, ok = QtGui.QInputDialog.getText(self, 'New Task',
            'Edit the current Task:')

        if ok:
            self.checkbox.setText(str(text))
            self.tModel.changeTitle(str(text))

