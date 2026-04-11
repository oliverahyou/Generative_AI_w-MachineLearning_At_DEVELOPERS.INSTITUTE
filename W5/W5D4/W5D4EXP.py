# Exercise 1: Identifying Data Types
# Below are various data sources. Identify whether each one is an example of structured or unstructured data.
#     A company’s financial reports stored in an Excel file. (Structured)
#     Photographs uploaded to a social media platform. (Unstructured)
#     A collection of news articles on a website. (Unstructured)
#     Inventory data in a relational database. (Structured)
#     Recorded interviews from a market research study. (Unstructured)
# Exercise 2: Transformation Exercise
# For each of the following unstructured data sources, propose a method to convert it into structured data. Explain your reasoning.
#     A series of blog posts about travel experiences. (Method: Extract information like location, date, and feeling at the time the post was written; Reasoning: This allows for easy analysis and comparison of travel experiences.)
#     Audio recordings of customer service calls. (Method: Transcribe audio to text and extract relevant information like customer issues and resolution; Reasoning: This enables sentiment analysis and identification of common problems.)
#     Handwritten notes from a brainstorming session. (Method: Scan and apply OCR(Optical Character Recognition) the notes to convert them into digital text; Reasoning: This allows for easy searching and categorization of ideas.)
#     A video tutorial on cooking. (Method: Extract subtitles or transcribe the audio; Reasoning: This enables searchability and analysis of the content.)
# Exercise 3 : Import a file from Kaggle
import pandas as pd
df = pd.read_csv('path/to/your/csvfile.csv')
df.head()
#    PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
# 0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
# 2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
# 3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
# 4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
# Exercise 4: Importing a CSV File
df = pd.read_csv("Iris.csv")
df.head(5)
#    Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
# 0   1            5.1           3.5            1.4           0.2  Iris-setosa
# 1   2            4.9           3.0            1.4           0.2  Iris-setosa
# 2   3            4.7           3.2            1.3           0.2  Iris-setosa
# 3   4            4.6           3.1            1.5           0.2  Iris-setosa
# 4   5            5.0           3.6            1.4           0.2  Iris-setosa
# Exercise 5 : Export a dataframe to excel format and JSON format.
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
df.to_excel("data.xlsx", index=False)
df.to_json('data.json', orient='records')
# Exercise 6: Reading JSON Data
import pandas as pd
json_data = pd.read_json('posts.json')
print(json_data.head(5))
# userId  id                                              title                                               body
# 0       1   1  sunt aut facere repellat provident occaecati e...  quia et suscipit\nsuscipit recusandae consequu...
# 1       1   2                                       qui est esse  est rerum tempore vitae\nsequi sint nihil repr...
# 2       1   3  ea molestias quasi exercitationem repellat qui...  et iusto sed quo iure\nvoluptatem occaecati om...
# 3       1   4                               eum et est occaecati  ullam et saepe reiciendis voluptatem adipisci\...
# 4       1   5                                 nesciunt quas odio  repudiandae veniam quaerat sunt sed\nalias aut...