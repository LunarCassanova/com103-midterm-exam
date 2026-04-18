
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


print("\nExpense Categories:")
for i in range(5):  
    print(i + 1, ".", categories[i])
print("0. Skip")

total_spent = 0  

for entry in range(4):
    print("\nEntry", entry + 1)

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
        item = input("Enter item description: ")  

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

        total_spent = total_spent + amount


print("\n--- Weekly Report ---")
print("Name:", name)
print("Budget:", budget)
print("Total Spent:", total_spent)


if total_spent >= budget * 0.25:
    print("Status: High Expense! ! High Expense Alert!")
else:
    print("Status: Normal")