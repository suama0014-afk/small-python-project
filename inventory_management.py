import json
FILENAME = "inventory.json"

def read_file(filename:str) -> dict:
    try:
        with open(filename) as readfile:
            data = json.load(readfile)
            return data
    except FileNotFoundError:
        print(f"No file name {filename}")
        return {}
    except json.JSONDecodeError:
        print(f"file {filename} is empty")
        return {}

def write_on_file(filename:str,data:dict) -> bool:
    try:
        with open(filename,'w') as writefile:
            json.dump(data, writefile,indent=4)
            return True
    except FileNotFoundError:
        print(f"No file name {filename}")
        return False

def add_product(inventory:dict, name:str, Quantity:int, price:int) -> bool:
    inventory = read_file(FILENAME)
    inventory[name] = {"Quantity":Quantity,"Price":price}
    write_on_file(FILENAME,inventory)
    return True

def update_product(inventory:dict,name:str) -> bool:
    if name not in inventory:
        print("product not fount")
        return False
    if name in inventory:
        ch = input("1. update quantity\n" \
                   "2. update price: ").strip()
        if ch == "1":
            new_quantity = int(input("Enter the new quantity: ").strip())
            inventory[name]['Quantity'] = new_quantity
        elif ch == "2":
            new_price = int(input("Enter the new price: ").strip())
            inventory[name]['Price'] = new_price
    write_on_file(FILENAME,inventory)
    return True
    

def calculat_total_value(inventory:dict) -> float:
    total_value = 0
    if not inventory:
        return total_value 
    for item in inventory.values():
        total_value += item['Quantity'] * item['Price']
    return total_value

def display_inventory(inventory:dict) -> dict:
    if not inventory:
        print("No products in inventory")
        return
    for name, details in inventory.items():
        print(f"Product:{name} | Quantity:{details['Quantity']} | Price:{details['Price']}")
   

def main():
    inventory = read_file(FILENAME)
    while True:
        print("--- system tracker ---")
        print("1. Add product\n" \
            "2. update product\n" \
            "3. calculate total value\n" \
            "4. display inventory\n" \
            "5. Exit")
        choice = input("Enter (1/5): ").strip()
        if choice == "1":
            p_name = input("Enter product name: ").strip()
            p_quantity = int(input("Enter product quantity: ").strip())
            p_price = int(input("Enter producr price: ").strip())
            add_product(inventory,p_name,p_quantity,p_price)
        elif choice == "2":
            p_name = input("Enter product name: ").strip()
            update_product(inventory,p_name)
        elif choice == "3":
            total = calculat_total_value(inventory)
            print(total)
        elif choice == "4":
            display_inventory(inventory)
        elif choice == "5":break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()