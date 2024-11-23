import pandas as pd
from datetime import datetime
import csv

# datetime EVM
expenses_df = pd.DataFrame(columns=["Date", "Description", "Amount"])

#input expense (1.Add Expense)
def add_expense():
    description = input("Enter description of expense: ")
    amount = float(input("Enter amount: "))
    date_input = input("Enter date of expense (YYYY-MM-DD): ")
    #One More Funtipon Enter to be time NOW
    if date_input == '':
        date_input = datetime.now()
    else:
        date_input = datetime.strptime(date_input,"%Y-%m-%d")

    new_expense = pd.DataFrame([[date_input, description, amount]], columns=["Date", "Description", "Amount"])
    global expenses_df
    expenses_df = pd.concat([expenses_df, new_expense], ignore_index=True)
    print("Expense added successfully!")

    # Save to CSV
    expenses_df.to_csv('expenses.csv', index=False)
    print("Expenses saved to expenses.csv")

#Check Expenses (2.Get Expenses)
def get_expenses():
    global expenses_df
    if expenses_df.empty:
        print("No expenses recorded.")
    else:
        print("Expenses:")
        print(expenses_df)

#Main (3.Exit)
def main():
    while True:
        print("1. Add Expense")
        print("2. Get Expenses")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            get_expenses()
        elif choice == "3":
            del_expenses()
        elif choice =="4":
            print("Bye Bye")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
