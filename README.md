# 💰 Smart Expense Tracker with Data Analytics

A beginner-level Python console mini project for tracking daily expenses, combined
with Pandas, NumPy, and Matplotlib to analyze and visualize spending data.

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

Choose an option (1-9) from the menu. Expenses are automatically saved to
`expenses.csv` — the next time you run the app, your existing data loads
automatically.

## Project Structure

```
expense-analytics-tracker/
├── expense_tracker.py   # main app (CRUD + analytics + charts)
├── requirements.txt      # dependencies
├── README.md              # this file
└── expenses.csv           # auto-created after first expense (not included)
```

## Sample Workflow

1. Use option 1 to add 8-10 sample expenses across different categories (Food,
   Travel, Bills, Shopping) and a few different months.
2. Use option 4 to view category-wise totals.
3. Use option 5 to view statistics (average, highest, lowest expense).
4. Use options 6, 7, and 8 to generate charts — these can be captured as
   screenshots for your resume or portfolio.

pending exceeds a set limit)
- Convert to a web app using Streamlit
- Export the analytics report as a PDF
