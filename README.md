# Exam-results-system

A small Python OOP program for recording student exam scores (PROG211, Limkokwing University, Sierra Leone).
Author: Mohamed Sallieu Mansaray

## What it does
- `Student` class: stores ID, name, program and score; validates scores (instance, static and class methods)
- `Exam` class: checks Pass/Fail and gives a grade (tuple of grade bands)
- A dictionary stores students by ID; `add_student()` and `display_students()` manage it

## How to run
```
python main.py
```

## Example output
```
ID: 6144 | Name: Mohammed | Score: 78
Exam: PROG211 - Object Oriented Programming 1 (pass mark: 50)
Pass
ID: 6144 | Name: Mohammed | Score: 78
ID: 5656 | Name: Aminata | Score: 45
Fail
Invalid score. Use 0 to 100.
ID: 6144 | Name: Mohammed | Score: 78
ID: 5656 | Name: Aminata | Score: 45
ID: 1107 | Name: Kadiatu | Score: 67
B
F
C
```

## DPG alignment
- Open source: MIT licence, public on GitHub
- Privacy-respecting: stores only ID, name, program and score; no age, gender or contact details. Sample data is fictional.
- Inclusive and accessible: plain text output, simple English, runs on any computer with Python
- Modular and reusable: each class has one job and can be reused in other systems
