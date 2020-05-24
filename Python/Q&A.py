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










"""

