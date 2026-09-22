from datetime import datetime

# Saare expenses store karne ke liye list
expenses = []


while True:

    print("\n==============================")
    print("       💰 EXPENSE TRACKER")
    print("==============================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")
    print("==============================")

    choice = input(" 👉 Enter your choice (1-4): ")


    # OPTION 1: ADD EXPENSE
    if choice == "1":

        print("\n--- ADD NEW EXPENSE ---")

        # Proper date input
        date_input = input(" 📅 Enter date (DD-MM-YYYY): ")

        try:
            date = datetime.strptime(date_input, "%d-%m-%Y").date()

        except ValueError:
            print(" ❌ Invalid date! Please enter date like 22-09-2026.")
            continue


        category = input("  🏷️  Enter category (Food, Travel, Clothes or anything?): ")

        description = input(" 📝 Enter description: ")

        amount = float(input("  💵  Enter amount : "))


        # Expense dictionary
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }


        # List mein expense add
        expenses.append(expense)

        print(" ✅ Expense added successfully!")


    # OPTION 2: VIEW ALL EXPENSES
    elif choice == "2":

        if len(expenses) == 0:

            print("\nNo expenses added yet.")

        else:

            print("\n--- ALL EXPENSES ---")

            count = 1

            for e in expenses:

                print(
                    f"{count}. "
                    f"Date: {e['date'].strftime('%d-%m-%Y')} | "
                    f"Category: {e['category']} | "
                    f"Description: {e['description']} | "
                    f"Amount: Rs. {e['amount']}"
                )

                count = count + 1


    # OPTION 3: TOTAL SPENDING
    elif choice == "3":

        total = 0

        for e in expenses:

            total = total + e["amount"]

        print(f"\nTotal Spending: Rs. {total}")


    # OPTION 4: EXIT
    elif choice == "4":

        print("\n ✅ Thank you for using Expense Tracker!")
        print("💸 Keep tracking your expenses! 😊")


        break


    # INVALID CHOICE
    else:

        print("\n ❌ Invalid choice! Please enter 1, 2, 3, or 4.")