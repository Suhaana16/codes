# calendar_task.py
# AI/ML Task Week 1

import calendar
import datetime

# Part 1: Using calendar module
def print_calendar_with_calendar_module():
    print("\n== Part 1: Calendar using calendar module ==")
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))
    print()
    print(calendar.month(year, month))

# Part 2: Using datetime only
def print_calendar_with_datetime_module():
    print("\n== Part 2: Calendar using datetime module only ==")
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))

    first_day = datetime.date(year, month, 1)
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)

    num_days = (next_month - first_day).days
    print("Mo Tu We Th Fr Sa Su")

    start_weekday = first_day.weekday()
    print("   " * start_weekday, end="")

    for day in range(1, num_days + 1):
        print(f"{day:2} ", end="")
        if (start_weekday + day) % 7 == 0:
            print()
    print()

# Main execution
if _name_ == "_main_":
    print_calendar_with_calendar_module()
    print_calendar_with_datetime_module()

"""
Sample Output:

Enter month (1-12): 6
Enter year: 2025

== Part 1: Calendar using calendar module ==
     June 2025
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30

== Part 2: Calendar using datetime module only ==
Mo Tu We Th Fr Sa Su
                   1 
 2  3  4  5  6  7  8 
 9 10 11 12 13 14 15 
16 17 18 19 20 21 22 
23 24 25 26 27 28 29 
30 
"""

