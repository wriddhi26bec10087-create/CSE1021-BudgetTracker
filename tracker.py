from storage import save_data


def set_budget(data):
    
    try:
        amount =float(input("Enter your budget amount: "))
        data["budget"] = amount
        save_data(data)
        print(f"Budget set to {amount:.2f}")
    except ValueError:
        print("Please enter a valid number.")


def add_expense(data):
    
    try:
        description = input("Expense description: ").strip()
        amount = float(input("Amount spent: "))
        category = input("Category (e.g. Food, Travel): ").strip() or "Uncategorized"
        data["expenses"].append({
            "description": description,
            "amount": amount,
            "category": category
        })
        save_data(data)
        print("Expense added.")
    except ValueError:
        print("Please enter a valid number.")


def view_expenses(data):
    while True:
    
        if not data["expenses"]:
            print("No expenses recorded yet.")
            return
        print("\n{:<20} {:<15} {:>10}".format("Description", "Category", "Amount"))
        print("-" * 47)
        for exp in data["expenses"]:
            print("{:<20} {:<15} {:>10.2f}".format(
                exp["description"][:20], exp["category"][:15], exp["amount"]
            ))
        yn = input("Go back? (Y/N): ").strip().upper()
        if yn == "Y":
            break
        elif yn == "N":
            pass
        else:
            print("Enter a valid option")
        




def view_summary(data):
    """Print total spent, budget, and remaining balance."""
    total_spent = sum(exp["amount"] for exp in data["expenses"])
    remaining = data["budget"] - total_spent
    print(f"\nBudget:    {data['budget']:.2f}")
    print(f"Spent:     {total_spent:.2f}")
    print(f"Remaining: {remaining:.2f}")
    if remaining < 0:
        print("Warning: You have exceeded your budget!")
