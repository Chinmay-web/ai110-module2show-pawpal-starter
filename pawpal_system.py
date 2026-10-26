
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False
    due_date: str = ""

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's collection."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Collect tasks from all pets."""
        all_tasks = []

        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))

        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner):
        """Initialize the scheduler with an owner."""
        self.owner = owner

    def sort_by_time(self):
        """Sort all pet tasks by scheduled time."""
        return sorted(
            self.owner.get_all_tasks(),
            key=lambda item: item[1].time
        )

    def filter_tasks(self, pet_name=None, completed=None):
        """Filter tasks by pet name or completion status."""
        tasks = self.owner.get_all_tasks()
        results = []

        for name, task in tasks:
            if pet_name is not None and name != pet_name:
                continue

            if completed is not None and task.completed != completed:
                continue

            results.append((name, task))

        return results

    def detect_conflicts(self):
        """Find tasks scheduled for the same date and time."""
        tasks = self.owner.get_all_tasks()
        conflicts = []

        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                first = tasks[i][1]
                second = tasks[j][1]

                if (first.time == second.time and
                        first.due_date == second.due_date):
                    conflicts.append((tasks[i], tasks[j]))

        return conflicts
