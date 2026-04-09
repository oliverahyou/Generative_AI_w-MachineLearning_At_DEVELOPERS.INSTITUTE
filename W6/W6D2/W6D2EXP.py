# 🌟 Exercise 1 : Understanding Data Visualization
# Instructions

#     Explain why data visualization is important in data analysis.
# Data visualization is crucial in data analysis because it allows us to represent complex data in a visual format that is easier to understand and interpret. 
# It helps to identify patterns in the data that may not be immediately obvious from numbers alone. Visualization also facilitate communication of insights and findings to a broader audience, making it easier for stakeholders to grasp the significance of the data and make informed decisions based on it.

#     Describe the purpose of a line graph in data visualization.
#  Line plots are used to display quantitative values over a continuous interval.

# 🌟 Exercise 2 : Creating a Line Plot for Temperature Variation
# Instructions

#     Create a simple line plot using Matplotlib that represents the temperature variations over a week.
#     Use a list of temperature values for each day of the week (e.g., [72, 74, 76, 80, 82, 78, 75]) and label the x-axis as “Day” and the y-axis as “Temperature (°F)”.

#Sample
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [72, 74, 76, 80, 82, 78, 75]

import matplotlib.pyplot as plt

plt.plot(days, temperatures)
plt.title('Temperature Variations Over a Week')
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.show()


# 🌟 Exercise 3 : Visualizing Monthly Sales with a Bar Chart
# Instructions

#     Generate a bar chart using Matplotlib to visualize the monthly sales data for a retail store.
#     Create a list of sales values for each month (e.g., [5000, 5500, 6200, 7000, 7500]) and label the x-axis as “Month” and the y-axis as “Sales Amount ($)”.


# 🌟 Exercise 4 : Data Visualisation
# Instructions

# Using the dataset: sales_data.csv

#     Calculate the total quantity of products sold by the company.
#     Identify the category that had the highest revenue and calculate how much revenue it generated.
#     Determine the average revenue per sale in the dataset.
#     Create a bar chart to visualize the total revenue generated in each quarter of the year (Q1, Q2, Q3, Q4).


# 🌟 Exercise 5 : Data Visualisation Using MatPlotLib
# Instructions

#     Create a simple line plot using Matplotlib. Plot the function y = x^2 for x values ranging from -10 to 10. Add a title and label the x and y axes.
#     Generate a bar chart to display the sales data of four different products (A, B, C, D) in a week. The sales values are 15, 30, 45, and 20 respectively. Label the chart appropriately.
#     Create a pie chart representing the following data about favorite fruits of a group of people: Apples (40%), Bananas (30%), Cherries (20%), and Dates (10%). Customize the chart with different colors for each fruit and add a legend.


