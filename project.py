from datetime import datetime, date
from tabulate import tabulate
from colorama import Fore, Style

contents = []
header = ["#", "Task", "Due Date", "Days Left", "Urgency"]

def main():
    while True:
        print("Options:")
        print("1. Add Task")
        print("2. Check Task")
        print("3. View Checklist")
        print("4. Exit")

        choice = input("Choose (1-4): ")

        if choice == "1":
            task = input("Task: ")
            due = input("Due Date (YYYY/MM/DD): ")
            generate(task, due)
        elif choice == "2":
            task_number = input("Enter task number to check off: ")
            check(task_number)
        elif choice == "3":
            display_table()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def generate(task, due_date):
    due = datetime.strptime(due_date, "%Y/%m/%d").date()
    if due:
        current_date = date.today()
        remaining_days = (due - current_date).days

        if remaining_days < 0:
            urgency = Fore.RED + "Overdue" + Style.RESET_ALL
        elif remaining_days < 1:
            urgency = Fore.RED + "VERY URGENT" + Style.RESET_ALL
        elif remaining_days < 3:
            urgency = Fore.YELLOW + "URGENT" + Style.RESET_ALL
        elif remaining_days < 7:
            urgency = Fore.GREEN + "Due Soon" + Style.RESET_ALL
        else:
            urgency = Fore.BLUE + "Just Chill" + Style.RESET_ALL

        contents.append({"Task": task, "Due Date": due_date, "Days Left": remaining_days, "Urgency": urgency})

        sort()

        print("\nTask added successfully!")
        display_table()
    else:
        raise ValueError("Invalid choice. Please try again.")


def sort():
    contents.sort(key = lambda x: x["Days Left"])

def display_table():
    if contents:
        print("Checklist:")
        table = [[i + 1, content['Task'], content['Due Date'], content['Days Left'], content['Urgency']] for i, content in enumerate(contents)]
        print(tabulate(table, header, tablefmt = "grid"))
    else:
        print("Checklist is empty")


def check(number):
    try:
        task_index = int(number) - 1 #starts from 0
        if 0 <= task_index < len(contents):
            removed = contents.pop(task_index)
            print(f"{removed['Task']} has been removed.")
            display_table()

        else:
            print("Please enter a valid number")


    except:
        print("Please enter a valid task number")


if __name__ == "__main__":
    main()
