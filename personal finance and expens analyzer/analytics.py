from file_handler import Expense
class Analyzer:

    @staticmethod
    def show_expenses(expenses_list:list[object]) -> str:
        if not expenses_list:
            return ["no expense to show"]
        return "\n".join([str(expense) for expense in expenses_list]) 
            
        
    @staticmethod
    def filter_by_category(expenses_list:list[dict],category:str) -> list:
        return [expense for expense in [Expense.to_dict(row) for row in expenses_list] if expense['category'.lower()] == category.lower()]

    @staticmethod
    def calculate_total(expenses_list:list[dict]) -> float:
        data = [Expense.to_dict(row) for row in expenses_list]
        total = sum(float(expense['amount']) for expense in data)
        return float(total)
    
    @staticmethod
    def summarized_by_category(expenses_list:list[dict]) -> list:
        summarized = {}
        for category in expenses_list:
            expense_object = Expense.to_dict(category)
            name = expense_object['category']
            amount = float(expense_object['amount'])

            summarized[name] = summarized.get(name,0) + amount
        return summarized