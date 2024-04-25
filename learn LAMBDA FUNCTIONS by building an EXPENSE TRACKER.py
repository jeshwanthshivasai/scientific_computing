def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
def print_expense(expenses):
    for expense in expenses:
        print(f"Amount: {expense["amount"]}, Category: {expense["category"]}")
def total_expenses(expenses):
    lambda expense: expense["amount"]
test=lambda x: x*2
print(sum(map(test, [2,3, 5, 8])))        
expenses=[]