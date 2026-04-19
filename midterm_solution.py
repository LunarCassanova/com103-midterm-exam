name = input("Enter your name: ")
while name == "":
    print("error, invalid input")
    name = input("Enter your name: ")

budget_input = input("Enter your weekly budget: ")

valid = 1
for ch in budget_input:
    if ch < '0' or ch > '9':
        valid = 0

while valid == 0 or budget_input == "":
    print("error, invalid option")
    budget_input = input("Enter your weekly budget: ")
    
    valid = 1
    for ch in budget_input:
        if ch < '0' or ch > '9':
            valid = 0

budget = int(budget_input)

categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

entry_cat = [0, 0, 0, 0]
entry_item = ["", "", "", ""]
entry_amount = [0, 0, 0, 0]

print("\nExpense Categories:")
for i in range(5):
    print(i + 1, ".", categories[i])
print("0. Skip")

total_spent = 0

for i in range(4):
    print("\nEntry", i + 1)

    option_input = input("Choose category (0-5): ")

    valid = 1
    for ch in option_input:
        if ch < '0' or ch > '9':
            valid = 0

    while valid == 0 or option_input == "":
        print("error, invalid option")
        option_input = input("Choose category (0-5): ")
        
        valid = 1
        for ch in option_input:
            if ch < '0' or ch > '9':
                valid = 0

    option = int(option_input)

    while option < 0 or option > 5:
        print("error, invalid option")
        option_input = input("Choose category (0-5): ")
        
        valid = 1
        for ch in option_input:
            if ch < '0' or ch > '9':
                valid = 0

        while valid == 0 or option_input == "":
            print("error, invalid option")
            option_input = input("Choose category (0-5): ")
            
            valid = 1
            for ch in option_input:
                if ch < '0' or ch > '9':
                    valid = 0

        option = int(option_input)

    if option == 0:
        print("Skipped")
    else:
        entry_cat[i] = option - 1

        item = input("Enter item description: ")
        entry_item[i] = item

        amount_input = input("Enter amount spent: ")

        valid = 1
        for ch in amount_input:
            if ch < '0' or ch > '9':
                valid = 0

        while valid == 0 or amount_input == "":
            print("error, invalid option")
            amount_input = input("Enter amount spent: ")
            
            valid = 1
            for ch in amount_input:
                if ch < '0' or ch > '9':
                    valid = 0

        amount = int(amount_input)
        entry_amount[i] = amount

        total_spent = total_spent + amount

print("\n--- Weekly Report ---")
print("Name:", name)
print("Budget:", budget)

for i in range(4):
    print("Entry", i + 1)
    
    if entry_cat[i] == 0 and entry_item[i] == "" and entry_amount[i] == 0:
        print("Skipped")
    else:
        print("Category:", categories[entry_cat[i]])
        print("Item:", entry_item[i])
        print("Amount:", entry_amount[i])

print("Total Spent:", total_spent)

cash_left = budget - total_spent
print("Cash Left:", cash_left)

if total_spent >= budget * 0.25:
    print("Status: High Expense! ! High Expense Alert!")
else:
    print("Status: Normal")