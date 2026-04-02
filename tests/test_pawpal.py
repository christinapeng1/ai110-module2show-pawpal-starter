from datetime import datetime, timedelta
from pawpal_system import Pet, Task

def test_mark_complete():
    pet = Pet(name="Buddy", age=3, breed="Golden Retriever")
    task = Task(description="Walk the dog", time=datetime.now(), frequency="daily")
    pet.add_task(task)
    # Mark the task as completed
    task.check_off()
    assert task.is_completed == True

def test_add_task_increases_count():
    pet = Pet(name="Buddy", age=3, breed="Golden Retriever")
    initial_count = len(pet.tasks)
    task = Task(description="Feed the dog", time=datetime.now(), frequency="daily")
    pet.add_task(task)
    assert len(pet.tasks) == initial_count + 1