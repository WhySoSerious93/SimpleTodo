
from task import TaskModel

_tasks = [TaskModel(1, "Deus Ex HR hartzen", True),
          TaskModel(2, "Erfolgreich investieren", False),
          TaskModel(3, "Geilste Todo App geschaffen", True)]

def loadTasks():
    """ Loads all existing tasks from the server. """
    # For now only return a list of example tasks.
    return _tasks

def createNewTask(text):
    """
        This function creates a new task with the given text, sends it to the
        database to retrieve the task id and returns a TaskModel instance.
    """
    # For now find out the highest id from the existing tasks and use
    # that id + 1 for the new task.
    highestId = -1
    for task in _tasks:
        if task.id > highestId:
            highestId = task.id

    newId = highestId + 1
    newTask = TaskModel(newId, text, False)
    _tasks.append(newTask)
    return newTask
