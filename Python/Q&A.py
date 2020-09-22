#Multi line comments are written like this:

""" 
Several
Lines
"""

"""
How can I use quotes inside of a string? - FAQ / Python FAQ - Codecademy Forums
https://discuss.codecademy.com/t/how-can-i-use-quotes-inside-of-a-string/448684
If a multi-line string isn’t assigned a variable or used in an expression it is treated as a comment.



Notice that when we perform division, the result has a decimal place. 
This is because Python converts all ints to floats before performing division. 
In older versions of Python (2.7 and earlier) this conversion did not happen, and integer division 
would always round down to the nearest integer.

#Q
print("total squares needed:" + quilt_width * quilt_length )
#I got the following error

#A
You use + to attempt string concatenation, but you don’t have two strings. Thus you get an error.
So either you will need to convert the integer to a string, so you can stick with your current approach (using +).
The problem is that using + to add number and string together, will result in a TypeError, 
you can add these two types together. these types don’t go together, just like certain things don’t go together.
you can use a comma (,) instead of a + to overcome your problem. 




How can i start new line after function ended? I use double backspace, but i hope there is an easier way, isn’t there?
“Home” button
tab and shift + tab
Backspace

Question
In Python, is a single tab equivalent to 2 spaces or 4 spaces, and if so can they be mixed?

Answer
In most code editors, tabs are not the same as 2 spaces or 4 spaces by default.
A tab is stored differently than spaces in the code. Tabs can be seen as a big “jump” in the text, while spaces are always 1 space each.
When you move your cursor in the code, you may notice this “jump” when going through tabs as opposed to spaces.
Unlike computers, we can’t easily tell whether an indentation is a tab or spaces. 
Not knowing this can cause potential errors in the code, and mixing them or wrongly applying them will cause an IndentationError. 
Because of this, staying consistent with using spaces or tabs in a program can be very important and save a lot of trouble.


Question
In Python, do parameters still hold some value when the function call completes?

Answer
When a function call completes, all the parameters will no longer store any values in them.
Unlike regular variables we’ve worked with before, that were not parameters, parameters do not continue to reference some 
value after the function finishes running. Parameters are essentially “temporary placeholder variables”, so they only temporarily, 
for the duration of the function call, hold onto values, and reference them while the function is running. Once the function call 
completes entirely, the parameters will dereference any values and become “empty” again.


Once you give an argument a default value (making it a keyword argument), 
no arguments that follow can be used positionally. For example:

def greet_customer(special_item="bananas", grocery_store): # this is not valid
    ...
def greet_customer(special_item, grocery_store="Engrossing Grocers"): # this is valid
    ...


Question
When writing a function in Python, do we have to place all keyword arguments so that they come after all the positional arguments in the function definition?

Answer
Yes, keyword arguments, which are assigned some value in the definition, must be written after all the positional arguments.
If we do not follow this rule, then Python will give us an error message.

Example code
# This would cause an error, because
# arg1 is a keyword argument but was placed 
# before arg2, a positional argument.
def func(arg1=10, arg2, arg3=30):
  return arg1 + arg2 + arg3
print(func(20))

# All keyword arguments must 
# follow all the positional arguments, so
# this updated function would work.
def fixed_func(arg2, arg1=10, arg3=30):
  return arg1 + arg2 + arg3
print(fixed_func(20)) # This will print 60


new_value is only a local variable, not accessible outside of the function. 
It is preset to 10, but takes on any value we pass in. If no value is passed in, then new_value becomes 10.
Multiple keywords are possible, but the position is critical.
>>> def foo(a = 1, b = 2, c = 3):
    return a * 4, b * 3, c * 2
>>> foo()
(4, 6, 6)
>>> foo(4)
(16, 6, 6)
>>> foo(4, 5)
(16, 15, 6)
>>> foo(4, 5, 6)
(16, 15, 12)

Q
def calculate_age(current_year,birth_year)
  return age = current_year - birth_year
This return a syntax error message

A
We cannot return a statement, only an expression.
return current_year - birth_year


Question
In Python, if there is a return statement within a function, does the return always have to be the last line of code in the function?

Answer
That does not always have to be the case, but usually, a return statement is the last line of code in a function since it should be run
last.

The reason for this is because of how a return statement works. When a return statement is run inside of a function, the function will
immediately terminate and return that value, and none of the remaining code lines in the function will run. Because of this, functions usually have the return statement at the very end, so that all the other lines of code in the function will complete first before the function terminates and returns a value.
Example
# This function will return 20
def example():
  total = 20
  return total	
  # These lines will not run
  # because they follow a return.
  total += 10
  print(total)
  return total

Question
What happens when a parameter has the same name as a variable defined outside the function?

Answer
When a parameter has the same name as a variable defined outside, instead of the function using the variable defined outside, 
it will only reference the value that was passed to the parameter. So, parameters will be used over variables of the same name 
within a function.
Example
name = "Josh"

# The parameter has the same name as the variable above.
# The function will not use the variable's value, but the value
# passed into this parameter instead.
def sayHi(name):
  print("Hi, " + name + "!")

sayHi("Anne") 
# This will print out “Hi, Anne!”

# The value of the variable defined outside was unchanged.
# This will print out “Josh”.
print(name)


Question
What is the difference between = and == in Python? Is there any relation?

Answer
In Python, the operators = and == serve very different purposes, and don’t have much relation at all other than similar syntax.
The = operator is used for assignment, such as when assigning a value to a variable.
The == operator is the relational operator for checking equality of two values. 
If the values are the same, it will return True, and will return False otherwise.
Example
# Assignment
number = 3
# Comparison
number == 30 # False


Q
If we use print instead of return why does the word none comes in the console?

A
So return and then “Strng” will never print.The returned value can be assigned to a variable for future use, passed directly as 
an argument to another function (in the example above, the print() function), or used as one value within an expression. 
If the calling expression does nothing with the return value, it will be lost.


Question
In Python, is there a limit to the number of elif statements that are allowed?

Answer
No, there is no strict limit to how many elif statements you can include after an if statement. You can add as many as you need into the program, 
not taking into account memory or other possible limitations like hardware.
The only strict limit is that there can only be one if and one else per if/elif/else statement block, but there is no limit on the number of elif.


Question
In Python, am I able to check for multiple error types with one try and except statement?

Answer
Yes, it is possible to check multiple error types with a single try and except statement.
For the except, we can include multiple error types listed within a tuple. It will check if any of the listed errors are encountered.
You can also do a general except without a specified error type, but that is not recommended as it will catch any errors, including 
ones we don’t want to check.
Example
# Multiple error types listed.
try:
  line of code
except(TypeError, NameError, ...):
  ...  
# Not recommended
try:
  line of code
except:
  ...


If there is a sequence separated by commas standing alone, it is a tuple.
If surrounded by parentheses, still a tuple.
If surrounded by brackets, it a list.
If surrounded by “curly braces”, it is a set.


Question
Do the lists passed to the zip() function have to be the same length?

Answer
The zip() function will only iterate over the smallest list passed. If given lists of different lengths, 
the resulting combination will only be as long as the smallest list passed. In the following code example, 
list_two contains more elements than list_one so the resulting merged list will only be as long as list_one.
list_one = ['Joe', 'Mark', 'Jane']
list_two = [ 100, 34, 87, 23, 65 ]
merged = zip(list_one, list_two)
print(list(merged))
# [('Joe', 100), ('Mark', 34), ('Jane', 87)]
It is possible to use the cycle() function from itertools to repeat values from the shorter list. 
This will allow zip() to iterate over all the elements from the longer list. 
In this example, cycle() is used to repeat values from list_one and the resulting merged list will now contain all values from list_two.

from itertools import cycle
list_one = ['Joe', 'Mark', 'Jane']
list_two = [ 100, 34, 87, 23, 65 ]
merged2 = zip(cycle(list_one), list_two)
print(list(merged2))
#[('Joe', 100), ('Mark', 34), ('Jane', 87), ('Joe', 23), ('Mark', 65)]


myList = ['a', 'b', 'c']
myTuple = ('a', 'b', 'c')
we have a list (myList) and a tuple (myTuple), a tuple is very similar to a list, except tuples are immutable.


Question
How does the behavior of the continue statement differ from the break statement?

Answer
The continue statement interrupts the execution of a loop and causes the loop to start the next iteration. 
Any code following the continue is not executed but the loop will continue on starting with the next iteration. 
The break statement will terminate the execution of the loop. No further code in the loop will execute and the program will 
resume execution at the next statement following the end of the loop.
In the following code example, if the counter is an even number, a continue statement is used to skip printing the number 
and continue to the next number. An if statement checks if counter has reached 19 and then uses a break to stop the execution 
of the loop. This code will print the odd numbers from 1 through 17.

counter = 0
while counter < 100:
    counter += 1
    
    # If number is even - skip to next
    if counter % 2 == 0:
        continue

    if counter == 19:
        break
        
    print(counter)


Question
When using a list comprehension with an if, is it possible to have an else clause?

Answer
Yes, an else clause can be used with an if in a list comprehension. The following code example shows the use of an else in a simple list comprehension. 
The if/else is placed in front of the for component of the list comprehension.
divbythree = [  "Yes" if number % 3 == 0 else "No" for number in range(1,20)]
print(divbythree)

How does indexing a string work? or What does `word[0]` in the example mean? - FAQ / Python FAQ - Codecademy Forums
https://discuss.codecademy.com/t/how-does-indexing-a-string-work-or-what-does-word-0-in-the-example-mean/457119

Can you break down the uses of the temporary variable `word` in the example? - FAQ / Python FAQ - Codecademy Forums
https://discuss.codecademy.com/t/can-you-break-down-the-uses-of-the-temporary-variable-word-in-the-example/457123


Question
In this exercise 14, the variable from the list comprehension is used to calculate a value. Is it possible to call a function using the variable?

Answer
Yes, the variable in the for of a list comprehension can be used as a parameter to a function. 
In this example, the variable number is passed to randint() to calculate a random number between number and 2 * number for the list produced by the comprehension.
from random import randint
random_numbers = [ randint(number, 2 * number) for number in range(10)]
print(random_numbers)


Question
When should I create a Pandas dataframe using a dictionary or a list?

Answer
You can create Pandas dataframes using either a dictionary or a list of lists, 
but depending on several factors, using one can be preferred over the other.

Using dictionaries can be much faster, since you can just include the column names as the keys, 
and include the values of the column as a list for the keys. However, a disadvantage of using a dictionary is that the columns 
will not preserve the order that you entered them, and will default to alphabetical ordering instead. This is important to 
keep in mind especially if the column order is important.

Using a list of lists allows you to enter each row of data one at a time as a separate list, but it may take longer than 
using a dictionary, since column names must be added as a separate list after the rows are added. However, a list of lists 
allows you to order the column names specifically, which can be very important.


Question
In a CSV file, does spacing matter, such as before or after commas?

Answer
Yes, in most cases for CSV files, Pandas will separate the data by the commas, and will keep any spaces that were included before or 
after a comma.
Because of this, it is important that when creating a CSV file, each value should only be separated by a comma without any unwanted 
whitespace before or after the commas, since they will not be removed automatically.
Example CSV row
name, date, location
For the above example, when reading the data from this CSV, it will include the leading spaces for ’ date’ and ’ location’.


Question
In Pandas, what happens if there are empty or missing values in a CSV file and we try to read it?

Answer
If the CSV file contains missing values, then when we read the file, it will populate the missing cells with NaN. 
NaN is short of “Not a Number”, and used to signify missing values.
If needed, we can replace these NaN values with an actual value, like 0 or an empty string '', using the fillna() method. 
Or, we can drop any rows that contain an empty value, using dropna().
For example, if we had a CSV file containing the following:
name,flavor,topping
,chocolate,chocolate shavings
Birthday Cake,,gold sprinkles
The second row is missing a value in the first column, and the third row is missing a value in the second column.
When we read this file using Pandas read_csv, it will load it like so, filling in the missing values with NaN.
name             flavor        topping
NaN              chocolate     chocolate shavings
Birthday Cake    NaN           gold sprinkles


Question
How is a Pandas series different from a dataframe?

Answer
In Pandas a series is a one-dimensional object that contains any type of data, similar in ways to a Numpy array.
Series objects have a single axis label, like a column title, which is the index of the series. 
A series is essentially a single column.
# Creating a series
clinic_east = pd.Series([100, 51, 81, 80, 51, 112])
A dataframe is a two-dimensional object that can hold multiple columns of different types of data. 
They are similar to a table in SQL.
A single column of a dataframe is a series, and a dataframe is a container of two or more series objects.
When we select a single row of a dataframe, the result is a Series (just like when we select a single column).

# Creating a DataFrame
df = pd.DataFrame ([
  ['January', 100, 100],
  ['February', 51, 45],
  ['March', 81, 96]],
  columns=["month", "clinic_east", "clinic_north"]
)
When we select a single column from a dataframe, the result is called a Series.
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
clinic_north = df.clinic_north
print(type(clinic_north))
#<class 'pandas.core.series.Series'>
print(type(df))
#<class 'pandas.core.frame.DataFrame'>


Question
Can we select columns of a Pandas dataframe in any order?

Answer
You certainly can! When selecting multiple columns from a DataFrame, you can order the columns however you would like them to appear. 
This is particularly useful because if we wanted to see the data in a certain way different from the original column order, we can reorder them in the output however we need.
Example
df = pd.DataFrame([
  ['Doe', 'Jane'],
  ['Law', 'Bob']],
  columns = ['last_name', 'first_name'])
# We can select the first_name column first, 
# then the last_name.
full_names = df[['first_name', 'last_name']]


Question
When using iloc to select ranges of Pandas dataframe rows, can we skip rows? For instance, can we choose to select every second or third row only?

Answer
You can! Selecting multiple rows using .iloc is very similar to list slicing in Python. There are a few ways to select rows using iloc.
To select just a single row, we pass in a single value, the index. For example with Python lists,
numbers[0] # First element of numbers list
And with Dataframes, we would do something similar,
orders.iloc[0].
Selecting a range of elements of a list and a range of rows in Pandas is also very similar.
# Python list
numbers[3:7]
# Pandas
orders.iloc[3:7]
To skip a certain number of indexes per index, we can include a third, step, value.
# This selects values at indexes 0, 3, 6, 9.
# Python list
numbers[0:10:3]
# This selects rows at indexes 0, 3, 6, 9
# Pandas
orders.iloc[0:10:3]

Lambda Functions in Python | Codecademy
https://www.codecademy.com/paths/data-science/tracks/advanced-python/modules/ida-2-5-lambda-functions/lessons/lambda/exercises/intro-to-lambda


Question
Can we add a new column at a specific position in a Pandas dataframe?

Answer
Yes, you can add a new column in a specified position into a dataframe, by specifying an index and using the insert() function. 
By default, adding a column will always add it as the last column of a dataframe.

Say for example, we had a dataframe with five columns. If we wanted to insert a new column at the third position (index 2), 
we could do so like this:

# Third position would be at index 2, because of zero-indexing.
df.insert(2, 'new-col', data)
This will insert the column at index 2, and fill it with the data provided by data. When inserting, the columns from index 2 onward 
will effectively be shifted over to the right by 1 index each. The column that was previously at index 2 would now be at index 3 and 
so on for the following columns.


Question
When we store values such as True or False into a dataframe, are they stored as strings?

Answer
No, although the values may seem to be string types when printing out a dataframe, the values of True and False are stored as the 
bool type.

To see the data types that each column of your dataframe stores, you can utilize the .info() method, as covered in the previous 
lesson on Pandas.

One thing to keep in mind is that when inspecting the column data types using .info(), you will see types such as float64, bool, 
as well as object. The object data type means that the column can store any Python object. Columns that store more than one type of 
value, say a column that contains numbers and strings, will have a dtype of object.


Question
Can we utilize the apply() method in Pandas to update a dataframe in-place?

Answer
No, unlike other methods that update the dataframe for which you can specify in-place, such as

df.drop(['A'], inplace=True)
df.rename({'B' : 'C'}, inplace=True)

using the apply() method does not have the parameter for inplace.

As a result, whenever you use apply() on a dataframe, if you wish to update the dataframe, then you must reassign it, for example:

df = df.apply(my_lambda)


Question
In the context of this exercise 12, how might the example lambda functions be rewritten using the regular form, utilizing def?

Answer
Lambda functions can usually always be written in the normal Python function structure. This post will try to rewrite the example 
lambda functions in the normal Python function structure, which utilizes def and consists of multiple lines, as opposed to lambda 
functions which are always a single line.
For the first lambda function
mylambda = lambda x: (x * 2) + 3
Rewriting this using the def structure could be as follows:
def my_function(x):
  return (x * 2) + 3
For the second example lambda function
stringlambda = lambda x: x.lower()
We can rewrite this like:
def string_function(x):
  return x.lower()
If we generalize how this is done, basically, the parameters of the function are the parameters that follow right after the keyword lambda and before the colon :. For example, for this lambda, the parameters are x and y
sumlambda = lambda x, y: x + y
The returned value of the function is just what follows the colon :,
x + y.
Written using the normal structure, this would be
def sum_function(x, y):
  return x + y


Question
In the context of this exercise 13, the example lambda functions, which use an if/else statement, were written using a backslash (\). Do we always need to include backslashes when writing lambda functions using if/else?

Answer
No, you do not always need to include backslashes \ when you write lambda functions with if/else statements.
In Python, the backslash character \, also called the “line continuation character”, is used to join two lines of code. 
When you have a backslash at the end of a code line, Python will continue reading the next line of code as though the lines are part of a single line of code.
We use backslashes for the main purpose of making the code easier to read, by decreasing the length of the code lines. 
In particular, lambda functions can become quite long and hard to read because they are a single line, which is why we usually apply backslashes to divide them into multiple lines.

Example
# A statement as a single line
print 1 + 3

# The same statement split into multiple lines
print \
1 + \
3
One important thing to keep in mind is that there cannot be any characters or spaces after a backslash. A backslash must be the very last character of a code line. Otherwise, an error will be thrown.



Question
In the context of this exercise 8, how does the lambda function in the example work?

Answer
In this exercise, the lambda function given in the example was
lambda x: x.split('@')[-1]
A quick explanation of what this lambda function will do is, it will take in a string input value, which will be an Email address 
like "john.smith@gmail.com", and return the Email provider, "gmail.com".
To better understand how it accomplishes this, let’s work through each part:
First, it will use .split() to “split” the inputted string on the delimiter '@'. In Python, this will return a new list with 
the string split into substrings separated on any "@" which were in the string. So, given
x = "john.smith@gmail.com"

x.split('@')
returns the list
['john.smith', 'gmail.com']

Finally, the function will access the last element of this list, using index -1. If you recall, we can use negative index values to select elements from the last position, where -1 selects the last element, -2 selects the second to last, and so on.

# x = "john.smith@gmail.com"

x.split('@')[-1]
# = ['john.smith', 'gmail.com'][-1]
# = 'gmail.com'

If we use apply without specifying a single column and add the argument axis=1, the input to our lambda function will be an entire row, 
not a column. To access particular values of the row, we use the syntax row.column_name or row[‘column_name’].


Question
In the context of this exercise 23, in Pandas, when do we apply lambda functions to rows as opposed to columns of a dataframe?

Answer
Generally, we apply a lambda to rows, as opposed to columns, when we want to perform functionality that needs to access more than one 
column at a time.
Take for instance, the example function from the exercise:
lambda row: row['Price'] * 1.075 if row['Is taxed?'] == 'Yes' else row['Price']
As we can see, this lambda function is accessing multiple columns of the dataframe: Price and Is taxed?. Because it is accessing 
multiple columns, it would need to be able to access the entire row, instead of just a single column.
On the other hand, when applying a lambda function to a single column, the lambda will only apply to that column’s values. For example, 
from the previous exercise example:
df['Email Provider'] = df.Email.apply(lambda x: x.split('@')[-1] )
will apply the lambda function only on the values of the column df.Email, and not to any other columns.

Using rename with only the columns keyword will create a new DataFrame, leaving your original DataFrame unchanged. That’s why we also 
passed in the keyword argument inplace=True. Using inplace=True lets us edit the original DataFrame.


Question
In the lesson 14, we learned how to add columns to a dataframe, but what if wanted to remove them?

Answer
In addition to being able to add columns, we have the ability to remove columns of a dataframe in Pandas.

There are a few ways you can go about removing columns from a dataframe:

Creating a new dataframe, and including just the columns you want to keep from the original dataframe. For example, if we only wanted to include these columns from a dataframe, it effectively “removes” all the other columns not included:
new_df = df[['col1', 'col4']]

You can utilize the built-in drop() method, to delete a specific column. In order to drop a column, we must specify axis=1. We can do so as follows:
df.drop('col3', axis=1, inplace=True)

To drop multiple columns at once, we can enter in multiple column names as a list using drop(), like so:
df.drop(['col3', 'col5'], axis=1, inplace=True)


As we saw in the previous exercise, the groupby function creates a new Series, not a DataFrame. For our ShoeFly.com example, 
the indices of the Series were different values of shoe_type, and the name property was price.
Usually, we’d prefer that those indices were actually a column. In order to get that, we can use reset_index(). This will transform 
our Series into a DataFrame and move the indices into their own column.


Question
In the context of this exercise 4, can we merge on more than one specific column?

Answer
Yes, you can perform a merge on one column, or on multiple specified columns, by passing in a list of the column names for each dataframe.

When listing multiple column names, it will only return rows for which all the column values match. Furthermore, the number of columns listed must match, and the order they are listed will matter.

Example
# This will match the values for 
# column "a" with "c" 
# and column "b" with "d".

pd.merge(
  df1,
  df2,
  left_on=["a", "b"],
  right_on=["c", "d"]
)


Using plt.subplot(), the first parameter represents the number of rows of subplots, the second represents the number of columns, 
and the third representing the index of the subplot.
This diagram has 2 rows, and the second one has 2 columns. We will be selecting the box with index 4, since the first three were 
taken up by our previous graphs.



Question
In the context of this exercise 5 in Matplotlib, how can rows in a plot have different numbers of columns?

Answer
In order to understand how rows of a plot can have different numbers of columns, we first need to understand how the subplot essentially works.

When you apply subplot, you are not actually setting permanent dimensions for the layout of the plot grid.

Instead, think of it as though each time you use subplot, with some specified values, you are just creating a “virtual” or temporary grid layout placed on top of the entire plot area. After we place the subplot based on the layout of this grid, it is removed until we create a new subplot, with a new temporary grid.

For example, if we create a subplot as follows
ax1 = plt.subplot(2, 2, 1)
this will create a temporary 2x2 grid, and place the subplot at index 1 based on this 2x2 grid, which is the upper left.

And, if we wanted to add another subplot, say at the bottom right, we would do
ax2 = plt.subplot(2, 2, 4)
which again creates a temporary 2x2 grid, and places the subplot at index 4, which is the lower right area.

A way to visualize this would be

# [temp ] is used to signify temporary empty subplots
# when the virtual grid is applied.

# Adding ax1
[ ax1 ] [temp ]
[temp ] [temp ]

# Result plot
[ ax1 ]


# Adding ax2
[temp ] [temp ]
[temp ] [ ax2 ]

# Result plot
[ ax1 ] 
        [ ax2 ]
What essentially happens when we create a subplot is as follows:

It creates a temporary “virtual” grid on top of the entire plot area.

It places the subplot within the layout of that temporary grid at the specified index, based on that grid.

After the subplot is placed, that virtual or temporary grid disappears, and we have the subplots on the plot area, as we intended.

When we add another subplot, this process repeats.



Question
On a bar chart, what happens to the x-tick labels if the text becomes long?

Answer
When x-tick label strings become too long, you will not get any error messages. However, the label text will start to overlap with 
the other label text, which can make them hard to read.

To prevent the issue of labels overlapping, you might utilize the rotation parameter, which will rotate the text for each label. 
By rotating the text, the text is no longer stuck stretching out horizontally but will stretch out on an angle, which will prevent overlap with the other labels.

Another way to prevent the issue of overlap is by avoiding it entirely. This can be done by choosing label text lengths that are 
not too long. You might do this by abbreviating terms.

Having label text that is easy to read is important so that other people will also be able to read and understand the information 
displayed on your graphs.



Question
In the context of this exercise 6, how does this list comprehension in the example work?

[t*element + w*n for element in range(d)]

Answer
The list comprehension provided in the example code returns a list of x values for the bar locations in the graph.

There are 4 variables which will let us do this:
n determines which dataset it is currently for.
t determines the total number of datasets to graph side by side.
d tells us how many bars there are per dataset.
w tells us the width of each individual bar.

If we take the provided values for the first dataset China Data, we get
[2*element + 0.8*1 for element in range(7)]

This essentially means, for each element in range(7), construct a list where each element is
2*element + 0.8

This would give us this list of values,
[0.8, 2.8, 4.8, 6.8, 8.8, 10.8, 12.8]

If we change n to 2 for the second dataset US Data, it gives us the list
[1.6, 3.6, 5.6, 7.6, 9.6, 11.6, 13.6]

These x values will position each pair of bars for each set of data next to each other in a clear way.



Question
In the context of this exercise 2, when do we use each type of graph shown?

Answer
Depending on what you are trying to convey visually with data, certain graphs can be better suited for the task. The following are 
brief summaries of each graph and when you might apply them.

A bar chart with error has the qualities of a bar chart, which lets us see categorical data. The heights of each bar can represent 
the average of values in the category, and with the addition of error bars, we can see the range of all values from smallest to largest represented by the bottom and top lines of the error bar. You might use this to display the average grade of students categorized by college major.

A line chart with error has the qualities of a line chart, which lets us display values for a sequence of data points, connected 
with straight lines. The added shaded error lets us see a lower and upper bound that the values can fall between, similar to the bar 
chart with error. You might use this to show stock prices over time.

Histograms let us see frequencies of variables that fall within intervals, which we refer to as “bins”. The one displayed in this 
exercise is a specific type called a normalized histogram, such that the total area of all the rectangles in the histogram sum to 1. 
You might use histograms to show how many people there are within different age ranges in years, like 10-20, 20-30, and so on.

A pie chart lets us see how values contribute to a whole, like slices of a pie. Each wedge size is proportional to the fraction of 
each value of the total value. You might use a pie chart when showing the percentages of students in different college majors.

Side by side charts are bar charts where different sets of data are shown next to each other. This is useful to directly visualize 
and compare multiple sets of data with each other. You might use this to compare the average grades of students based on college major 
from different colleges.

Last, but not least, stacked bars allow us to see how individual values contribute toward a total value, similar to pie charts, but 
displayed as a vertical column and without the restriction of a set size, as you can keep adding to the bar’s total height. You might use stacked bars when showing the hours spent studying for different classes per day. The total height of each column would be total hours spent studying that day.



Question
In the context of this exercise 69, what do the horizontal and vertical axes represent in a KDE plot?

Answer
For this lesson, the KDE plots we work will be using univariate data. So, only one of the axes will represent actual values in the data.

The horizontal or x-axis of a KDE plot is the range of values in the data set. This is similar to the x axis for histograms.

The vertical or y-axis of a KDE plot represents the Kernel Density Estimate of the Probability Density Function of a random variable, 
which is interpreted as a probability differential. The probability of a value being between the points x1 and x2 is the total shaded 
area of the curve under the two points.



Question
In the context of this exercise 31, how do we read a violin plot to determine its distribution type?

Answer
When reading a violin plot, the distributions are essentially just rotated vertically rather than horizontally, and then mirrored on 
the left and right sides.

To read the distributions from a violin plot, we just need to reverse these steps. We can rotate the plots so that the values are on 
the x axis, and in increasing order from left to right. Then, you can ignore the mirrored side below the x axis, and read the 
distribution shape as you normally would, for the top half.

Keeping this in mind, we can determine the shapes of the example violin plots in the exercise:

Dataset 1 (Blue) is unimodal and has most of its data on the right, so it must be skewed left.

Dataset 2 (Green) is unimodal and seems to be symmetric and normal.

Dataset 3 (Red) appears to be bimodal.


Question
What are some differences between an array and a list?

Answer
In Python, an array, or NumPy Array, and list share many similarities, but they also have some important differences on how they can be used.

Both arrays and lists can hold multiple items of any type. You can also access individual items by indexes.

One important, and probably the main difference, between them is that you can perform operations on an array, like addition, multiplication, and subtraction, like you would a vector in mathematics.

This means that if you have an array of numbers, you can add a single number to every value in the array with one operation. With a list, operations cannot be applied on every single element like for an array, and might even cause errors.

Arrays also provide several other useful functionality, which you will learn throughout this lesson.

Example
test = np.array([1, 2, 3, 4, 5])
test += 10

# The array is now [11, 12, 13, 14, 15]


Question
Can we perform operations between 1-D and 2-D NumPy Arrays?

Answer
Yes, when performing an operation between a 1-D and a 2-D NumPy Array, it will essentially perform the operation on the 1-D array with each row of the 2-D Array individually.

As a result, it is only possible if the number of elements for every row in both Arrays match.

For example, these two arrays have 2 elements in each row, so you can perform an operation on them.

# When we perform an operation on these arrays, 
# it is essentially running the operation 
# on each row of the 2-D list with the 1-D list.
arr1 = np.array([[1, 1], [2, 2], [3, 3]])
arr2 = np.array([10, 10])

arr1 * arr2
# The result of running the above is
# [[10 10]
#  [20 20]
#  [30 30]]


Question
When selecting elements from a 1-D NumPy Array, is there a way to skip elements?

Answer
Yes, actually, selecting elements from a 1-D Array is similar to list or string slicing.

Just like when slicing a list or string, we can include a third value, which is the step value, or the number of indexes to increment for each item in the new list or substring.

Code
# By default, step is 1, and selects each item 
# in the range of indexes.
test = np.array([92, 94, 88, 91, 87])

print test[0:5] 
# [92, 94, 88, 91 87]

# With a step of 2, it will skip every other element.
print test[0:5:2] 
# [92, 88, 87]


Question
Without initially knowing the dimensions of a 2-D Array, how could we get the last element?

Answer
Assuming that the 2-D Array has the same number of elements for each row, such that it is an Array of size M x N, we could do this using the len() function. The len() function works the same way for arrays as it does for lists in Python.

First, we can get the last row index like so.
len(array) - 1

And since each row has the same number of elements, we can get the index of the final column like so.
len(array[0]) - 1

Putting this together, selecting the last, or bottom-right most, element is done with
array[len(array) - 1, len(array[0]) - 1]


Question
In the context of this exercise 14, what is an axis in Numpy?

Answer
An axis is similar to a dimension. For a 2-dimensional array, there are 2 axes: vertical and horizontal.

When applying certain Numpy functions like np.mean(), we can specify what axis we want to calculate the values across.

For axis=0, this means that we apply a function along each “column”, or all values that occur vertically.

For axis=1, this means that we apply a function along each “row”, or all values horizontally.

Example
# Given the following 2-dimensional array
values = np.array([
[10, 20, 30, 40],
[50, 60, 70, 80],
])

# Axis=0
# along each "column"
print np.mean(values, axis=0) 
# [30, 40, 50, 60]

# Axis=1
# along each "row"
print np.mean(values, axis=1)
# [25, 65]


Question
In the context of this exercise 6, what happens to the dataset when the standard deviation is small or large?

Answer
When the standard deviation is small, the values will be less spread out and be closer to the mean. This will cause the overall shape of this dataset to appear less chaotic 
and more leveled.

When the standard deviation is large, the values will be more spread out from the mean. The shape of the dataset will appear to be more uneven and chaotic as the standard 
deviation increases.


Question
In the context of this exercise 6, are standard deviations relative to the data they are from?

Answer
Yes, this is because a standard deviation depends on the dataset values.

If you have a set of large numbers and a set of small number, both with a similar distribution shape, the standard deviation of the larger numbered dataset is most likely 
going to have a larger standard deviation because the values themselves are larger.

In this exercise, our data for pumpkin is roughly 10 times larger than the values in acorn_squash, with the values somewhat similarly spread out. As a result, the standard 
deviation will most likely be bigger for the larger numbered dataset.

If you wanted to make the comparison somewhat closer, you might consider normalizing or scaling the datasets to be around the same scale when comparing the standard 
deviations.


Question
What are some important differences between standard deviation and interquartile range?

Answer
Standard Deviation
The standard deviation takes into account all the values of a dataset, including any outliers. It is dependent on the mean, because the value is used to tell how much the 
data deviates from the mean of a dataset.

The standard deviation is also important when we need to utilize the variance of a dataset, which is necessary to do things like linear regression or other analysis of data.

Because the standard deviation is affected by skewed data, it can be more reliable when the data is normalized and not skewed.

Interquartile Range
The Interquartile Range tells us how spread the data is. The larger this value is, the more spread out the data is, and conversely, the smaller the value, the less spread 
the data is.

Unlike the standard deviation, however, it does not take into account all the values in the dataset, but mainly their positions when the data is ordered. It is not affected 
as much by outliers or data that is skewed or not normalized.

Ultimately, using both when analyzing data can sometimes be better than only using one value, and we can obtain more insight by observing both.

Question
In the context of this exercise 10, how does np.mean() give us the probability?

Answer
The np.mean() function is generally used to get the average of all values in a dataset. We can apply this function with a logical statement to get the percent of values that satisfy the logical statement.

In the exercise example, we have np.mean(a==4). First, this will evaluate the conditional, a==4, which will return a list of True and False values. Then it will run np.mean() on that list of True and False values. When running np.mean() on a list of True and False values, True = 1, False = 0 during the calculation.

Because True values count as 1, this is like counting how many elements satisfy the logical statement, and the calculation is essentially:

(Number elements satisfying condition) / (Number total elements)

Example
# a = [4, 3, 1, ..., 4]
np.mean(a==4)
=
np.mean([True, False, False, ..., True])

# In Numpy functions, 
# True  counts as 1
# False counts as 0

# This is then equivalent to calculating
np.mean([1, 0, 0, ..., 1])

# Example:
# There are 10000 total elements
# 5000 elements equal to 4
np.mean(a==4)
= 
5000 / 10000 = 0.5 or 50% probability 



Question
What are some important differences between a Normal and Binomial Distribution?

Answer
Normal Distribution
Normal distributions are more common in statistics than binomial distributions most of the time. These distributions are always symmetric and unimodal by definition.

Normal distributions can be described by their mean and standard deviation. The mean determines where the center of the distribution is located. The standard deviation determines the shape of the distribution. A larger standard deviation means a wider and flatter shape, while a smaller standard deviation means a skinnier shape.

Furthermore, unlike binomial distributions, a normal distribution is based on the values of a dataset.

An example of a normal distribution is for the heights of people in a country.

Binomial Distribution
These distributions tell us the probability for a specific number of “successes” to happen, given a probability of success and number of trials.

Unlike normal distributions, binomial distributions tell us the results of only two possible outcomes: success or failure.

An example of this is flipping a coin, which can only result in heads or tails.


Regular expressions are special sequences of characters that describe a pattern of text that is to be matched
We can use literals to match the exact characters that we desire
Alternation, using the pipe symbol |, allows us to match the text preceding or following the |
Character sets, denoted by a pair of brackets [], let us match one character from a series of characters
Wildcards, represented by the period or dot ., will match any single character (letter, number, symbol or whitespace)
Ranges allow us to specify a range of characters in which we can make a match
Shorthand character classes like \w, \d and \s represent the ranges representing word characters, digit characters, and whitespace characters, respectively
Groupings, denoted with parentheses (), group parts of a regular expression together, and allows us to limit alternation to part of a regex
Fixed quantifiers, represented with curly braces {}, let us indicate the exact quantity or a range of quantity of a character we wish to match
Optional quantifiers, indicated by the question mark ?, allow us to indicate a character in a regex is optional, or can appear either 0 times or 1 time
The Kleene star, denoted with the asterisk *, is a quantifier that matches the preceding character 0 or more times
The Kleene plus, denoted by the plus +, matches the preceding character 1 or more times
The anchor symbols hat ^ and dollar sign $ are used to match text at the start and end of a string, respectively


Convergence
How do we know when we should stop changing the parameters m and b? How will we know when our program has learned enough?
To answer this, we have to define convergence. Convergence is when the loss stops changing (or changes very slowly) when parameters are changed.



Kaggle:

we can specify a value for sep to put some special string in between our printed arguments:
print(1, 2, 3, sep=' < ')
1 < 2 < 3
But if we don't specify a value, sep is treated as having a default value of ' ' (a single space).
print(1, 2, 3)
1 2 3


By default, max returns the largest of its arguments. But if we pass in a function using the optional key argument, it returns the argument x that maximizes key(x) (aka the 'argmax').

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)
Which number is biggest?
100
Which number is the biggest modulo 5?
14



"""

