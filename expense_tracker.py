"""
Smart Expense Tracker with Data Analytics
------------------------------------------
Beginner-level console mini project.
Core CRUD: pure Python + CSV (jaisa pehle tha)
Analytics: Pandas + NumPy
Visualization: Matplotlib

Author: Rushna
"""

from datetime import datetime
import csv
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Script jahan bhi rakhi ho, expenses.csv hamesha usi folder mein banegi/use hogi
# (isse ek se zyada jagah files generate hone ka masla khatam ho jaata hai)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, "expenses.csv")

# Saare expenses store karne ke liye list
expenses = []


# ----------------------------------------------------
# FUNCTION: FILE SE PURANE EXPENSES LOAD KARO (agar file exist karti hai)
# ----------------------------------------------------
def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expense = {
                    "date": datetime.strptime(row["date"], "%d-%m-%Y").date(),
                    "category": row["category"],
                    "description": row["description"],
                    "amount": float(row["amount"])
                }
                expenses.append(expense)
        print(f" 📂 {len(expenses)} purane expenses file se load ho gaye.")


# ----------------------------------------------------
# FUNCTION: SAARE EXPENSES FILE MEIN SAVE KARO
# ----------------------------------------------------
def save_expenses():
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "category", "description", "amount"])

        for e in expenses:
            writer.writerow([
                e["date"].strftime("%d-%m-%Y"),
                e["category"],
                e["description"],
                e["amount"]
            ])


# ----------------------------------------------------
# HELPER: CSV KO PANDAS DATAFRAME MEIN LOAD KARO (analytics ke liye)
# ----------------------------------------------------
def get_dataframe():
    if not os.path.exists(FILENAME) or len(expenses) == 0:
        print("\n ⚠️  Koi expense data nahi mila. Pehle kuch expenses add karein.")
        return None

    df = pd.read_csv(FILENAME)
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
    return df


# ----------------------------------------------------
# ANALYTICS 1: CATEGORY-WISE TOTAL (PANDAS groupby)
# ----------------------------------------------------
def category_wise_analysis():
    df = get_dataframe()
    if df is None:
        return

    print("\n--- 📊 CATEGORY-WISE SPENDING (Pandas groupby) ---")
    summary = df.groupby("category")["amount"].sum().sort_values(ascending=False)

    for category, total in summary.items():
        print(f"  {category:<15} : Rs. {total:.2f}")


# ----------------------------------------------------
# ANALYTICS 2: STATISTICS (NUMPY)
# ----------------------------------------------------
def show_statistics():
    df = get_dataframe()
    if df is None:
        return

    amounts = np.array(df["amount"])

    print("\n--- 🔢 SPENDING STATISTICS (NumPy) ---")
    print(f"  Total Spending   : Rs. {np.sum(amounts):.2f}")
    print(f"  Average Expense  : Rs. {np.mean(amounts):.2f}")
    print(f"  Median Expense   : Rs. {np.median(amounts):.2f}")
    print(f"  Highest Expense  : Rs. {np.max(amounts):.2f}")
    print(f"  Lowest Expense   : Rs. {np.min(amounts):.2f}")
    print(f"  Std. Deviation   : Rs. {np.std(amounts):.2f}")


# ----------------------------------------------------
# CHART 1: BAR CHART - CATEGORY-WISE SPENDING
# ----------------------------------------------------
def show_bar_chart():
    df = get_dataframe()
    if df is None:
        return

    summary = df.groupby("category")["amount"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    plt.bar(summary.index, summary.values, color="#4C72B0")
    plt.title("Category-wise Spending")
    plt.xlabel("Category")
    plt.ylabel("Amount (Rs.)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


# ----------------------------------------------------
# CHART 2: PIE CHART - SPENDING SHARE BY CATEGORY
# ----------------------------------------------------
def show_pie_chart():
    df = get_dataframe()
    if df is None:
        return

    summary = df.groupby("category")["amount"].sum()

    plt.figure(figsize=(6, 6))
    plt.pie(summary.values, labels=summary.index, autopct="%1.1f%%", startangle=90)
    plt.title("Spending Share by Category")
    plt.tight_layout()
    plt.show()


# ----------------------------------------------------
# CHART 3: LINE CHART - MONTHLY SPENDING TREND
# ----------------------------------------------------
def show_monthly_trend():
    df = get_dataframe()
    if df is None:
        return

    df["month"] = df["date"].dt.to_period("M").astype(str)
    monthly = df.groupby("month")["amount"].sum()

    plt.figure(figsize=(8, 5))
    plt.plot(monthly.index, monthly.values, marker="o", color="#DD8452")
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount (Rs.)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


# ----------------------------------------------------
# PROGRAM START: PURANE EXPENSES LOAD KARO
# ----------------------------------------------------
load_expenses()


while True:

    print("\n==================================")
    print("   💰 SMART EXPENSE TRACKER")
    print("==================================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Category-wise Analysis (Pandas)")
    print("5. Spending Statistics (NumPy)")
    print("6. Bar Chart - Category Spending")
    print("7. Pie Chart - Spending Share")
    print("8. Line Chart - Monthly Trend")
    print("9. Exit")
    print("==================================")

    choice = input(" 👉 Enter your choice (1-9): ")


    # OPTION 1: ADD EXPENSE
    if choice == "1":

        print("\n--- ADD NEW EXPENSE ---")

        date_input = input(" 📅 Enter date (DD-MM-YYYY): ")

        try:
            date = datetime.strptime(date_input, "%d-%m-%Y").date()

        except ValueError:
            print(" ❌ Invalid date! Please enter date like 22-09-2026.")
            continue

        category = input("  🏷️  Enter category (Food, Travel, Clothes or anything?): ")

        description = input(" 📝 Enter description: ")

        try:
            amount = float(input("  💵  Enter amount : "))
        except ValueError:
            print(" ❌ Invalid amount! Please enter a number.")
            continue

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        save_expenses()

        print(" ✅ Expense added and saved to file successfully!")


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


    # OPTION 4: CATEGORY-WISE ANALYSIS (PANDAS)
    elif choice == "4":
        category_wise_analysis()


    # OPTION 5: STATISTICS (NUMPY)
    elif choice == "5":
        show_statistics()


    # OPTION 6: BAR CHART
    elif choice == "6":
        show_bar_chart()


    # OPTION 7: PIE CHART
    elif choice == "7":
        show_pie_chart()


    # OPTION 8: LINE CHART - MONTHLY TREND
    elif choice == "8":
        show_monthly_trend()


    # OPTION 9: EXIT
    elif choice == "9":

        save_expenses()

        print("\n ✅ Thank you for using Smart Expense Tracker!")
        print(" 💾 All expenses saved to expenses.csv")
        print("💸 Keep tracking your expenses! 😊")

        break


    # INVALID CHOICE
    else:
        print("\n ❌ Invalid choice! Please enter 1-9.")
