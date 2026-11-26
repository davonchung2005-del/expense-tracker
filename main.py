from datetime import date
descriptions = []
amounts = []
categories = []
dates = []

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

with open("expenses.csv", "w") as file:
    for i in range(len(descriptions)):
        file.write(f"{descriptions[i]},{categories[i]},{amounts[i]},{dates[i]}\n")

totals = {}
for category in categories:
    if not category in totals:
        totals[category] = 0

for i in range(len(categories)):
    totals[categories[i]] += amounts[i]

print("Totals per category:")
for category in totals:
    print(f"{category}: {totals[category]:.2f} €")

print("Your expenses:")
for i in range(len(descriptions)):
    print(f"{dates[i]} {descriptions[i]} ({categories[i]}): {amounts[i]:.2f} €")
     
print(f"Total: {sum(amounts):.2f} €")



