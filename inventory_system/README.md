# Inventory System

A command-line inventory manager written in Python. Add products, update their quantity or price, view the full stock list, and calculate the total value of the inventory. Data is saved to a JSON file, so it is still there the next time you run the program.

## Features

- Add a product with its name, quantity, and price
- Update the quantity or the price of an existing product
- Calculate the total inventory value (sum of `quantity x price` for all products)
- Display all products
- Automatic saving to `inventory.json` after every change
- Safe file reading: a missing or empty data file is handled without crashing

## Tech Stack

- Python 3 (standard library only: `json`, `pathlib`)

## Getting Started

**Requirements:** Python 3.9 or newer (tested with Python 3.12)

```bash
git clone https://github.com/suama0014-afk/small-python-project.git
cd small-python-project/inventory_system
python inventory_management.py
```

> On some systems the command is `python3` instead of `python`.

The program reads and writes `inventory.json` in the same folder as the script, so it works no matter where you launch it from. The repository includes a sample `inventory.json` so you can try it right away.

## Usage

```
--- system tracker ---
1. Add product
2. update product
3. calculate total value
4. display inventory
5. Exit
```

Example (using the included sample data):

| Menu choice | Input | Result |
|-------------|-------|--------|
| `1` Add product | name `mouse`, quantity `10`, price `20` | Product is added and saved |
| `3` Calculate total value | none | `2750` |
| `2` Update product | name `mouse`, then `1` (quantity), new value `15` | Quantity is updated and saved |
| `4` Display inventory | none | `Product:mouse \| Quantity:15 \| Price:20` (and the other products) |

## Data Format

Products are stored as JSON, using the product name as the key:

```json
{
    "phone": {
        "Quantity": 2,
        "Price": 150
    },
    "laptop": {
        "Quantity": 1,
        "Price": 300
    }
}
```

## Project Structure

```
inventory_system/
├── inventory_management.py   # Program logic and menu
└── inventory.json            # Saved inventory data
```

## Limitations and Future Improvements

- Adding a product with a name that already exists replaces the old entry.
- Quantity and price are entered as whole numbers. Decimal prices and clearer messages for invalid input would improve it.
- There is no option to delete a product yet.
- Product names are case-sensitive (`Phone` and `phone` are different products).

## Author

Osama Mohammed Abdalazim Siyd
