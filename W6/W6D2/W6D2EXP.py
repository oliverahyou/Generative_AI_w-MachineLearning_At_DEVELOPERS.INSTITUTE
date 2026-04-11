# 🌟 Exercise 1 : Understanding Data Visualization
# Instructions
#     Explain why data visualization is important in data analysis.
# Data visualization is crucial in data analysis because it allows us to represent complex data in a visual format that is easier to understand and interpret. 
# It helps to identify patterns in the data that may not be immediately obvious from numbers alone. 
# Visualization also facilitate communication of insights and findings to a broader audience, making it easier for stakeholders to grasp the significance of the data and make informed decisions based on it.
#     Describe the purpose of a line graph in data visualization.
#  Line plots are used to display quantitative values over a continuous interval.

# 🌟 Exercise 2 : Creating a Line Plot for Temperature Variation
# Instructions
#     Create a simple line plot using Matplotlib that represents the temperature variations over a week.
#     Use a list of temperature values for each day of the week (e.g., [72, 74, 76, 80, 82, 78, 75]) and label the x-axis as “Day” and the y-axis as “Temperature (°F)”.
import matplotlib as plt
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [72, 74, 76, 80, 82, 78, 75]
plt.title('Temperature Variations Over a Week')
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.plot(days, temperatures)
plt.show()
# 🌟 Exercise 3 : Visualizing Monthly Sales with a Bar Chart
# Instructions
#     Generate a bar chart using Matplotlib to visualize the monthly sales data for a retail store.
#     Create a list of sales values for each month (e.g., [5000, 5500, 6200, 7000, 7500]) and label the x-axis as “Month” and the y-axis as “Sales Amount ($)”.
months = ['January', 'February', 'March', 'April', 'May']
sales = [5000, 5500, 6200, 7000, 7500]
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales Amount ($)')
plt.bar(months, sales)
plt.show()
# 🌟 Exercise 4 : Data Visualisation
# Instructions
# Using the dataset: sales_data.csv
#     Calculate the total quantity of products sold by the company.
import pandas as pd
df = pd.read_csv("sales_data.csv")
print(df.head())
total_quantity = df["quantity"].sum()
print("Total Quantity of products sold:", total_quantity)
#Total Quantity of products sold: 5360.0
#     Identify the category that had the highest revenue and calculate how much revenue it generated.
df = pd.read_csv("sales_data.csv")
category_revenue = df.groupby("category")["revenue"].sum()
top_category = category_revenue.idxmax()
top_revenue = category_revenue.max()
print(f"Highest Revenue Category: {top_category} with a top revenue of ${top_revenue}")
plt.figure()
category_revenue.plot(kind='bar')
plt.xlabel("Category")
plt.ylabel("Total Revenue ($)")
plt.title("Revenue by Category")
plt.show()
#Electronics had the highest revenue with a top revenue of $15000
#     Determine the average revenue per sale in the dataset.
df = pd.read_csv('sales_data.csv')
total_revenue = df['revenue'].sum()
total_quantity = df['quantity'].sum()
avg_revenue_per_sale = total_revenue / total_quantity
print(f"Average Revenue per Sale: ${avg_revenue_per_sale:.2f}")
# Average Revenue per Sale: 141.48
#     Create a bar chart to visualize the total revenue generated in each quarter of the year (Q1, Q2, Q3, Q4).
df = pd.read_csv('sales_data.csv', parse_dates=['date'])
df['quarter'] = df['date'].dt.quarter
quarterly_revenue = df.groupby('quarter')['revenue'].sum().sort_index()
plt.figure(figsize=(8,5))
plt.bar(quarterly_revenue.index, quarterly_revenue.values, color='skyblue')
plt.xticks([1,2,3,4], ['Q1', 'Q2', 'Q3', 'Q4'])
plt.xlabel('Quarter')
plt.ylabel('Total Revenue')
plt.title('Total Revenue per Quarter')
plt.show()
# 🌟 Exercise 5 : Data Visualisation Using MatPlotLib
# Instructions
#     Create a simple line plot using Matplotlib. Plot the function y = x^2 for x values ranging from -10 to 10. Add a title and label the x and y axes.
x = list(range(-10, 11))
y = [i**2 for i in x]
plt.plot(x, y)
plt.title('Plot of y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.show()
#     Generate a bar chart to display the sales data of four different products (A, B, C, D) in a week. The sales values are 15, 30, 45, and 20 respectively. Label the chart appropriately.
products = ['A', 'B', 'C', 'D']
sales = [15, 30, 45, 20]
plt.bar(products, sales)
plt.title('Weekly Sales')
plt.xlabel('Products')
plt.ylabel('Units Sold')
plt.show()
#     Create a pie chart representing the following data about favorite fruits of a group of people: Apples (40%), Bananas (30%), Cherries (20%), and Dates (10%). Customize the chart with different colors for each fruit and add a legend.
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
percentages = [40, 30, 20, 10]
colors = ['red', 'yellow', 'pink', 'brown']  # Custom colors for each fruit
plt.pie(percentages, labels=fruits, colors=colors, autopct='%1.1f%%')
plt.title('Favorite Fruits')
plt.legend(fruits, title='Fruits')
plt.show()

