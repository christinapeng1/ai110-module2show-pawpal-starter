from datetime import datetime
from pawpal_system import Task, Pet, Owner, Scheduler

# Create an owner and pets
owner = Owner(name="John Doe", email="john@example.com", phone="123-456-7890")
pet1 = Pet(name="Buddy", age=3, breed="Golden Retriever")
pet2 = Pet(name="Mittens", age=2, breed="Tabby Cat")
owner.add_pet(pet1)
owner.add_pet(pet2)

# Create a scheduler
scheduler = Scheduler(owner)

# Add tasks out of order
task1 = Task(description="Morning Walk", time=datetime.strptime("08:00", "%H:%M"), frequency="daily", priority=1)
task2 = Task(description="Evening Walk", time=datetime.strptime("18:00", "%H:%M"), frequency="daily", priority=2)
task3 = Task(description="Lunch Feeding", time=datetime.strptime("12:00", "%H:%M"), frequency="daily", priority=3)

pet1.add_task(task2)  # Add Evening Walk first
pet1.add_task(task1)  # Add Morning Walk second
pet1.add_task(task3)  # Add Lunch Feeding last

# Sort tasks by time and print
sorted_tasks = scheduler.get_tasks_by_time()
print("Tasks sorted by time:")
for task in sorted_tasks:
    print(f"{task.description} at {task.time.strftime('%H:%M')}")

# Filter tasks by completion status
filtered_tasks = scheduler.filter_tasks(include_completed=False)
print("\nIncomplete tasks:")
for task in filtered_tasks:
    print(f"{task.description} at {task.time.strftime('%H:%M')}")

# Filter tasks by pet name
filtered_tasks_by_pet = scheduler.filter_tasks(pet_name="Buddy")
print("\nTasks for Buddy:")
for task in filtered_tasks_by_pet:
    print(f"{task.description} at {task.time.strftime('%H:%M')}")