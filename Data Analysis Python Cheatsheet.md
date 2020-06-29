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



Indexing NumPy elements using conditionals
NumPy elements can be indexed using conditionals. The syntax to filter an array using a conditional is array_name[conditional].

The returned array will contain only the elements for which the conditional evaluates to True.

numbers = np.array([-5, 4, 0, 2, 3])
positives = numbers[numbers > 0]
print(positives)
# array([4, 2, 3])



NumPy element-wise logical operations
NumPy Arrays support element-wise logical operations, returning new Arrays populated with False or True based on their evaluation.

numbers = np.array([-5, 4, 0, 2, 3])
is_positive = numbers > 0
print(is_positive)
# array([False, True, False, True, True], dtype=bool)


Creating NumPy Arrays from files
NumPy Arrays can be created from data in CSV files or other delimited text by using the np.genfromtxt() method.

The named parameter delimiter is used to determine the delimiting character between values.

imported_csv = np.genfromtxt("filename.txt", delimiter=",")


NumPy Arrays
NumPy (short for “Numerical Python”) is a Python module used for numerical computing, creating arrays and matrices, and performing very fast operations on those data structures. The core of NumPy is a multidimensional Array object.

The NumPy .array() method is used to create new NumPy Arrays.

# Import the NumPy module, aliased as 'np'
import numpy as np

# NumPy Arrays can be created with a list
my_array = np.array([1, 2, 3, 4])


Accessing NumPy Array elements by index
Individual NumPy Array elements can be accessed by index, using syntax identical to Python lists: array[index] for a single element, or array[start:end] for a slice, where start and end are the starting and ending indexes for the slice.

Nested Arrays or elements can be accessed by adding additional comma-separated parameters.

matrix = np.array([[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9]])

print(matrix[0, 0]) 
# 1

print(matrix[1,:])
# array([4, 5, 6])


NumPy element-wise arithmetic operations
NumPy Arrays support element-wise operations, meaning that arithmetic operations on arrays are applied to each value in the array.

Multiple arrays can also be used in arithmetic operations, provided that they have the same lengths.

odds = np.array([1, 3, 5, 7, 9])
evens = odds + 1
print(evens)
# array([2, 4, 6, 8, 10])

array1 = np.array([1, 2, 3])
array2 = np.array([4, 3, 2])
new_array = array1 + array2
print(new_array)
# array([5, 5, 5])


NumPy’s Mean and Axis
In a two-dimensional array, you may want the mean of just the rows or just the columns. In Python, the NumPy .mean() function can be used to find these values. To find the average of all rows, set the axis parameter to 1. To find the average of all columns, set the axis parameter to 0.

We will use the following 2-dimensional array for this example:

```
py
ring_toss = np.array([[1, 0, 0], 
                          [0, 0, 1], 
                          [1, 0, 1]])
```

The code below will calculate the average of each row.

```py
np.mean(ring_toss, axis=1)
# Output: array([ 0.33333333,  0.33333333,  0.66666667])
```



Conditions in Numpy.mean()
In Python, the function numpy.mean() can be used to calculate the percent of array elements that satisfies a certain condition.

import numpy as np
a = np.array([1,2,3,4])
np.mean(a)
# Output = 2.5

np.mean(a>2)
# The array now becomes array([False, False, True, True])
# True = 1.0,False = 0.0
# Output = 0.5
# 50% of array elements are greater than 2


NumPy Percentile Function
In Python, the NumPy .percentile function accepts a NumPy array and percentile value between 0 and 100. The function returns the value of the array element at the percentile specified.

d = np.array([1, 2, 3, 4, 4, 4, 6, 6, 7,  8, 8])
np.percentile(d, 40)
# Output: 4.00



NumPy’s Percentile and Quartiles
In Python, the NumPy .percentile() function can calculate the first, second and third quartiles of an array. These three quartiles are simply the values at the 25th, 50th, and 75th percentiles, so those numbers would be the parameters, just as with any other percentile.

d = [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8]
np.percentile(d, 25)
# Output: 3.5
np.percentile(d, 75)
#Output: 6.5


NumPy’s Sort Function
In Python, the NumPy .sort() function takes a NumPy array and returns a different NumPy array, this one containing the same numbers in ascending order.

heights = np.array([49.7, 46.9, 62, 47.2, 47, 48.3, 48.7])
np.sort(heights)
# Output: array([ 46.9,  47. ,  47.2,  48.3,  48.7,  49.7,  62])


Definition of Percentile
In statistics, a data set’s Nth percentile is the cutoff point demarcating the lower N% of samples.


Datasets and their Histograms
When datasets are plotted as histograms, the way the data is distributed determines the distribution type of the data.

The number of peaks in the histogram determines the modality of the dataset. It can be unimodal (one peak), bimodal (two peaks), multimodal (more than two peaks) or uniform (no peaks).

Unimodal datasets can also be symmetric, skew-left or skew-right depending on where the peak is relative to the rest of the data.

Normal Distribution using Python Numpy module
Normal distribution in NumPy can be created using the below method.

np.random.normal(loc, scale, size)

Where loc is the mean for the normal distribution, scale is the standard deviation of the distribution, and size is the number of observations the distribution will have.

import numpy as np
mu = 0 #mean
sigma = 0.1 #standard deviation
np.random.normal(mu, sigma, 1000)


Standard deviation
The standard deviation of a normal distribution determines how spread out the data is from the mean.

68% of samples will fall between +/- 1 standard deviation of the mean.

95% of samples will fall between +/- 2 standard deviations of the mean.

99.7% of samples will fall between +/- 3 standard deviations of the mean.

Histogram Visualization
A histogram is a plot that visualizes the distribution of samples in a dataset. Histogram shows the frequency on the vertical axis and the horizontal axis is another dimension. Usually horizontal axis has bins, where every bin has a minimum and maximum value. Each bin also has a frequency between x and infinite.

import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
plt.hist(x_axis,bins=10,color='blue')
plt.xlabel('Age bins')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()


haracter Sets in Regular Expressions
Regular expression character sets denoted by a pair of brackets [] will match any of the characters included within the brackets. For example, the regular expression con[sc]en[sc]us will match any of the spellings consensus, concensus, consencus, and concencus.

Optional Quantifiers in Regular Expressions
In Regular expressions, optional quantifiers are denoted by a question mark ?. It indicates that a character can appear either 0 or 1 time. For example, the regular expression humou?r will match the text humour as well as the text humor.

Literals in Regular Expressions
In Regular expression, the literals are the simplest characters that will match the exact text of the literals. For example, the regex monkey will completely match the text monkey but will also match monkey in text The monkeys like to eat bananas.

Fixed Quantifiers in Regular Expressions
In Regular expressions, fixed quantifiers are denoted by curly braces {}. It contains either the exact quantity or the quantity range of characters to be matched. For example, the regular expression roa{3}r will match the text roaaar, while the regular expression roa{3,6}r will match roaaar, roaaaar, roaaaaar, or roaaaaaar.

Alternation in Regular Expressions
Alternation indicated by the pipe symbol |, allows for the matching of either of two subexpressions. For example, the regex baboons|gorillas will match the text baboons as well as the text gorillas.

Anchors in Regular Expressions
Anchors (hat ^ and dollar sign $) are used in regular expressions to match text at the start and end of a string, respectively. For example, the regex ^Monkeys: my mortal enemy$ will completely match the text Monkeys: my mortal enemy but not match Spider Monkeys: my mortal enemy or Monkeys: my mortal enemy in the wild. The ^ ensures that the matched text begins with Monkeys, and the $ ensures the matched text ends with enemy.

Regular Expressions
Regular expressions are sequence of characters defining a pattern of text that needs to be found. They can be used for parsing the text files for specific pattern, verifying test results, and finding keywords in emails or webpages.

Wildcards in Regular expressions
In Regular expression, wildcards are denoted with the period . and it can match any single character (letter, number, symbol or whitespace) in a piece of text. For example, the regular expression ......... will match the text orangutan, marsupial, or any other 9-character text.

Regular Expression Ranges
Regular expression ranges are used to specify a range of characters that can be matched. Common regular expression ranges include: [A-Z]. : match any uppercase letter [a-z]. : match any lowercase letter [0-9]. : match any digit [A-Za-z] : match any uppercase or lowercase letter.

Shorthand Character Classes in Regular Expressions
Shorthand character classes simplify writing regular expressions. For example, \w represents the regex range [A-Za-z0-9_], \d represents [0-9], \W represents [^A-Za-z0-9_] matching any character not included by \w, \D represents [^0-9] matching any character not included by \d.

Kleene Star & Kleene Plus in Regular Expressions
In Regular expressions, the Kleene star(*) indicates that the preceding character can occur 0 or more times. For example, meo*w will match mew, meow, meooow, and meoooooooooooow. The Kleene plus(+) indicates that the preceding character can occur 1 or more times. For example, meo+w will match meow, meooow, and meoooooooooooow, but not match mew.

Grouping in Regular Expressions
In Regular expressions, grouping is accomplished by open ( and close parenthesis ). Thus the regular expression I love (baboons|gorillas) will match the text I love baboons as well as I love gorillas, as the grouping limits the reach of the | to the text within the parentheses.


Hypothesis Test Errors
Type I errors, also known as false positives, is the error of rejecting a null hypothesis when it is actually true. This can be viewed as a miss being registered as a hit. The acceptable rate of this type of error is called significance level and is usually set to be 0.05 (5%) or 0.01 (1%).

Type II errors, also known as false negatives, is the error of not rejecting a null hypothesis when the alternative hypothesis is the true. This can be viewed as a hit being registered as a miss.

Depending on the purpose of testing, testers decide which type of error to be concerned. But, usually type I error is more important than type II.

Sample Vs. Population Mean
In statistics, we often use the mean of a sample to estimate or infer the mean of the broader population from which the sample was taken. In other words, the sample mean is an estimation of the population mean.

Central Limit Theorem
The central limit theorem states that as samples of larger size are collected from a population, the distribution of sample means approaches a normal distribution with the same mean as the population. No matter the distribution of the population (uniform, binomial, etc), the sampling distribution of the mean will approximate a normal distribution and its mean is the same as the population mean.

The central limit theorem allows us to perform tests, make inferences, and solve problems using the normal distribution, even when the population is not normally distributed.

Hypothesis Test P-value
Statistical hypothesis tests return a p-value, which indicates the probability that the null hypothesis of a test is true. If the p-value is less than or equal to the significance level, then the null hypothesis is rejected in favor of the alternative hypothesis. And, if the p-value is greater than the significance level, then the null hypothesis is not rejected.

Univariate T-test
A univariate T-test (or 1 Sample T-test) is a type of hypothesis test that compares a sample mean to a hypothetical population mean and determines the probability that the sample came from a distribution with the desired mean.

This can be performed in Python using the ttest_1samp() function of the SciPy library. The code block shows how to call ttest_1samp(). It requires two inputs, a sample distribution of values and an expected mean and returns two outputs, the t-statistic and the p-value.

from scipy.stats import ttest_1samp

t_stat, p_val = ttest_1samp(example_distribution, expected_mean)


Tukey’s Range Hypothesis Tests
A Tukey’s Range hypothesis test can be used to check if the relationship between two datasets is statistically significant.

The Tukey’s Range test can be performed in Python using the StatsModels library function pairwise_tukeyhsd(). The example code block shows how to call pairwise_tukeyhsd(). It accepts a list of data, a list of labels, and the desired significance level.

from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey_results = pairwise_tukeyhsd(data, labels, alpha=significance_level)
