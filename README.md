# 💰 Smart Expense Tracker with Data Analytics

Beginner-level Python console mini project. Roz mareez expenses track karne ke saath
saath Pandas, NumPy, aur Matplotlib use karke data analyze aur visualize bhi karta hai.

## Features

| # | Feature | Library Used |
|---|---------|--------------|
| 1 | Add / View / Total expenses | Core Python + CSV |
| 2 | Category-wise spending breakdown | Pandas (`groupby`) |
| 3 | Statistics: mean, median, max, min, std dev | NumPy |
| 4 | Bar chart — category-wise spending | Matplotlib |
| 5 | Pie chart — spending share by category | Matplotlib |
| 6 | Line chart — monthly spending trend | Matplotlib |
| 7 | Auto-save/load from `expenses.csv` | Core Python |

## Tech Stack

- Python 3
- Pandas — data cleaning & grouping
- NumPy — numerical calculations
- Matplotlib — data visualization
- CSV — persistent storage (no database needed)

## How to Run

```bash
pip install -r requirements.txt
python expense_tracker.py
```

Menu se option (1-9) choose karein. Expenses `expenses.csv` mein automatically save
ho jayenge — jab dobara app chalayenge, purana data khud load ho jayega.

## Project Structure

```
expense-analytics-tracker/
├── expense_tracker.py   # main app (CRUD + analytics + charts)
├── requirements.txt      # dependencies
├── README.md              # this file
└── expenses.csv           # auto-created after first expense (not included)
```

## Sample Workflow

1. Option 1 se 8-10 dummy expenses add karein (different categories: Food, Travel,
   Bills, Shopping — 2-3 different months ki dates ke sath).
2. Option 4 se category-wise totals dekhein.
3. Option 5 se statistics (average, highest, lowest expense) dekhein.
4. Option 6, 7, 8 se charts generate karein — yeh screenshots resume/portfolio ke
   liye use kar sakte hain.

## Resume Bullet Points (copy-paste ready)

- Built a console-based **Expense Tracker** in Python with persistent CSV storage
  and CRUD operations (add, view, total).
- Integrated **Pandas** for category-wise expense aggregation using `groupby()`.
- Applied **NumPy** for statistical analysis (mean, median, standard deviation) of
  spending data.
- Created data visualizations (bar, pie, line charts) using **Matplotlib** to show
  spending patterns and monthly trends.
- Practiced clean code structure, error handling (invalid date/amount input), and
  file I/O in Python.

## Possible Next Steps (agar aage improve karna ho)

- SQLite database use karein CSV ki jagah
- Budget limit alerts add karein (agar category ka spending limit cross ho jaye)
- Streamlit se isko web app mein convert karein
- Export analytics report as PDF
