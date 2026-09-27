from file_handler import read_from_csv,save_to_csv
from analytics import filter_by_category,calculate_total,summarized_by_category
import datetime
FILENAME = 'expenses.csv'

expenses_list = read_from_csv(FILENAME)

def add_expenses(expenses_list:list[dict]) -> bool:
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    category = input("Enter the category of expenses: ").strip()
    while True:
        try:
            amount = int(input("Enter the amount: ").strip())
            break
        except ValueError:
            print("Amount must be integer. Try again")
        
    description = input("Enter the description of category: ")

    data = {"date":date,"category":category,"amount":amount,"description":description}
    expenses_list.append(data)
    save_to_csv(FILENAME,expenses_list)
    print("Expenses added successfully!")
    return True

def main():
    while True:
        print("--- system tracker ---")
        ch = input("1. Add Expenses\n" \
                   "2. Filter By Category\n" \
                   "3. Calculate Total Expenses\n" \
                   "4. Summarized By Category\n" \
                   "5. Exit\n"
                   "Enter (1/5): ").strip()
        if ch == "1": add_expenses(expenses_list)
        elif ch == "2":
            category = input("Enter category: ").strip()
            filterd = filter_by_category(expenses_list,category)
            if not filterd:
                print(f"Category {category} not found!")
            else:
                for line in filterd:
                    print(f"Date:{line['date']}|Category:{line['category']}|Amount:{line['amount']}|description:{line['description']}")
        elif ch == "3": 
            print(f"Total amount: {calculate_total(expenses_list)}")
        elif ch == "4": 
            summarized_category = summarized_by_category(expenses_list)
            print(summarized_category)
        elif ch == "5": break

if __name__ == "__main__":
    main()