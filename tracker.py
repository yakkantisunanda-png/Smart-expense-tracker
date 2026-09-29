import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Amount", "Reason", "Status"])

def add_expense():
    try:
        amount = float(input("\nAmount entha?: Rs."))
        reason = input("Enduku kharchu pettav?: ")

        status = "Safe"
        if amount >= 10000:
            print("HIGH ALERT: Chala pedda amount! Double check chey.")
            status = "High Risk"
        elif amount >= 4000:
            print(f"WARNING: Rs.{amount} - Fraud risk undochu.")
            status = "Medium Risk"

        with open(FILE_NAME, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([str(date.today()), amount, reason, status])
        print(f"Saved! Status: {status}")

    except ValueError:
        print("Amount ni number lo ivvu!")

def show_expenses():
    print("\n--- Nee Expenses ---")
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("Inka expenses levu.")

init_file()
while True:
    print("\n1. Add Expense\n2. Show All Expenses\n3. Exit")
    choice = input("Choose (1/2/3): ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        show_expenses()
    elif choice == '3':
        print("Bye!")
        break
    else:
        print("Wrong choice")
