from PyQt4 import QtGui, QtCore

class TaskWidget(QtGui.QWidget):
    taskDeleteClicked = QtCore.pyqtSignal()

    def __init__(self, taskModel):
        super().__init__()

        self.taskModel = taskModel
        self.hbox = QtGui.QHBoxLayout(self)

        self.paint()

    def paint(self):
        self.checkbox = QtGui.QCheckBox(self.taskModel.getTitle(), self)
        if self.taskModel.isDone():
            self.checkbox.setCheckState(QtCore.Qt.Checked)

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
        # TODO remove task model
        self.taskDeleteClicked.emit()

    def onEditClicked(self):
        text, ok = QtGui.QInputDialog.getText(self, 'New Task',
            'Edit the current Task:')

        if ok:
            self.checkbox.setText(str(text))
            self.taskModel.changeTitle(str(text))

