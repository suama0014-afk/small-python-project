# Personal Finance & Expense Analyzer

A command-line tool written in Python for tracking personal expenses. Record expenses with a category, amount, and description, then filter them by category, calculate the total, and see a spending summary per category. Expenses are saved to a CSV file, so your data is kept between runs.

## Features

- Add an expense (the date is filled in automatically with today's date)
- Input validation before saving:
  - all required fields are present (`date`, `category`, `amount`, `description`)
  - the amount is a number greater than 0
  - the date follows the `YYYY-MM-DD` format
  - the category is not empty
- Filter expenses by category (not case-sensitive)
- Calculate the total of all expenses
- Summarize spending by category
- Persistent storage in `expenses.csv`
- Error logging to `app.log` (for example when the CSV file is missing)
- Unit test with `pytest`

## Tech Stack

- Python 3 (standard library: `csv`, `logging`, `datetime`)
- `pytest` for testing (optional)

## Getting Started

**Requirements:** Python 3.9 or newer (tested with Python 3.12)

```bash
git clone https://github.com/suama0014-afk/small-python-project.git
cd "small-python-project/personal finance and expens analyzer"
python main.py
```

> Run the program from inside this folder, because `expenses.csv` and `app.log` are read and written in the current directory. On some systems the command is `python3` instead of `python`.

### Run the tests

```bash
pip install pytest
pytest test.py
```

## Usage

```
--- system tracker ---
1. Add Expenses
2. Filter By Category
3. Calculate Total Expenses
4. Summarized By Category
5. Exit
```

Example using the included `expenses.csv`:

| Menu choice | Input | Result |
|-------------|-------|--------|
| `1` Add Expenses | category `food`, amount `45.5`, description `lunch` | `Expenses added successfully!` |
| `2` Filter By Category | `car` | Lists every expense in the `car` category |
| `3` Calculate Total Expenses | none | The sum of all expenses |
| `4` Summarized By Category | none | `{'house': 330.0, 'car': 300.0, 'phone': 200.0, ...}` |

If the amount is 0 or negative, the expense is rejected with an error message and nothing is saved.

## Data Format

Expenses are stored in `expenses.csv`:

```csv
date,category,amount,description
2026-09-27,house,150,home needed form supermarket
2026-10-02,car,100.0,car ecupment
```

## Project Structure

```
personal finance and expens analyzer/
├── main.py            # Menu, user input, and data validation
├── file_handler.py    # Expense class and CSV reading/writing (with logging)
├── analytics.py       # Analyzer: filter, total, and summary by category
├── test.py            # Unit test for the validation logic
├── expenses.csv       # Saved expenses
└── app.log            # Error log
```

The code is split by responsibility:

- **`Expense`** represents a single expense and converts to and from a dictionary.
- **`FileHandler`** reads and writes the CSV file and logs errors.
- **`Analyzer`** contains the calculations (filter, total, summary).
- **`ValidateData`** checks each field before an expense is saved.

## Future Improvements

- Show amounts per month or per date range
- Edit and delete existing expenses
- Add more unit tests (analytics and file handling)
- Export a summary report

## Author

Osama Mohammed Abdalazim Siyd
