from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from collections import defaultdict


@dataclass
class Task:
    description: str
    time: datetime
    frequency: str  # e.g., "daily", "weekly", "once"
    is_completed: bool = False
    priority: int = 0  # Priority score (e.g., 1 = high, 5 = low)

    def check_off(self) -> None:
        """Mark the task as completed."""
        self.is_completed = True


@dataclass
class Pet:
    name: str
    age: int
    breed: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to the pet's task list."""
        self.tasks.append(task)

    def get_tasks(self, include_completed: bool = False) -> List[Task]:
        """Retrieve tasks for the pet, optionally filtering out completed tasks."""
        if include_completed:
            return self.tasks
        return [task for task in self.tasks if not task.is_completed]


@dataclass
class Owner:
    name: str
    email: str
    phone: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's list of pets."""
        self.pets.append(pet)

    def get_all_tasks(self, include_completed: bool = False) -> List[Task]:
        """Retrieve all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks(include_completed=include_completed))
        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_tasks_by_priority(self, include_completed: bool = False) -> List[Task]:
        """Retrieve all tasks across pets, sorted by priority."""
        tasks = self.owner.get_all_tasks(include_completed=include_completed)
        return sorted(tasks, key=lambda task: task.priority)

    def get_tasks_by_time(self):
        """Retrieve all tasks across pets, sorted by time."""
        tasks = []
        for pet in self.owner.pets:
            tasks.extend(pet.tasks)
        return sorted(tasks, key=lambda task: task.time)

    def schedule_task(self, pet_name: str, task: Task) -> Optional[str]:
        """Add a task to a specific pet by name."""
        for pet in self.owner.pets:
            if pet.name == pet_name:
                pet.add_task(task)
                return f"Task '{task.description}' scheduled for {pet.name}."
        return f"Pet '{pet_name}' not found."

    def mark_task_completed(self, pet_name: str, task_description: str) -> Optional[str]:
        """Mark a specific task as completed for a specific pet."""
        for pet in self.owner.pets:
            if pet.name == pet_name:
                for task in pet.tasks:
                    if task.description == task_description and not task.is_completed:
                        task.check_off()
                        return f"Task '{task_description}' marked as completed for {pet.name}."
        return f"Task '{task_description}' not found for pet '{pet_name}'."

    def filter_tasks(self, pet_name: Optional[str] = None, include_completed: Optional[bool] = None) -> List[Task]:
        """Filter tasks by pet name or completion status."""
        tasks = self.owner.get_all_tasks(include_completed=True)  # Start with all tasks
        if pet_name:
            tasks = [task for pet in self.owner.pets if pet.name == pet_name for task in pet.tasks]
        if include_completed is not None:
            tasks = [task for task in tasks if task.is_completed == include_completed]
        return tasks

    def detect_conflicts(self):
        """Detect and return warnings for task scheduling conflicts."""
        # Group tasks by time
        conflicts = defaultdict(list)
        for pet in self.owner.pets:
            for task in pet.tasks:
                conflicts[task.time].append((pet.name, task.description))
        
        # Generate warnings for conflicts
        warnings = [
            f"Conflict detected at {time.strftime('%H:%M')}: " +
            ", ".join([f"{desc} for {pet}" for pet, desc in entries])
            for time, entries in conflicts.items() if len(entries) > 1
        ]
        
        return warnings