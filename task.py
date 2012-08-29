
class TaskModel:
    """
        This class represents a task identified by its unique id.
    """

    def __init__(self, id, title, done):
        """
            Initializes a new instance of the TaskModel class.
            title: The title of the task.
            done: True if the task is done, otherwise false.
        """
        self.id = id
        self._title = title
        self._done = done


    def _changeProperty(self, propertyName, propertyValue):
        """
            Changes the given property of this model on the server.
            It automatically updates the value of this model instance.
        """
        # TODO: Add server communication later.

        # Gets the property with the given name and changes its value.
        # __dict__ is a variable containing all attributes and the associated value in a dictionary.
        self.__dict__[propertyName] = propertyValue

    def changeTitle(self, newTitle):
        """ Changes the title of the task. """
        self._changeProperty("title", newTitle)

    def changeDone(self, isDone):
        """ Changes the value indicating whether the task is done. """
        self._changeProperty("done", isDone)

    def getTitle(self):
        return self._title

    def isDone(self):
        return self._done
