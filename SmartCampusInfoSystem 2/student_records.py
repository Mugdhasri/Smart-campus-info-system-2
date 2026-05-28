# -*- coding: utf-8 -*-
# ============================================================
# Lab 3: Student Record Data Management using Data Structures
# Smart Campus Information System
# ============================================================

def manage_student_records():
    """Store and manage student records using lists, dicts, and sets."""
    print("\n" + "=" * 45)
    print("   STUDENT RECORD DATA MANAGEMENT SYSTEM")
    print("=" * 45)

    # Step 1: Input Collection - list of dictionaries
    students = []
    students.append({"name": "Priya",  "age": 20, "grades": [85, 90, 78]})
    students.append({"name": "Rahul",  "age": 21, "grades": [72, 88, 91]})
    students.append({"name": "Anita",  "age": 19, "grades": [95, 89, 92]})

    # Step 2: Record Management - display using loop
    print("\n=== Student Records ===")
    for student in students:
        avg = sum(student["grades"]) / len(student["grades"])
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Grades : {student['grades']}")
        print(f"Average: {avg:.2f}")
        print("-" * 25)

    # Step 3: Event Participation Analysis using Sets
    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}

    common_participants = event_A & event_B      # intersection
    all_participants    = event_A | event_B      # union
    only_event_A        = event_A - event_B      # difference

    # Step 4: Output Display
    print("\n=== Event Participation Analysis ===")
    print(f"Event A Participants : {event_A}")
    print(f"Event B Participants : {event_B}")
    print(f"Common Participants  : {common_participants}")
    print(f"All Participants     : {all_participants}")
    print(f"Only Event A         : {only_event_A}")

    return students


if __name__ == "__main__":
    manage_student_records()
