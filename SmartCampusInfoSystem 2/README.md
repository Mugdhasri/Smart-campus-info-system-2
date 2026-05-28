# Smart Campus Information System
### Python Programming Lab – Dayananda Sagar College of Engineering
**Course Code:** 1BPLC105B / 205B

---

## Overview

A Python-based **Smart Campus Information System** that digitally manages student information, academic records, and performance analysis. Developed module by module across 9 lab experiments and integrated into a single Main Application Dashboard.

---

## Modules

| Lab | File | Description |
|-----|------|-------------|
| Lab 1 | `student_registration.py` | Student Registration & Grade Evaluation |
| Lab 2 | `course_enrollment.py` | Course Enrollment Management |
| Lab 3 | `student_records.py` | Student Record Data Management (Lists, Dicts, Sets) |
| Lab 4 | `search_sort_students.py` | Sorting (Bubble/Selection) & Searching (Linear/Binary) |
| Lab 5 | `fee_calculation.py` | Fee Calculation using Functions |
| Lab 6 | `file_manager.py` | File Handling – Academic Records |
| Lab 7 | `directory_scanner.py` | Directory Scanning with Exception Handling |
| Lab 8 | `performance_analytics.py` | Performance Analytics (NumPy, Pandas, Matplotlib) |
| Lab 9&10 | `main_application.py` | Main System Dashboard – Full Integration |

---

## How to Run

### Prerequisites
```bash
pip install numpy pandas matplotlib
```

### Run the Main Application
```bash
cd SmartCampusInfoSystem
python main_application.py
```

### Run Individual Modules
```bash
python student_registration.py
python course_enrollment.py
python student_records.py
python search_sort_students.py
python fee_calculation.py
python file_manager.py
python directory_scanner.py
python performance_analytics.py
```

---

## Features

- **Student Registration** – Input student name & score, evaluate grade (A–F) with performance remarks
- **Course Enrollment** – Add up to 5 courses with credit validation using loops, `break`, and `continue`
- **Record Management** – Manage student records using lists, dictionaries, and sets for event analysis
- **Sort & Search** – Sort IDs with Bubble Sort & Selection Sort; search with Linear & Binary Search
- **Fee Calculation** – Modular fee calculator with optional hostel and transportation fees
- **File Handling** – Write, read, and generate reports from student academic record files
- **Directory Scanner** – Scan folder structures with custom exception handling
- **Performance Analytics** – Statistical analysis and bar charts using NumPy, Pandas, and Matplotlib

---

## Project Structure

```
SmartCampusInfoSystem/
├── main_application.py         ← Entry point (Lab 9 & 10)
├── student_registration.py     ← Lab 1
├── course_enrollment.py        ← Lab 2
├── student_records.py          ← Lab 3
├── search_sort_students.py     ← Lab 4
├── fee_calculation.py          ← Lab 5
├── file_manager.py             ← Lab 6
├── directory_scanner.py        ← Lab 7
├── performance_analytics.py    ← Lab 8
└── README.md
```

---

## Course Outcomes Demonstrated

| CO | Description |
|----|-------------|
| CO1 | Fundamental Python concepts – variables, conditionals, loops |
| CO2 | Data structures – lists, tuples, dictionaries, sets |
| CO3 | Modular programming – functions, modules, integration |
| CO4 | File operations – read, write, seek, process records |
| CO5 | Python packages – NumPy, Pandas, Matplotlib, os module |
