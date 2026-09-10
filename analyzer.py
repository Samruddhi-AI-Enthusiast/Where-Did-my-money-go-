def analyze_expenses(expenses):
    total = sum(expenses.values())
    biggest_expense = max(expenses, key=expenses.get)

    return total, biggest_expense