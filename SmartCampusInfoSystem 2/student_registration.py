# -*- coding: utf-8 -*-
# ============================================================
# Lab 1: Student Registration and Grade Evaluation
# Smart Campus Information System
# ============================================================

def register_student():
    """Accept student details and evaluate grade."""
    print("\n" + "=" * 45)
    print("   STUDENT REGISTRATION & GRADE EVALUATION")
    print("=" * 45)

    # Step 1: Input collection
    student_name = input("Enter student name: ").strip()
    while True:
        try:
            score = float(input("Enter exam score (0-100): "))
            if 0 <= score <= 100:
                break
            else:
                print("Score must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric score.")

    # Step 2: Grade evaluation using conditional statements
    if score >= 90 and score <= 100:
        grade = "A"
        remark = "Excellent"
    elif score >= 75:
        grade = "B"
        remark = "Very Good"
    elif score >= 60:
        grade = "C"
        remark = "Good"
    elif score >= 40:
        grade = "D"
        remark = "Average"
    else:
        grade = "F"
        remark = "Needs Improvement"

    # Step 3: Output display
    print("\n--- Student Report ---")
    print(f"Name             : {student_name}")
    print(f"Score            : {score}")
    print(f"Grade            : {grade}")
    print(f"Performance Remark: {remark}")
    print("-" * 25)

    return {"name": student_name, "score": score, "grade": grade, "remark": remark}


if __name__ == "__main__":
    register_student()
