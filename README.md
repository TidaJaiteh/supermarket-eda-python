# 🛒 Supermarket Sales Analysis

A Python-based exploratory data analysis (EDA) project examining sales performance, customer behavior, and product trends across three supermarket branches.

\---

## 📌 Project Overview

This project analyzes transactional sales data from a supermarket chain with three branches — Giza, Alex, and Cairo. The goal is to uncover actionable business insights around branch performance, product line revenue, customer demographics, and satisfaction ratings using Python and data visualization libraries.

\---

## 🛠️ Tools \& Technologies

* **Python 3.13**
* **pandas** — data manipulation and analysis
* **matplotlib** — data visualization
* **seaborn** — statistical data visualization

\---

## 📂 Dataset

* **Source:** Kaggle — Supermarket Sales Dataset
* **Size:** 1,000 transactions, 17 columns
* **Period:** January – March (3 months)
* **Key columns:** Branch, City, Product Line, Sales, Gender, Payment, Rating, Date

\---

## 🔍 Analysis Performed

* **Data Cleaning** — checked for missing values, converted date formats, extracted Month and Day features
* **Branch Performance** — compared total revenue across all three branches
* **Product Line Revenue** — ranked product categories by total sales
* **Customer Demographics** — analyzed purchasing behavior by gender
* **Monthly Sales Trend** — tracked revenue changes across the 3-month period
* **Customer Satisfaction** — examined distribution of customer ratings

\---

## 📊 Visualizations

|Chart|Description|
|-|-|
|Bar Chart|Total Sales by Branch|
|Horizontal Bar Chart|Total Sales by Product Line|
|Count Plot|Number of Purchases by Gender|
|Line Chart|Monthly Sales Trend|
|Histogram + KDE|Customer Rating Distribution|

\---

## 💡 Key Business Insights

**1. Branch Performance**
Giza is the top performing branch with $110,568 in total sales, outperforming Alex ($106,200) and Cairo ($106,197) by approximately $4,000 each. The business should investigate what Giza is doing differently — whether it's location, staffing, or product availability — and replicate those practices across other branches.

**2. Product Line Revenue**
Food and Beverages led all product lines with $56,144 in sales while Health and Beauty was the weakest at $49,193 — a gap of nearly $7,000. The business should consider running targeted promotions on Health and Beauty products to test customer response before making any inventory decisions.

**3. Customer Demographics**
Female customers accounted for 571 out of 1,000 transactions (57%) compared to 429 male transactions. Marketing campaigns should be tailored toward female shoppers while also exploring strategies to attract and retain more male customers.

**4. Monthly Sales Trend**
January recorded the strongest sales at $116,291 while February was the weakest at $97,219 — a drop of nearly $19,000. This seasonal dip suggests the business should plan targeted promotions or discount campaigns in February to maintain revenue consistency throughout the quarter.

**5. Customer Satisfaction**
The average customer rating of 6.97 out of 10 indicates moderate satisfaction. There is clear room for improvement. The business should gather qualitative feedback to identify specific pain points — such as product quality, wait times, or customer service — and address them to push ratings above 8.0.

\---

## ▶️ How to Run

1. Clone this repository

```bash
git clone https://github.com/yourusername/supermarket-analysis.git
```

2. Install required libraries

```bash
pip install pandas matplotlib seaborn
```

3. Run the analysis

```bash
python analysis.py
```

\---

## 📁 Project Structure

```
supermarket-analysis/
├── SuperMarket-Analysis.csv        # Raw dataset
├── analysis.py                     # Main analysis script
├── check.py                        # Quick stats script
├── chart1\_sales\_by\_branch.png      # Branch sales chart
├── chart2\_sales\_by\_product.png     # Product line chart
├── chart3\_purchases\_by\_gender.png  # Gender purchases chart
├── chart4\_monthly\_trend.png        # Monthly trend chart
├── chart5\_rating\_distribution.png  # Rating distribution chart
└── README.md                       # Project documentation
```

\---

## 👤 Author

Tida Jaiteh
Information Systems Student
tida3858817@gmail.com
  [GitHub](https://github.com/TidaJaiteh)
  [Linkedin]( www.linkedin.com/in/tida-jaiteh-0092ba346)

