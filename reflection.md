# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

Three core actions a user should be able to perform with PawPal is to enter pet tasks, checkoff completed tasks, and add their pet.

For classes, we will need a Task class which holds the name of the task, a description, and time of the task. It should have the ability to be checked off.
We will also need a Checklist class that holds the tasks.
It should also have a Pet class that holds basic information about the pet like its name, age, and breed.
It will also have a class for the Owner so the owner can enter information about themselves.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
 
 Yes, my design changed during implementation. One change I made was adding a priority attribute to the tasks because CoPilot suggested that have a priority score may be helpful for the owner to determine which tasks require focus.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers the following constraints:
  - **Time**: Tasks are scheduled based on their specified time, and conflicts are detected if multiple tasks overlap.
  - **Priority**: Tasks can have different priority levels, which can be used to determine their importance in future enhancements.
  - **Pet-specific tasks**: Tasks are associated with specific pets, ensuring that each pet's schedule is managed independently while still detecting conflicts across pets.

The decision to prioritize time as the most important constraint was based on the need to avoid scheduling conflicts, which could lead to missed or overlapping tasks. Time conflicts are critical to address first, as they directly impact the feasibility of completing tasks.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff the scheduler makes is that it only detects conflicts and provides warnings rather than resolving them automatically. This means the user must manually adjust the schedule to resolve any conflicts.

This tradeoff is reasonable because it keeps the scheduler lightweight and avoids overly complex logic for automatic conflict resolution, which may not align with the user's preferences. By providing warnings, the scheduler empowers the user to make informed decisions while maintaining simplicity and flexibility.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

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
