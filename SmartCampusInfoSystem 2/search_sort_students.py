# -*- coding: utf-8 -*-
# ============================================================
# Lab 4: Sorting and Searching of Student IDs
# Smart Campus Information System
# ============================================================

def sort_and_search():
    """Sort student IDs using Bubble Sort and Selection Sort, then search."""
    print("\n" + "=" * 45)
    print("      SORTING AND SEARCHING STUDENT IDs")
    print("=" * 45)

    # Step 1: Store Student IDs
    student_ids = [105, 102, 110, 108, 101, 115]
    print(f"\nOriginal IDs: {student_ids}")

    # ── Step 2: Bubble Sort ──────────────────────────────────
    ids_bubble = student_ids.copy()
    n = len(ids_bubble)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ids_bubble[j] > ids_bubble[j + 1]:
                ids_bubble[j], ids_bubble[j + 1] = ids_bubble[j + 1], ids_bubble[j]
    print(f"Sorted IDs (Bubble Sort)   : {ids_bubble}")

    # ── Step 3: Selection Sort ───────────────────────────────
    ids_selection = student_ids.copy()
    n = len(ids_selection)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if ids_selection[j] < ids_selection[min_index]:
                min_index = j
        ids_selection[i], ids_selection[min_index] = ids_selection[min_index], ids_selection[i]
    print(f"Sorted IDs (Selection Sort): {ids_selection}")

    # Use bubble-sorted list for searching
    sorted_ids = ids_bubble

    # ── Step 4: Linear Search ────────────────────────────────
    target = int(input("\nEnter Student ID to search: "))
    found_index = -1
    for i in range(len(sorted_ids)):
        if sorted_ids[i] == target:
            found_index = i
            break

    if found_index != -1:
        print(f"Linear Search : ID {target} found at index {found_index}")
    else:
        print(f"Linear Search : ID {target} not found")

    # ── Step 5: Binary Search ────────────────────────────────
    low, high, found_index = 0, len(sorted_ids) - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if sorted_ids[mid] == target:
            found_index = mid
            break
        elif sorted_ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if found_index != -1:
        print(f"Binary Search : ID {target} found at index {found_index}")
    else:
        print(f"Binary Search : ID {target} not found")

    return sorted_ids


if __name__ == "__main__":
    sort_and_search()
