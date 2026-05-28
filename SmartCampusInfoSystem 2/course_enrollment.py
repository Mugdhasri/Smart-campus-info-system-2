# -*- coding: utf-8 -*-
# ============================================================
# Lab 2: Course Enrollment Management System
# Smart Campus Information System
# ============================================================

def manage_enrollment():
    """Manage course enrollment with loops, continue, and break."""
    print("\n" + "=" * 45)
    print("      COURSE ENROLLMENT MANAGEMENT SYSTEM")
    print("=" * 45)

    courses = []       # list to store (course_name, credits)
    max_courses = 5

    # Step 1 & 2: Input collection with loop, continue, and break
    while True:
        if len(courses) >= max_courses:
            print(f"\nMaximum course limit ({max_courses}) reached!")
            break

        course_name = input("\nEnter course name (or 'done' to finish): ").strip()
        if course_name.lower() == "done":
            break
        if not course_name:
            print("Course name cannot be empty! Skipping entry...")
            continue

        credits = input("Enter credit value: ").strip()

        # Step 2: Validation
        if not credits.isdigit():
            print("Invalid credit value! Skipping entry...")
            continue

        credits = int(credits)
        if credits <= 0:
            print("Credit must be positive! Skipping entry...")
            continue

        # Valid entry
        courses.append((course_name, credits))
        print(f"Course '{course_name}' with {credits} credits added.")

    # Step 3: Output display
    print("\n--- Enrollment Report ---")
    if courses:
        for course, credit in courses:
            print(f"  Course: {course}, Credits: {credit}")
        print(f"Total courses enrolled: {len(courses)}")
    else:
        print("No courses enrolled.")

    return courses


if __name__ == "__main__":
    manage_enrollment()
