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






















"""

