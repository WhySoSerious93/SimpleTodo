
from task import TaskModel

def loadTasks():
    """ Loads all existing tasks from the server. """
    # For now only return a list of example tasks.
    return [TaskModel("CS:GO hartzen",               True),
            TaskModel("Benutzerverwaltung bedacht",  False),
            TaskModel("Geilste Todo App geschaffen", True)]
