def filter_by_category(expenses_list:list[dict],category:str) -> list:
    return [item for item in expenses_list if item['category'] == category]

def calculate_total(expenses_list:list[dict]) -> float:
    total = sum(int(expenses['amount']) for expenses in expenses_list)
    return total

def summarized_by_category(expenses_list:list[dict]) -> dict:
    category_total_amount = {}
    for cate in expenses_list:
        name = cate['category']
        amount = int(cate['amount'])

        category_total_amount[name] = category_total_amount.get(name,0) + amount

    return category_total_amount