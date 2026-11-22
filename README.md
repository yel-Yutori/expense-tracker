# expense-tracker
Expense tracking tool - SE Assignment 1

## Member B－支出圓餅圖視覺化功能

### 功能介紹

本功能使用 Python 的 Matplotlib 套件，讀取 Member A 儲存於 `expenses.csv` 的記帳資料，依照支出類別統計金額，並產生圓餅圖。

功能包含：

1. 讀取 `expenses.csv` 記帳資料。
2. 依照支出類別加總金額。
3. 自動計算各類別的支出百分比。
4. 支援中文類別顯示。
5. 將圓餅圖儲存為 `pie_chart.png`。

### 安裝套件

在 Terminal 輸入：

```bash
pip install matplotlib
```

### 執行方式

確認 `expenses.csv` 與 `plot_pie.py` 位於同一個資料夾。

在 Terminal 輸入：

```bash
python plot_pie.py
```

執行後會顯示各類別的支出圓餅圖，並產生 `pie_chart.png` 圖片。

### 圓餅圖範例

![支出圓餅圖]