# -*- coding: utf-8 -*-
# ============================================================
# Lab 5: Student Fee Calculation using Functions
# Smart Campus Information System
# ============================================================

def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    """
    Calculate total fee for a student.

    Parameters:
        tuition_fee        (float): Mandatory tuition fee
        hostel_fee         (float): Optional hostel fee (default 0)
        transportation_fee (float): Optional transportation fee (default 0)

    Returns:
        float: Total fee amount
    """
    total_fee = tuition_fee + hostel_fee + transportation_fee
    return total_fee


def fee_calculator_menu():
    """Interactive menu to calculate student fees."""
    print("\n" + "=" * 45)
    print("       STUDENT FEE CALCULATION SYSTEM")
    print("=" * 45)

    while True:
        try:
            tuition = float(input("\nEnter Tuition Fee (Rs.): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    hostel_input = input("Include Hostel Fee? (yes/no): ").strip().lower()
    hostel = 0
    if hostel_input == "yes":
        while True:
            try:
                hostel = float(input("Enter Hostel Fee (Rs.): "))
                break
            except ValueError:
                print("Invalid input.")

    transport_input = input("Include Transportation Fee? (yes/no): ").strip().lower()
    transport = 0
    if transport_input == "yes":
        while True:
            try:
                transport = float(input("Enter Transportation Fee (Rs.): "))
                break
            except ValueError:
                print("Invalid input.")

    total = calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)

    print("\n--- Fee Breakdown ---")
    print(f"  Tuition Fee        : Rs. {tuition:,.2f}")
    print(f"  Hostel Fee         : Rs. {hostel:,.2f}")
    print(f"  Transportation Fee : Rs. {transport:,.2f}")
    print(f"  {'─'*30}")
    print(f"  Total Fee          : Rs. {total:,.2f}")

    return total


def demo_fee_calculation():
    """Demonstrate fee calculation with three example cases."""
    print("\n=== Fee Calculation Demo ===")
    print("Case 1 - Only Tuition Fee:")
    print(f"  Total: Rs. {calculate_fee(50000):,.2f}")

    print("\nCase 2 - Tuition + Hostel:")
    print(f"  Total: Rs. {calculate_fee(50000, hostel_fee=30000):,.2f}")

    print("\nCase 3 - Tuition + Hostel + Transportation:")
    print(f"  Total: Rs. {calculate_fee(50000, hostel_fee=30000, transportation_fee=10000):,.2f}")


if __name__ == "__main__":
    demo_fee_calculation()
    fee_calculator_menu()
