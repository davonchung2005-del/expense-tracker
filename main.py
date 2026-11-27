from datetime import date

#One list per piece of information; same index = same expense
descriptions = []
amounts = []
categories = []
dates = []

#Load saved expenses (skip if the file doesn't exist yet)
try:
    with open("expenses.csv", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            descriptions.append(parts[0])
            categories.append(parts[1])
            amounts.append(float(parts[2]))
            dates.append(parts[3])
except FileNotFoundError:
    pass

#Ask for new expenses until the user types "stop"
while True:
    description = input("What did you buy? ").lower().strip()
    if description == "stop":
        break
    category = input("Which category? ").lower().strip()
    amount = float(input("How much did it cost? "))
    descriptions.append(description)
    categories.append(category)
    amounts.append(amount)
    dates.append(str(date.today()))

#Save all expenses (overwrites the file)
with open("expenses.csv", "w") as file:
    for i in range(len(descriptions)):
        file.write(f"{descriptions[i]},{categories[i]},{amounts[i]},{dates[i]}\n")

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
    total = 0
    for i in range(len(dates)):
        if dates[i][0:7] == month:
            print(f"{dates[i]} {descriptions[i]} ({categories[i]}): {amounts[i]:.2f} €")
            total += amounts[i]
    print(f"Total: {total:.2f} €")



