#Multi line comments are written like this:

""" 
Several
Lines
"""

"""
How can I use quotes inside of a string? - FAQ / Python FAQ - Codecademy Forums
https://discuss.codecademy.com/t/how-can-i-use-quotes-inside-of-a-string/448684
"""

"""
Notice that when we perform division, the result has a decimal place. 
This is because Python converts all ints to floats before performing division. 
In older versions of Python (2.7 and earlier) this conversion did not happen, and integer division 
would always round down to the nearest integer."""

#Q
print("total squares needed:" + quilt_width * quilt_length )
#I got the following error
"""
#A
You use + to attempt string concatenation, but you don’t have two strings. Thus you get an error.
So either you will need to convert the integer to a string, so you can stick with your current approach (using +).
The problem is that using + to add number and string together, will result in a TypeError, 
you can add these two types together. these types don’t go together, just like certain things don’t go together.
you can use a comma (,) instead of a + to overcome your problem. 
"""
