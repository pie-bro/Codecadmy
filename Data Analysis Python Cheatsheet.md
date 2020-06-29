Pyplot functions
The Python library Matplotlib contains the pyplot module, which provides users with an interface for graphing data. Pyplot contains over 100 functions, from acorr to yticks. You must import the module, and plt is the standard variable name used.

from matplotlib import pyplot as plt
Here are some of the most common pyplot functions:

Function	Description
Plot	plots y versus x as lines and/or markers
Show	displays a figure
Axis	sets some axis properties
Xlabel	sets the label for the x-axis
Ylabel	sets the label for the y-axis
Title	sets a title for the axes
Subplot	adds a subplot to the current figure
Subplots_adjust	tunes the subplot layout
Legend	places a legend on the axes
Figure	creates a new figure
Savefig	saves the current figure
Pyplot-axis
Matplotlib’s pyplot.axis function takes one parameter, which must be a four-item array, and returns the current axes’ limits. The four items should contain enough info to define an x axis and a y axis by minimum and maximum values. The array must order these values as follows: x-axis minimum, x-axis maximum, y-axis minimum, y-axis maximum.

https://author.codecademy.com/learning-standards/5cc9c73faf246d6f7689df89

x = range(12)
y = [2,8,20,40,70,300,930,7000,68000,500000,4000000, 2000000]
plt.plot(x, y)

#x-axis minimum is 0, x-axis maximum is 11; y-axis minimum is 300, y-axis maximum is 500000
plt.axis([0,11,300,500000])
plt.show()


Setting Linestyle, Color in Matplotlib
In Python’s Matplotlib, the pyplot.plot() function can accept parameters to set the color(color), linestyle(linestyle) and marker(marker) for line graph. Color values can be HTML color names or HEX codes. Line styles can be dashed('--') or dotted('..'). Markers can be circles('o'), squares('s'), stars('*'), or other shapes.

pyplot.plot(days, money_spent, color='green', linestyle='--')
pyplot.plot(days, money_spent_2, color='#AAAAAA',  marker='o')


Adjusting Subplot Margins in Matplotlib
In Python’s Matplotlib, subplots can overlap, either horizontally or vertically. The function pyplot.subplots_adjust() can set better spacing around each subplot in a figure. It can set values for left, right, bottom and top margins, plus the horizontal(wspace) and vertical(hspace) spaces between adjacent subplots.

import matplotlib.pyplot as plt

# Left Plot
plt.subplot(1, 2, 1)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

# Right Plot
plt.subplot(1, 2, 2)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

# Subplot Adjust
plt.subplots_adjust(wspace=1.3)

plt.show()


X-ticks and Y-ticks in Matplotlib
In Python’s Matplotlib, the x-tick and y-tick marks of the plot can be changed using functions ax.set_xticks() and ax.set_yticks(). These functions accepts an array of values representing tick mark positions.

import matplotlib.pyplot as plt

ax = plt.subplot()
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
ax.set_xticks([1, 2, 4])


Subplots in Matplotlib
In Python, the Matplotlib’s pyplot.subplot() function can be used to create a figure with a grid of subplots. The function accepts number of rows, number of columns, and the current index as arguments.

import matplotlib.pyplot as plt

# Datasets
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

# First Subplot
plt.subplot(1, 2, 1)
plt.plot(x,y, color='green')
plt.title('First Subplot')

# Second Subplot
plt.subplot(1, 2, 2)
plt.plot(x,y, color='blue')
plt.title('Second Subplot')

# Display both subplots
plt.show()


Figures in Matplotlib
In Python’s Matplotlib, a figure is a container that holds plots. It can hold a single plot or multiple plots. When a figure holds multiple separate plots, those are called subplots.


Seaborn
Seaborn is a Python data visualization library that builds off the functionalities of Matplotlib and integrates nicely with Pandas DataFrames. It provides a high-level interface to draw statistical graphs, and makes it easier to create complex visualizations.

Estimator argument in barplot
The estimator argument of the barplot() method in Seaborn can alter how the data is aggregated. By default, each bin of a barplot displays the mean value of a variable. Using the estimator argument this behaviour would be different.

The estimator argument can receive a function such as np.sum, len, np.median or other statistical function. This function can be used in combination with raw data such as a list of numbers and display in a barplot the desired statistic of this list.

Seaborn barplot
In Seaborn, drawing a barplot is simple using the function sns.barplot(). This function takes in the paramaters data, x, and y. It then plots a barplot using data as the dataframe, or dataset for the plot. x is the column of the dataframe that contains the labels for the x axis, and y is the column of the dataframe that contains the data to graph (aka what will end up on the y axis).

Using the Seaborn sample data “tips”, we can draw a barplot having the days of the week be the x axis labels, and the total_bill be the y axis values:

sns.barplot(data = tips, x = "day", y = "total_bill")


Barplot error bars
By default, Seaborn’s barplot() function places error bars on the bar plot. Seaborn uses a bootstrapped confidence interval to calculate these error bars.

The confidence interval can be changed to standard deviation by setting the parameter ci = "sd".

Seaborn hue
For the Seaborn function sns.barplot(), the hue parameter can be used to create a bar plot with more than one dimension, or, in other words, such that the data can be divided into more than one set of columns.

Using the Seaborn sample data “tips”, we can draw a barplot with the days of the week as the labels of the columns on the x axis, and the total_bill as the y axis values as follows:

sns.barplot(data = tips, x = "day", y = "total_bill", hue = "sex")

As you can see, hue divides the data into two columns based on the “sex” - male and female.


Seaborn function plots means by default
By default, the seaborn function sns.barplot() plots the means of each category on the x axis.

In the example code block, the barplot will show the mean satisfaction for every gender in the dataframe df.

sns.barplot(data = df, x = "Gender", y = "Satisfaction")


Box and Whisker Plots in Seaborn
A box and whisker plot shows a dataset’s median value, quartiles, and outliers. The box’s central line is the dataset’s median, the upper and lower lines marks the 1st and 3rd quartiles, and the “diamonds” shows the dataset’s outliers. With Seaborn, multiple data sets can be plotted as adjacent box and whisker plots for easier comparison.

three datasets mapped as box and whisker plots, one blue, one green and one red.
Seaborn Package
Seaborn is a suitable package to plot variables and compare their distributions. With this package users can plot univariate and bivariate distributions among variables. It has superior capabilities than the popular methods of charts such as the barchart. Seaborn can show information about outliers, spread, lowest and highest points that otherwise would not be shown on a traditional barchart.



Pandas DataFrame creation
The fundamental Pandas object is called a DataFrame. It is a 2-dimensional size-mutable, potentially heterogeneous, tabular data structure.

A DataFrame can be created multiple ways. It can be created by passing in a dictionary or a list of lists to the pd.DataFrame() method, or by reading data from a CSV file.

# Ways of creating a Pandas DataFrame
# Passing in a dictionary:
data = {'name':['Anthony', 'Maria'], 'age':[30, 28]}
df = pd.DataFrame(data)

# Passing in a list of lists:
data = [['Tom', 20], ['Jack', 30], ['Meera', 25]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])

# Reading data from a csv file:
df = pd.read_csv('students.csv')


Pandas
Pandas is an open source library that is used to analyze data in Python. It takes in data, like a CSV or SQL database, and creates an object with rows and columns called a data frame. Pandas is typically imported with the alias pd.

import pandas as pd


Selecting Pandas DataFrame rows using logical operators
In pandas, specific rows can be selected if they satisfy certain conditions using Python’s logical operators. The result is a DataFrame that is a subset of the original DataFrame.

Multiple logical conditions can be combined with OR (using |) and AND (using &), and each condition must be enclosed in parentheses.

# Selecting rows where age is over 20
df[df.age > 20]

# Selecting rows where name is not John
df[df.name != "John"]

# Selecting rows where age is less than 10
# OR greater than 70
df[(df.age < 10) | (df.age > 70)]


Pandas apply() function
The Pandas apply() function can be used to apply a function on every value in a column or row of a DataFrame, and transform that column or row to the resulting values.

By default, it will apply a function to all values of a column. To perform it on a row instead, you can specify the argument axis=1 in the apply() function call.

# This function doubles the input value
def double(x):
  return 2*x

# Apply this function to double every value in a specified column
df.column1 = df.column1.apply(double)

# Lambda functions can also be supplied to `apply()`
df.column2 = df.column2.apply(lambda x : 3*x)

# Applying to a row requires it to be called on the entire DataFrame
df['newColumn'] = df.apply(lambda row: 
  row['column1'] * 1.5 + row['column2'],
  axis=1
)



Pandas DataFrames adding columns
Pandas DataFrames allow for the addition of columns after the DataFrame has already been created, by using the format df['newColumn'] and setting it equal to the new column’s value.

# Specifying each value in the new column:
df['newColumn'] = [1, 2, 3, 4]

# Setting each row in the new column to the same value:
df['newColumn'] = 1

# Creating a new column by doing a 
# calculation on an existing column:
df['newColumn'] = df['oldColumn'] * 5


Pandas’ Groupby
In a pandas DataFrame, aggregate statistic functions can be applied across multiple rows by using a groupby function. In the example, the code takes all of the elements that are the same in Name and groups them, replacing the values in Grade with their mean. Instead of mean() any aggregate statistics function, like median() or max(), can be used. Note that to use the groupby() function, at least two columns must be supplied.

df = pd.DataFrame([
  ["Amy","Assignment 1",75],
  ["Amy","Assignment 2",35],
  ["Bob","Assignment 1",99],
  ["Bob","Assignment 2",35]
  ], columns=["Name", "Assignment", "Grade"])

df.groupby('Name').Grade.mean()

# output of the groupby command
|Name | Grade|
| -  | - |
|Amy | 55|
|Bob |  67|


Pandas DataFrame Aggregate Function
Pandas’ aggregate statistics functions can be used to calculate statistics on a column of a DataFrame. For example, df.columnName.mean() computes the mean of the column columnName of dataframe df. The code block shows how to calculate statistics on the column columnName of df using Pandas’ aggregate statistics functions.

df.columnName.mean() # Average of all values in column
df.columnName.std() # Standard deviation of column
df.columnName.median() # Median value of column
df.columnName.max() # Maximum value in column
df.columnName.min() # Minimum value in column
df.columnName.count() # Number of values in column
df.columnName.nunique() # Number of unique values in column
df.columnName.unique() # List of unique values in column



Efficient Data Storage with Multiple Tables
For efficient data storage, related information is often spread across multiple tables of a database.

Consider an e-commerce business that tracks the products that have been ordered from its website. Business data for the company could be split into three tables:

orders would contain the information necessary to describe an order: order_id, customer_id, product_id, quantity, and timestamp
products would contain the information to describe each product: product_id, product_description and product_price
customers would contain the information for each customer: customer_id, customer_name, customer_address, and customer_phone_number
This table structure prevents the storage of redundant information, given that each customer’s and product’s information is only stored once, rather than each time a customer places an order for another item.

Pandas DataFrame Inner Merge
In Pandas the .merge() function uses an inner merge by default. An inner merge can be thought of as the intersection between two (or more) DataFrames. This is similar to a Venn diagram. In other words, an inner merge only returns rows both tables have in common. Any rows in one DataFrame that are not in the other, will not be in the result.

A Venn diagram of the intersection of two sets. The RED area is the intersection. This is what we get from an INNER MERGE.


