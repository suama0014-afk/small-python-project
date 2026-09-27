import csv

def save_to_csv(filename:str,expenses_list:list[dict]) -> bool:
    try:
        with open(filename,'w',newline='') as file:
            header = ["date","category","amount","description"]
            writer = csv.DictWriter(file, fieldnames=header)

            writer.writeheader()
            writer.writerows(expenses_list)
            return True
    except FileNotFoundError:
        print(f"No scv file name {filename}")
        return False

def read_from_csv(filename:str) -> list[dict]:
    try:
        with open(filename,'r') as file:
            reader = csv.DictReader(file)

            return list(reader)
    except FileNotFoundError:
        print(f"No csv file name {filename}")
        return []
    except UnicodeDecodeError as e:
        print(f"Error reading file: {e}")
        return []