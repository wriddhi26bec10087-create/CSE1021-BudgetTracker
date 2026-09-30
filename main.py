from storage import load_data
from tracker import *

MENU = """
=== Budget Tracker ===
1. Set budget
2. Add expense
3. View expenses
4. View summary
5. Exit
"""


def main():
    data =load_data()
    while True:
        print(MENU)
        choice= input("Choose an option (1-5): ").strip()
        if choice =="1":
            set_budget(data)
        elif choice == "2":
            add_expense(data)
        elif choice== "3":
            view_expenses(data)
        elif choice == "4":
            view_summary(data)
        elif choice== "5":
            print("bye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
