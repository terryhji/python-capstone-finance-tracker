print("Welcome to the Personal Finance Tracker!")


def view_expenses(data):
    for category in data:
        print(f"Category: {category}")
        for exp in data[category]:
            print(f"- {exp[0]}: ${exp[1]}")

def view_summary(data):
    for category in data:
        print("Summary: ")
        sum = 0
        for exp in data[category]:
            sum += exp[1]
        print(f"{category}: ${sum}")

def menu_logic(data):
    try:
        print("What would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        mode = int(input("Choose an option: "))
    except TypeError:
        print("Invalid mode. Please enter a number.")
        return 0
    else:
        match mode:
            case 1:
                add_expense(data)
                return 0
            case 2:
                view_expenses(data)
                return 0
            case 3:
                view_summary(data)
                return 0
            case 4:
                print("Goodbye!")
                return 1


def add_expense(data):
    try:
        exp_disc = input("Input an expense description: ")
        category = input("Input a category: ")
        amt = round(float(input("Input amount: ")), 2)
    except TypeError:
        print("Invalid amount. Please enter a number.")
    else:
        if category in data:
            data[category].append((exp_disc, amt))
        else:
            data[category] = [(exp_disc, amt)]
        print("Expense added successfully.")
    return data

cond = 0
data = {}
while cond == 0:
    cond = menu_logic(data)