import matplotlib.pyplot as plt

def add_transaction():
    ammount = float(input("Enter ammount: "))
    if type(ammount) != float:
        print("Invalid ammount")
        return 0
    category = input("Enter category: ")
    date = [int(i) for i in input("Enter date separated by a space: ").split()]
    if len(date) != 3:
        print("Invalid date")
        return 0
    if type(date[0]) != int or type(date[1]) != int or type(date[2]) != int:
        print("Invalid date")
        return 0
    str_date = "-".join([str(i) for i in date])
    description = input("Enter description: ")
    transaction = {"ammount": ammount, "category": category, "date": str_date, "description": description }
    with open("transaction.txt", "r") as f:
        f = open("transaction.txt", "a")
        f.write(f"{transaction}\n")
        f.close()

def analyze_transactions():
    monthly_totals = {}
    with open("transaction.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            transaction = eval(line)
            date = transaction["date"].split('-')
            month = date[1]
            if month not in monthly_totals:
                monthly_totals[month] = 0
            monthly_totals[month] += transaction["ammount"]
    for month, total in monthly_totals.items():
        print(f"Total for month {month}: {total}")
    f.close()

    category_totals = {}
    with open("transaction.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            transaction = eval(line)
            category = transaction["category"]
            if category not in category_totals:
                category_totals[category] = 0
            category_totals[category] += transaction["ammount"]
    for category, total in category_totals.items():
        print(f"Total for category {category}: {total}")
    f.close()

def matplotlib_transactions():
    month = input("Enter month: ")
    transaction_ammount = []
    day_transaction = []
    with open("transaction.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            transaction = eval(line)
            day = transaction["date"].split('-')[0]
            date = transaction["date"].split('-')
            if date[1] == month:
                transaction_ammount.append(transaction["ammount"])
                day_transaction.append(day)
        f.close()

    category_ammount = {}
    with open("transaction.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            transaction = eval(line)
            category = transaction["category"]
            if transaction["date"].split('-')[1] == month:
                if category not in category_ammount:
                    category_ammount[category] = 0
                category_ammount[category] += transaction["ammount"]

    fig, ax = plt.subplots(ncols=2, figsize=(10, 5))

    fig.suptitle(f"Transactions in {month}")

    ax[0].pie(category_ammount.values(), labels=category_ammount.keys())
    ax[1].plot(day_transaction, transaction_ammount)

    plt.show()
    
            
matplotlib_transactions()