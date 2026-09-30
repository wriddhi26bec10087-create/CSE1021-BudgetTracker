# Budget Tracker

A simple,  Budget Tracker application written in Python. This program allows users to set a total budget,categorized expenses, view formatted expense history, and save data.

---

## Project Structure

```text
budget_tracker/
│
├── data/
│   └── expenses.json      # Persistent storage for budget & expense entries
├── main.py                # Main application entry point 
├── storage.py             # Functions to load and save data from/to JSON
└── tracker.py             # Core tracker operations (set budget, add expense, view expenses)
```

---

## Features

- **Set Budget**: Set and update your total budget allowance
- **Add Expense**: Log expenses with description, amount, and custom categories (e.g., Food, Travel, Uncategorized)
- **View Expenses**: Display recorded expenses in a table layout
- **Persistent Storage**: Automatically saves all data to `data/expenses.json` so your entries persist across sessions.
- **Error Handling**: Handles invalid numerical inputs gracefully

---

## Getting Started

### Prerequisites

- **Python**: Make sure Python 3.11  is installed on system

To check if Python is installed, run:
```bash
python --version
# or
python3 --version
```

---

##  Installation & Setup

1. **Clone or Download the Repository**
   Download the project folder

2. **Navigate to the Project Directory**
   Open your terminal/command prompt and navigate into the `budget_tracker` folder:
   ```bash
   cd path/to/budget_tracker
   ```

3. **Ensure Directory Setup**
   Ensure the `data/` folder exists in your project root so that JSON storage functions correctly.

---

##  Running the Application

Execute the following command in your terminal from the project directory:

```bash
python main.py
```
*(Use `python3 main.py` if `python` points to Python 2 on your system).*

---

##  Usage Guide

Upon launching the application, will be greeted with the main menu:

```text
--- Budget Tracker ---
1. Set budget
2. Add expense
3. View expenses
4. View summary
5. Exit
```

- Choose **1** to initialize or update your main budget amount.
- Choose **2** to enter individual expense details (description, cost, and category).
- Choose **3** to view all recorded expenses formatted neatly in tabular form.
- Choose **5** to close the program safely.

---
