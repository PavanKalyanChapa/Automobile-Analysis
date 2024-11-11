import pandas as pd
import numpy as np
import seaborn as sns  # for visualization
import matplotlib.pyplot as plt  # for visualization

sns.set(color_codes=True)
df = pd.read_csv('data.csv')
# To display the top 5 rows
df.head(5)
# Checking the data type
df.dtypes

# Dropping irrelevant columns
df = df.drop(['Engine Fuel Type', 'Number of Doors', 'Market Category','Vehicle Style','Popularity'], axis=1)
df.head(5)

df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive","highway MPG": "MPG-H","city mpg":"MPG-C","MSRP":"Price"})
df.head(5)

# Total number of rows and columns
df.shape

# Rows containing duplicate data
duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)

# Used to count the number of rows before removing the data
df.count()

# Dropping the duplicates
df = df.drop_duplicates()
df.head(5)

# Counting the number of rows after removing duplicates.
df.count()

# Finding the null values.
print(df.isnull().sum())

#Dropping the missing values
df = df.dropna()
df.count()

# After dropping the values
print(df.isnull().sum())

#Detecting Outliers
sns.boxplot(x=df["Price"])

sns.boxplot(x=df["MPG-H"])

sns.boxplot(x=df["MPG-C"])

sns.boxplot(x=df['Cylinders'])

#selects only columns with numeric data types --->  select_dtypes(include=[np.number]).
Q1 = df.select_dtypes(include=[np.number]).quantile(0.25)
Q3 = df.select_dtypes(include=[np.number]).quantile(0.75)
IQR = Q3 - Q1
print(IQR)

#Removing Outliers
df_numeric = df.select_dtypes(include=[np.number])
df = df[~((df_numeric < (Q1 - 1.5 * IQR)) | (df_numeric > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape

# Plotting a Histogram
df.Make.value_counts().nlargest(40).plot(kind = 'bar', figsize=( 10,5))
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make');

# Finding the relations between the variables.
# Selecting only numeric columns from the DataFrame
numeric_df = df.select_dtypes(include=[np.number])

# Calculating the correlation matrix for the numeric columns
c = numeric_df.corr()

# Plotting the heatmap
plt.figure(figsize=(20,10))
sns.heatmap(c, cmap="BrBG", annot=True)
plt.title("Correlation Heatmap")
plt.show()

# Displaying the correlation matrix
c

# Plotting a scatter plot
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()

