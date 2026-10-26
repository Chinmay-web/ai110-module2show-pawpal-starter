# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

For my initial design, I wanted users to be able to add pets, schedule activities like feeding and walking, and view their daily tasks. I chose four main classes: Owner, Pet, Task, and Scheduler. The Owner class manages the pets, while the Pet class stores each pet's information and tasks. The Task class represents activities with details like time and completion status. The Scheduler class organizes tasks by time and helps identify scheduling conflicts.

**b. Design changes**

I initially designed the system with four classes: Owner, Pet, Task, and Scheduler. After reviewing the design with AI, I realized the Task class needed a due_date attribute to support recurring activities. I added this attribute because the scheduler will eventually need to distinguish tasks scheduled for different days. This change keeps the design simple while making it easier to implement recurring tasks later.

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

I used AI to help brainstorm the class structure, create the UML diagram, and develop the Python class skeletons. AI was especially helpful when organizing the relationships between Owner, Pet, Task, and Scheduler. I reviewed the generated code and made adjustments while debugging the CLI output. I verified the implementation by running `main.py` and manually executing two tests. Both tests passed.

**b. Judgment and verification**

One example of using my own judgment was when the AI-generated code caused errors while printing the schedule. Instead of accepting the code as correct, I reviewed the output and adjusted how the task information was displayed. I verified the changes by running main.py and checking that the tasks appeared in chronological order. I also ran two tests to confirm that task completion and task addition worked correctly.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
