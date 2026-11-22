import csv
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

totals = {}

try:
    with open("expenses.csv", "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            category = row["category"]
            amount = float(row["amount"])
            totals[category] = totals.get(category, 0) + amount

    if totals:
        plt.pie(
            totals.values(),
            labels=totals.keys(),
            autopct="%1.1f%%"
        )
        plt.title("Expense Distribution")
        plt.savefig("pie_chart.png")
        plt.show()
    else:
        print("No expense data found.")

except FileNotFoundError:
    print("Cannot find expenses.csv")
except (ValueError, KeyError):
    print("Expense data format error")