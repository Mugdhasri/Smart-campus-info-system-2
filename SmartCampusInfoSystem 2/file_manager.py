# -*- coding: utf-8 -*-
# ============================================================
# Lab 6: File Handling for Student Academic Records
# Smart Campus Information System
# ============================================================

import os

RECORDS_FILE = "student_records.txt"


def write_records():
    """Write student details to a file."""
    with open(RECORDS_FILE, "w") as file:
        file.write("ID,Name,Marks\n")
        file.write("101,Arjun,85\n")
        file.write("102,Meera,92\n")
        file.write("103,Ravi,76\n")
        file.write("104,Anita,89\n")
    print(f"Student records written to '{RECORDS_FILE}' successfully.")


def read_records():
    """Read and display stored records from the file."""
    print(f"\nReading records from '{RECORDS_FILE}':")
    print("-" * 30)
    with open(RECORDS_FILE, "r") as file:
        records = file.readlines()
        for record in records:
            print(record.strip())
    return records


def generate_report(records):
    """Process stored data to generate a simple performance report."""
    print("\n--- Performance Report ---")
    total_students = 0
    total_marks = 0
    highest_marks = -1
    lowest_marks = 101
    top_student = ""
    low_student = ""

    for record in records[1:]:   # Skip header
        parts = record.strip().split(",")
        if len(parts) < 3:
            continue
        name  = parts[1]
        marks = int(parts[2])

        total_students += 1
        total_marks    += marks

        if marks > highest_marks:
            highest_marks = marks
            top_student   = name
        if marks < lowest_marks:
            lowest_marks = marks
            low_student  = name

    if total_students == 0:
        print("No student data found.")
        return

    average_marks = total_marks / total_students
    print(f"Total Students : {total_students}")
    print(f"Average Marks  : {average_marks:.2f}")
    print(f"Top Student    : {top_student} ({highest_marks} marks)")
    print(f"Needs Attention: {low_student} ({lowest_marks} marks)")


def file_management_module():
    """Run the full file handling module."""
    print("\n" + "=" * 45)
    print("   FILE HANDLING – ACADEMIC RECORDS MANAGER")
    print("=" * 45)
    write_records()
    records = read_records()
    generate_report(records)


if __name__ == "__main__":
    file_management_module()
