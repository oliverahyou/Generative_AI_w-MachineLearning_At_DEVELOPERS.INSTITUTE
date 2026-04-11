# Exercise 1: Duplicate Detection and Removal
import pandas as pd
df = pd.read_csv('train.csv')
clean_df = df.drop_duplicates()
clean_df.to_csv("train_data.csv", index=False)
rows = len(df)
print(rows)
# 891 rows in the original dataset
# 891 rows in the cleaned dataset, indicating that there were no duplicate entries in the original dataset.
# Exercise 2: Handling Missing Values
print(df.isnull().sum())
# PassengerId      0
# Survived         0
# Pclass           0
# Name             0
# Sex              0
# Age            177
# Parch            0
# Ticket           0
# Fare             0
# Cabin          687
# Embarked         2
df["Age"] = df["Age"].fillna(df["Age"].median())
# Type of data: Numerical
# Method used: Median Imputation
# Reasons for using Median Imputation for "Age"
# Robustness to Outliers: The median is less affected by outliers compared to the mean. If there are extreme values in the "Age" column, using the median will provide a more representative value
df.drop(columns=["Cabin"], inplace=True)
# Type of data: Categorical
# Method used: Dropping the columns
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
# Type of data: Categorical
# Method used: Mode Imputation
# Reasons for using Mode Imputation for "Embarked":
# Only a few missing entries and mode preserves the category distribution
print(df.isnull().sum())  
# PassengerId    0
# Survived       0
# Pclass         0
# Name           0
# Sex            0
# Age            0
# SibSp          0
# Parch          0
# Ticket         0
# Fare           0
# Embarked       0
# As seen above: After applying the above strategies, there are no missing values left in the dataset.
# Exercise 3: Feature Engineering
# Using the following formula, we can create feature: 'Family Size'
# Family Size = SibSp + Parch + 1, where one is the person themselves
df["Family Size"] = df["SibSp"] + df["Parch"] + 1
# Since title are usually followed by a dot in the name, we can extract the title from the "Name" column using string manipulation techniques
df["Title"] = df["Name"].str.extract(' ([A-Za-z]+)\.', expand=False)
# Exercise 4: Outlier Detection and Handling
import matplotlib.pyplot as plt
df = pd.read_csv("train.csv")
# Histograms
df['Fare'].hist(bins=50)
plt.title("Fare Distribution")
plt.show()
df['Age'].hist(bins=50)
plt.title("Age Distribution")
plt.show()
# Boxplots
df.boxplot(column=['Fare'])
plt.title("Fare Boxplot")
plt.show()
df.boxplot(column=['Age'])
plt.title("Age Boxplot")
plt.show()
#IQR method for outlier detection
def detect_outliers_iqr(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return lower, upper
fare_lower, fare_upper = detect_outliers_iqr(df['Fare'])
age_lower, age_upper = detect_outliers_iqr(df['Age'])
print("Fare bounds:", fare_lower, fare_upper)
print("Age bounds:", age_lower, age_upper)
# Exercise 5: Data Standardization and Normalization
# Exercise 6: Feature Encoding
# Exercise 7: Data Transformation for Age Feature