from pawpal_system import Owner, Pet, Task, Scheduler

# Create an owner
owner = Owner("Alex")

# Create two pets
pet1 = Pet("Buddy", "Dog", 3)
pet2 = Pet("Luna", "Cat", 2)

# Add pets to owner
owner.add_pet(pet1)
owner.add_pet(pet2)

# Create tasks
task1 = Task("Morning walk", "08:00", "daily")
task2 = Task("Feed Buddy", "09:00", "daily")
task3 = Task("Feed Luna", "07:30", "daily")

# Assign tasks to pets
pet1.add_task(task1)
pet1.add_task(task2)
pet2.add_task(task3)

# Create scheduler
scheduler = Scheduler(owner)

# Print today's schedule
print("\n=== Today's Schedule ===")

for pet, task in scheduler.sort_by_time():
    print(f"{task.time} - {pet}: {task.description}")