import csv
import os
from datetime import datetime

FILE = "expenses.csv"
FIELDS = ["date", "amount", "category", "note"]

def save_expense(date, amount, category, note=""):
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow({"date": date, "amount": amount,
                         "category": category, "note": note})

def ask_date():
    while True:
        s = input("日期 (YYYY-MM-DD，直接 Enter 用今天): ").strip()
        if not s:
            return datetime.today().strftime("%Y-%m-%d")
        try:
            datetime.strptime(s, "%Y-%m-%d")
            return s
        except ValueError:
            print("格式錯誤，請重新輸入")

def ask_amount():
    while True:
        try:
            value = float(input("金額: "))
            if value > 0:
                return value
            print("金額必須大於 0")
        except ValueError:
            print("請輸入數字")

def main():
    while True:
        date = ask_date()
        amount = ask_amount()
        category = input("類別 (例如 餐飲/交通/娛樂): ").strip() or "其他"
        note = input("備註 (可留空): ").strip()
        save_expense(date, amount, category, note)
        print("已儲存！")
        if input("繼續新增？(y/n): ").lower() != "y":
            break

if __name__ == "__main__":
    main()
