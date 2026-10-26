# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

For my initial design, I wanted users to be able to add pets, schedule activities like feeding and walking, and view their daily tasks. I chose four main classes: Owner, Pet, Task, and Scheduler. The Owner class manages the pets, while the Pet class stores each pet's information and tasks. The Task class represents activities with details like time and completion status. The Scheduler class organizes tasks by time and helps identify scheduling conflicts.

**b. Design changes**

I initially designed the system with four classes: Owner, Pet, Task, and Scheduler. After reviewing the design with AI, I realized the Task class needed a due_date attribute to support recurring activities. I added this attribute because the scheduler will eventually need to distinguish tasks scheduled for different days. This change keeps the design simple while making it easier to implement recurring tasks later.

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**
My scheduler mainly considers the time each task is scheduled for, the pet assigned to the task, and whether the task has been completed. I decided that time was the most important constraint because the main purpose of PawPal+ is to help pet owners organize their daily activities. The scheduler sorts tasks in chronological order, making it easier for users to see what needs to be done first. It can also filter tasks by pet or completion status and identify tasks scheduled at the same date and time.

**b. Tradeoffs**

One tradeoff I made was keeping the scheduling system simple instead of automatically resolving conflicts between tasks. The scheduler can detect when two tasks are scheduled for the same date and time, but it does not automatically reschedule them. I think this is reasonable because pet owners may have different preferences, and automatically changing a task could create problems. This approach allows users to make their own decisions while keeping the system easy to understand.

## 3. AI Collaboration

I used AI to help brainstorm the class structure, create the UML diagram, and develop the Python class skeletons. AI was especially helpful when organizing the relationships between Owner, Pet, Task, and Scheduler. I reviewed the generated code and made adjustments while debugging the CLI output. I verified the implementation by running `main.py` and manually executing two tests. Both tests passed.

**b. Judgment and verification**

One example of using my own judgment was when the AI-generated code caused errors while printing the schedule. Instead of accepting the code as correct, I reviewed the output and adjusted how the task information was displayed. I verified the changes by running main.py and checking that the tasks appeared in chronological order. I also ran two tests to confirm that task completion and task addition worked correctly.

---

## 4. Testing and Verification

**a. What you tested**

I tested whether tasks could be marked as completed and whether tasks could be successfully added to a pet. I also ran main.py to check that the scheduler displayed activities in chronological order. These tests were important because they verified some of the main features of PawPal+. Both automated test functions passed when I ran them manually.

**b. Confidence**

I am confident that the basic features of my scheduler work correctly because the program successfully displayed the schedule and passed both tests. However, I would still want to test more complicated situations before considering the system fully complete. If I had more time, I would test scheduling conflicts, multiple tasks at the same time, and tasks scheduled on different dates. I would also test how the scheduler handles pets that do not have any assigned tasks.

## 5. Reflection

**a. What went well**

The part of this project I am most satisfied with is getting the different classes to work together. At first, organizing the relationships between Owner, Pet, Task, and Scheduler was challenging, but I was able to create a system that successfully stores pet information and organizes their daily tasks. Seeing the schedule print correctly after debugging the code was especially satisfying.


**b. What you would improve**

I would improve the scheduling system by adding automatic reminders and allowing users to reschedule tasks more easily. I would also like to develop a more interactive interface instead of relying on the command line. Another improvement would be expanding the recurring task functionality so users could manage daily and weekly activities across multiple dates.

**c. Key takeaway**

One important thing I learned from this project is that designing a system requires more than just writing code. I had to think about how different classes would interact and how information would move between them. I also learned that AI can be useful for brainstorming and generating code, but it is still important to review its suggestions, test the results, and make changes when something does not work correctly.
