import datetime

from analytics import Analyzer
from file_handler import FileHandler,Expense

FILENAME = 'expenses.csv'
# fileHandle = FileHandler()
analyzer = Analyzer()
expenses_list = FileHandler.read_from_csv_file(FILENAME)

class ValidateData:
    @staticmethod
    def dict_keys(expens:dict) -> tuple[bool,str]:
        REQUIRED_KEYS = {"date","category","amount","description"}
        if not REQUIRED_KEYS.issubset(expens.keys()):
            missing = REQUIRED_KEYS - set(expens.keys())
            return False ,f"missing keys:{missing}"
        return True,""

    @staticmethod
    def validate_amount(expens:dict) -> tuple[bool,str]:
        try:
            amount = float(expens['amount'])
            if amount <= 0:
                return False,"Amount must be greater than 0"
            return True, ""
        except ValueError as e:
            return False, e
       
    @staticmethod
    def validate_category(expens:dict) -> tuple[bool,str]:
        if not str(expens['category']).strip():
            return False, "category can not be empty"
        return True,""
        
    @staticmethod
    def validate_date(expens:dict) -> tuple[bool,str]:
        date_str = expens['date']
        pattern = "%Y-%m-%d"
        try:
            datetime.datetime.strptime(date_str,pattern)  # noqa: DTZ007
            return True,""
        except ValueError as e:
            return False,e

def validate(expens:dict) -> tuple[bool,str]:
    errors = []

    is_valide_keys,msg = ValidateData.dict_keys(expens)
    if not is_valide_keys:
        errors.append(msg)
        return False,errors

    checks = [
            ValidateData.validate_amount(expens),
            ValidateData.validate_date(expens),
            ValidateData.validate_category(expens)
    ]

    for is_valide, msg in checks:
        if not is_valide:
            errors.append(msg)

    return len(errors) == 0, errors
    
def add_expenses(expenses_list:list[dict]) -> bool:
    date = datetime.datetime.now().strftime("%Y-%m-%d")  # noqa: DTZ005
    category = input("Enter the category of expenses: ").strip()
    while True:
        try:
            amount = float(input("Enter the amount: ").strip())
            break
        except ValueError:
            print("Amount must be number. Try again")
        
    description = input("Enter the description of category: ")

    expense_data = Expense(date=date,category=category,amount=amount,description=description)
    data = expense_data.to_dict()
    is_valide,message = validate(data)
    if is_valide:
        expenses_list.append(data)
        FileHandler.save_to_csv_file(FILENAME,expenses_list)
        print("Expenses added successfully!")
    else:
        print(message)
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
            filterd = analyzer.filter_by_category(expenses_list,category)
            if not filterd:
                print(f"Category {category} not found!")
            else:
                for line in filterd:
                    print(f"Date:{line['date']}|Category:{line['category']}|Amount:{line['amount']}|description:{line['description']}")
        elif ch == "3": 
            print(f"Total amount: {analyzer.calculate_total(expenses_list)}")
        elif ch == "4": 
            summarized_category = analyzer.summarized_by_category(expenses_list)
            print(summarized_category)
        elif ch == "5": break

if __name__ == "__main__":
    main()