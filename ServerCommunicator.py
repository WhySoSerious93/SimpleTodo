
from task import TaskModel

def loadTasks():
    """ Loads all existing tasks from the server. """
    # For now only return a list of example tasks.
    return [TaskModel(1, "Deus Ex HR hartzen", False),
            TaskModel(2, "Erfolgreich investieren", False),
            TaskModel(3, "Geilste Todo App geschaffen", False)]
