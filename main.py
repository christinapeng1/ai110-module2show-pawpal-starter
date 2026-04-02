from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler

# Create an Owner
owner = Owner(name="Alice", email="alice@example.com", phone="123-456-7890")

# Create two Pets
pet1 = Pet(name="Buddy", age=3, breed="Golden Retriever")
pet2 = Pet(name="Mittens", age=2, breed="Siamese Cat")

# Add Pets to the Owner
owner.add_pet(pet1)
owner.add_pet(pet2)

# Create Tasks with different times
task1 = Task(description="Morning Walk", time=datetime.now() + timedelta(hours=1), frequency="daily", priority=1)
task2 = Task(description="Feed Breakfast", time=datetime.now() + timedelta(hours=2), frequency="daily", priority=2)
task3 = Task(description="Vet Appointment", time=datetime.now() + timedelta(hours=5), frequency="once", priority=1)

# Add Tasks to Pets
pet1.add_task(task1)
pet1.add_task(task2)
pet2.add_task(task3)

# Create a Scheduler
scheduler = Scheduler(owner)

# Print "Today's Schedule"
print("Today's Schedule:")
tasks = scheduler.get_tasks_by_time()
for task in tasks:
    print(f"- {task.time.strftime('%Y-%m-%d %H:%M:%S')} | {task.description} | Priority: {task.priority}")