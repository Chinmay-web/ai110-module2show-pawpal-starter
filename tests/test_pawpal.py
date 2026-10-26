from pawpal_system import Task, Pet


def test_task_completion():
    task = Task("Morning walk", "08:00", "daily")

    assert task.completed == False

    task.mark_complete()

    assert task.completed == True


def test_task_addition():
    pet = Pet("Buddy", "Dog", 3)

    assert len(pet.tasks) == 0

    task = Task("Feed Buddy", "09:00", "daily")
    pet.add_task(task)

    assert len(pet.tasks) == 1