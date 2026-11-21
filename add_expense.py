import csv
import os

file = "expenses.csv"
new_file = not os.path.exists(file) or os.path.getsize(file) == 0

with open(file, "a", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)

    if new_file:
        writer.writerow(["date", "amount", "category", "notes"])

    while True:
        date = input("Date (YYYY-MM-DD): ")
        amount = input("Amount: ")
        category = input("Category: ")
        notes = input("Notes (optional): ")

        writer.writerow([date, amount, category, notes])
        f.flush()
        print("Expense saved!")

        again = input("Add another expense? (y/n): ")
        if again.lower() != "y":
            break