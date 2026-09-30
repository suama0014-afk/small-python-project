import csv
import logging

logging.basicConfig(
                    filename='app.log',
                    level= logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def save_to_csv(filename:str,expenses_list:list[dict]) -> bool:
    try:
        with open(filename,'w',newline='') as file:
            header = ["date","category","amount","description"]
            writer = csv.DictWriter(file, fieldnames=header)

            writer.writeheader()
            writer.writerows(expenses_list)
            return True
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        return False

def read_from_csv(filename:str) -> list[dict]:
    try:
        with open(filename,'r') as file:
            reader = csv.DictReader(file)

            return list(reader)
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        return []
    except UnicodeDecodeError :
        logging.error(f"Reading file failed: {filename}")
        return []