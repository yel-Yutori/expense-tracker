import csv
import matplotlib.pyplot as plt

totals = {}

try:
    with open("expenses.csv", encoding="utf-8-sig") as file:
        for row in csv.DictReader(file):
            category = row["category"]
            amount = float(row["amount"])
            totals[category] = totals.get(category, 0) + amount

    if not totals:
        print("沒有消費資料")
    else:
        plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
        plt.pie(totals.values(), labels=totals.keys(),
                autopct="%1.1f%%")
        plt.title("Expense Distribution")
        plt.savefig("pie_chart.png")
        plt.show()

except FileNotFoundError:
    print("找不到 expenses.csv")
except (ValueError, KeyError):
    print("資料格式錯誤")