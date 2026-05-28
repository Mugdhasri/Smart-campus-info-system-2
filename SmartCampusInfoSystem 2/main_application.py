# -*- coding: utf-8 -*-
# ============================================================
# Lab 9 & 10: Smart Campus Information System
#             Main Application Dashboard
#
# Dayananda Sagar College of Engineering
# Python Programming Lab - Integration of Labs 1 to 8
#
# Modules Integrated:
#   1. Student Registration & Grade Evaluation   (Lab 1)
#   2. Course Enrollment Management              (Lab 2)
#   3. Student Record Data Management            (Lab 3)
#   4. Sorting and Searching Student IDs         (Lab 4)
#   5. Fee Calculation using Functions           (Lab 5)
#   6. File Handling - Academic Records          (Lab 6)
#   7. Directory Scanning with Exception Handling(Lab 7)
#   8. Performance Analytics (NumPy/Pandas/Matplotlib)(Lab 8)
# ============================================================

from student_registration  import register_student
from course_enrollment     import manage_enrollment
from student_records       import manage_student_records
from search_sort_students  import sort_and_search
from fee_calculation       import fee_calculator_menu, demo_fee_calculation
from file_manager          import file_management_module
from directory_scanner     import directory_scanner_module
from performance_analytics import analyze_performance


BANNER = """
==============================================================
       SMART CAMPUS INFORMATION SYSTEM
       Dayananda Sagar College of Engineering
       Python Programming Lab - Final Integration
==============================================================
"""

MENU = """
+----------------------------------------------+
|           MAIN SYSTEM DASHBOARD              |
+----------------------------------------------+
|  1. Student Registration & Grade Evaluation  |
|  2. Course Enrollment Management             |
|  3. Student Record Data Management           |
|  4. Sorting & Searching Student IDs          |
|  5. Fee Calculation                          |
|  6. File Handling - Academic Records         |
|  7. Directory Scanner                        |
|  8. Performance Analytics                    |
|  0. Exit                                     |
+----------------------------------------------+
"""


def main():
    print(BANNER)

    while True:
        print(MENU)
        choice = input("Enter your choice (0-8): ").strip()

        if choice == "1":
            register_student()

        elif choice == "2":
            manage_enrollment()

        elif choice == "3":
            manage_student_records()

        elif choice == "4":
            sort_and_search()

        elif choice == "5":
            print("\n--- Demo Cases ---")
            demo_fee_calculation()
            print("\n--- Custom Fee Calculation ---")
            fee_calculator_menu()

        elif choice == "6":
            file_management_module()

        elif choice == "7":
            directory_scanner_module()

        elif choice == "8":
            analyze_performance()

        elif choice == "0":
            print("\n" + "=" * 50)
            print("  Thank you for using Smart Campus Info System!")
            print("  Dayananda Sagar College of Engineering")
            print("=" * 50 + "\n")
            break

        else:
            print("\n[!] Invalid choice. Please enter a number between 0 and 8.")

        input("\n[Press Enter to return to the Main Menu...]")


if __name__ == "__main__":
    main()
