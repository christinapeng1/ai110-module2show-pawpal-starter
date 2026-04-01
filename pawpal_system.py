from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class Task:
    name: str
    description: str
    time: datetime
    is_completed: bool = False

    def check_off(self) -> None:
        """Mark the task as completed."""
        pass


@dataclass
class Pet:
    name: str
    age: int
    breed: str

    def get_details(self) -> str:
        """Return pet details as a formatted string."""
        pass


@dataclass
class Owner:
    name: str
    email: str
    phone: str

    def get_contact_info(self) -> str:
        """Return owner contact information as a formatted string."""
        pass


class Checklist:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the checklist."""
        pass

    def remove_task(self, task: Task) -> None:
        """Remove a task from the checklist."""
        pass

    def get_tasks(self) -> List[Task]:
        """Retrieve all tasks in the checklist."""
        pass