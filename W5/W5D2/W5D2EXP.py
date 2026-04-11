# Exercise 1: Introduction to Data Analysis (Easy)
# Objective: Understand the basic overview and significance of data analysis.
# Task: Write a short essay or report on the following topics:
#     What is data analysis?
#     Why is data analysis important in modern contexts?
#     List and describe three areas where data analysis is applied today.
# Hint/Tip:
#     Research current trends in data analysis and real-world examples to provide depth to your essay.
# Data Analysis
# Definition:
# Data analysis is the process of inspecting, cleansing, transforming, and modeling data with the goal of discovering useful information, drawing conclusions, and supporting decision-making.
# It involves various techniques and tools to analyze data sets, identify patterns, and extract insights that can better inform business strategies, scientific research, and policy-making.
# 6 Key Steps in Data Analysis:
# 1. Data Collection: Gathering data from various sources such as databases, surveys, experiments or online platforms.
# 2. Data Cleaning: Removing or correcting errors and inconsistencies in the data to ensure its quality and reliability.
# 3. Data Exploration: Analyzing the data to understand its structure, identify patterns, anomalies or relationships for further analysis.
# 4. Data Interpretation: Drawing conclusions and insights from the analyzed data to inform decision-making or support hypotheses.
# 5. Data Visualization: Presenting the findings in a clear and understandable manner through charts, graphs, and reports.
# 6. Data Reporting: Communicating the results of the analysis to stakeholders in a clear and concise manner through presentations and reports
# Importance of Data Analysis:
# To put it simply: Properly executed data collection and its analysis could be the difference between success and failure for a business, organization, or any entity that relies on informed decision-making.
    # Applications of Data Analysis:
# 1. Business strategy: Before the launch of a new product or service, successful companies often conduct market research and analyse consumer data  to further understand their target audience and their preferences. This allows them to finetune their products or services and marketing strategies to better meet the needs of their customers, ultimately leading to increased sales and customer satisfaction.
# 2. Scientific research: In scientific research, data analysis is crucial for interpreting experimental results and drawing meaningful conclusions. For example, in medical research, analyzing patient data can help identify patterns and correlations that may lead to new treatments or insights into diseases.
# 3. Government policy : Governments use data analysis to inform policy decision making, improve public services and public satisfaction.
# Exercise 2: Dataset Loading and Initial Analysis
# Objective: Practice dataset loading from Kaggle and initial analysis.
import pandas as pd
df = pd.read_csv("Time Americans Spend Sleeping.csv")
df.head()
# Time Americans Spend Sleeping.csv
# index  Year  Period  Avg hrs per day sleeping  Standard Error Type of Days          Age Group  Activity   Sex
# 0      0  2003  Annual                      8.57           0.018     All days  15 years and over  Sleeping  Both
# 1      1  2004  Annual                      8.55           0.026     All days  15 years and over  Sleeping  Both
# 2      2  2005  Annual                      8.62           0.023     All days  15 years and over  Sleeping  Both
# 3      3  2006  Annual                      8.63           0.024     All days  15 years and over  Sleeping  Both
# 4      4  2007  Annual                      8.57           0.024     All days  15 years and over  Sleeping  Both
# Brief description of the dataset: 5 rows of a dataset that contains information about the average hours per day Americans spend sleeping, along with the standard error, type of days, age group, activity, and sex.
df = pd.read_csv("Mental health Depression disorder Data.csv")
df.head()
# Mental health Depression disorder Data.csv
#   index       Entity Code  Year Schizophrenia (%) Bipolar disorder (%) Eating disorders (%)  Anxiety disorders (%)  Drug use disorders (%)  Depression (%)  Alcohol use disorders (%)
# 0      0  Afghanistan  AFG  1990           0.16056             0.697779             0.101855               4.828830                1.677082        4.071831                   0.672404
# 1      1  Afghanistan  AFG  1991          0.160312             0.697961             0.099313               4.829740                1.684746        4.079531                   0.671768
# 2      2  Afghanistan  AFG  1992          0.160135             0.698107             0.096692               4.831108                1.694334        4.088358                   0.670644
# 3      3  Afghanistan  AFG  1993          0.160037             0.698257             0.094336               4.830864                1.705320        4.096190                   0.669738
# 4      4  Afghanistan  AFG  1994          0.160022             0.698469             0.092439               4.829423                1.716069        4.099582                   0.669260
# Brief description of the dataset: 5 rows of a dataset that contains information about the prevalence of various mental health disorders in Afghanistan from 1990 to 1994.
df = pd.read_csv("clean_dataset.csv")
df.head()
# clean_dataset.csv
# Gender    Age   Debt  Married  BankCustomer     Industry Ethnicity  YearsEmployed  PriorDefault  Employed  CreditScore  DriversLicense       Citizen  ZipCode  Income  Approved
# 0       1  30.83  0.000        1             1  Industrials     White           1.25             1         1            1               0       ByBirth      202       0         1
# 1       0  58.67  4.460        1             1    Materials     Black           3.04             1         1            6               0       ByBirth       43     560         1
# 2       0  24.50  0.500        1             1    Materials     Black           1.50             1         0            0               0       ByBirth      280     824         1
# 3       1  27.83  1.540        1             1  Industrials     White           3.75             1         1            5               1       ByBirth      100       3         1
# 4       1  20.17  5.625        1             1  Industrials     White           1.71             1         0            0               0  ByOtherMeans      120       0         1
# Brief description of the dataset: 5 rows of a dataset that contains bank details of customers, including their gender, age, debt, marital status, bank customer status, industry, ethnicity, years employed, prior default status, employment status, credit score, driver's license status, citizenship, zip code, income, and whether their loan application was approved.  
# Exercise 3: Identifying Data Types
# # Objective: Learn to identify different data types.
# Time Americans Spend Sleeping.csv
# Column Name:Year
# Data Type:Quantitative
# Reason:Numerical data that can be measured and statistically analyzed.
# Column Name:Period
# Data Type:Qualitative
# Reason:Non-numerical data that describes characteristics or opinions
# Column Name:Avg hrs per day sleeping
# Data Type:Quantitative
# Reason:Numerical data that can be measured and statistically analyzed.
# Column Name:Standard Error
# Data Type:Quantitative
# Reason:Numerical data that can be measured and statistically analyzed.
# Column Name:Type of Days
# Data Type:Qualitative
# Reason:Non-numerical data that describes characteristics or opinions
# Column Name:Age Group
# Data Type:Qualitative
# Reason:Non-numerical data that describes characteristics or opinions
# Column Name:Activity
# Data Type:Qualitative
# Reason:Non-numerical data that describes characteristics or opinions
# Column Name: Sex
# Data Type: Quantitative 
# Reason:Numerical data that can be measured and statistically analyzed.
# Exercise 4: Exploring Data Types
df = pd.read_csv("Iris.csv")
df.head()
#  Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
# 0   1            5.1           3.5            1.4           0.2  Iris-setosa
# 1   2            4.9           3.0            1.4           0.2  Iris-setosa
# 2   3            4.7           3.2            1.3           0.2  Iris-setosa
# 3   4            4.6           3.1            1.5           0.2  Iris-setosa
# 4   5            5.0           3.6            1.4           0.2  Iris-setosa
# SepalLengthCm: Quantitative, Reason:Numerical data that can be measured and statistically analyzed.
# SepalWidthCm: Quantitative, Reason:Numerical data that can be measured and statistically analyzed.
# PetalLengthCm: Quantitative, Reason:Numerical data that can be measured and statistically analyzed.
# PetalWidthCm: Quantitative, Reason:Numerical data that can be measured and statistically analyzed.
# Species: Qualitative, Reason:Non-numerical data that describes characteristics or opinions
# Exercise 5: Basic Data Analysis with Google Colab
# Reference being column SepalLengthCm
# SepalLengthCm = [5.1, 4.9, 4.7, 4.6, 5.0]
import statistics
mean_value = statistics.mean(SepalLengthCm)
median_value = statistics.median(SepalLengthCm)
try:
    mode_value = statistics.mode(SepalLengthCm)
except statistics.StatisticsError:
    mode_value = "No mode (all values appear once)"
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
import matplotlib.pyplot as plt
SepalLengthCm = [5.1, 4.9, 4.7, 4.6, 5.0]
SepalWidthCm = [3.5, 3.0, 3.2, 3.1, 3.6]
plt.scatter(SepalLengthCm, SepalWidthCm)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width")
plt.show()
# Exercise 6: Basic Observation Skills in Data Analysis
# Objective: Develop observation skills for data analysis.
df = pd.read_csv("Time Americans Spend Sleeping.csv")
# Time Americans Spend Sleeping.csv
# index  Year  Period  Avg hrs per day sleeping  Standard Error Type of Days          Age Group  Activity   Sex
# 0      0  2003  Annual                      8.57           0.018     All days  15 years and over  Sleeping  Both
# 1      1  2004  Annual                      8.55           0.026     All days  15 years and over  Sleeping  Both
# 2      2  2005  Annual                      8.62           0.023     All days  15 years and over  Sleeping  Both
# 3      3  2006  Annual                      8.63           0.024     All days  15 years and over  Sleeping  Both
# 4      4  2007  Annual                      8.57           0.024     All days  15 years and over  Sleeping  Both
# Colummns of interest: Year, Avg hrs per day sleeping, Standard Error, Age Group
# Types of analysis:
# Group Comparison Analysis could lead to insights on difference in sleeping patterns across different years, age groups, or types of days.
# Correlation Analysis could lead to insights on the potential increase or decrease of the average hours per day sleeping throughout the academic progression of the student population
# Cluster Analysis could lead to insightful segmentation of student population intro clusters such as 'Well-rested', 'Sleep-deprived', and 'Average Sleepers'

