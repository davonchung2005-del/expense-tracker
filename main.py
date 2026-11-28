from datetime import date 
from datetime import datetime
import csv

#One list per piece of information; same index = same expense
descriptions = []
amounts = []
categories = []
dates = []

#Load saved expenses (skip if the file doesn't exist yet)
try:
    with open("expenses.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for parts in reader:
            descriptions.append(parts[0])
            categories.append(parts[1])
            amounts.append(float(parts[2]))
            dates.append(parts[3])
except FileNotFoundError:
    pass

#Ask for new expenses until the user types "stop"
while True:
    description = input("What did you buy? (stop to quit)").lower().strip()
    if description == "stop":
        break
    category = input("Which category? ").lower().strip()

    while True:
        try:
            amount = float(input("How much did it cost? "))
            break
        except ValueError:
            print("The amount is invalid")
    descriptions.append(description)
    categories.append(category)
    amounts.append(amount)
    dates.append(str(date.today()))
    

#Save all expenses (overwrites the file)
with open("expenses.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for i in range(len(descriptions)):
        writer.writerow([descriptions[i], categories[i], amounts[i], dates[i]])

#Create a string total of 0 for each category
totals = {}
for category in categories:
    if not category in totals:
        totals[category] = 0

#Add each amount to its category
for i in range(len(categories)):
    totals[categories[i]] += amounts[i]

#Show totals per category
print("Totals per category:")
for category in totals:
    print(f"{category}: {totals[category]:.2f} €")

#Show every expense and the overall total
print("Your expenses:")
for i in range(len(descriptions)):
    print(f"{dates[i]} {descriptions[i]} ({categories[i]}): {amounts[i]:.2f} €")

print(f"Total: {sum(amounts):.2f} €")


#Monthly overview
while True:
    month = input("Enter a month (YYYY-MM) for a monthly overview or 'stop' to exit: ").strip().lower()
    if month == "stop":
        break
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("invalid")
        continue

    total = 0
    for i in range(len(dates)):
        if dates[i][0:7] == month:
            print(f"{dates[i]} {descriptions[i]} ({categories[i]}): {amounts[i]:.2f} €")
            total += amounts[i]
    print(f"Total: {total:.2f} €")



