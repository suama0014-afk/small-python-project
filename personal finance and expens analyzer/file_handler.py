import csv
import logging

FILENAME = "expenses.csv"
logging.basicConfig(
                    filename='app.log',
                    level= logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s - %(lineno)d',
                    datefmt='%Y-%m-%d %H:%M:%S')

class Expense:
    def __init__(self,date:str,category:str,amount:float,description:str) -> None:
        self.date = date   
        self.category = category
        self.amount = amount
        self.description = description

    def to_dict(self) -> dict:
        return {
                "date": self.date,
                "category": self.category,
                "amount": self.amount,
                "description": self.description
        }

    @classmethod
    def from_dict(cls,data:dict) -> "Expense":
        return cls(
            date = data.get("date",""),
            category = data.get("category",""),
            amount = float(data.get("amount",0)),
            description = data.get("description","")
        )

    def __repr__(self) -> str:
        return f"Expense(date='{self.date}',category='{self.category}',amount='{self.amount}')"


class FileHandler:
    @staticmethod
    def save_to_csv_file(filename, expenses_list:list[dict]) -> bool:
        try:
            with open (filename,'w',newline="") as file:
                header = ["date","category","amount","description"]
                writter = csv.DictWriter(file,fieldnames=header,)

                writter.writeheader()
                writter.writerows(expenses_list)
                return True
        except FileNotFoundError:
            logging.error(f"fila {filename} not found")
            return False
    @staticmethod
    def read_from_csv_file(filename) -> list[dict]:
        try:
            with open(filename,'r') as file:
                reader = csv.DictReader(file)

                expense_objects = [Expense.from_dict(row) for row in reader ]
                return expense_objects
        except FileNotFoundError:
            logging.error(f"file  {filename} not found!")
            return []
        except UnicodeDecodeError:
            logging.error(f"can not read {filename} file!")
            return []