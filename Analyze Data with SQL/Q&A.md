Question
In the context of this exercise 52, can we add a column at a specific position to a table?
Answer
No, unfortunately, you cannot specify what position to add a column to a table.
By default, a new column will always be added at the end of the table. 
For most intents and purposes, this should not affect much, since you can always select the columns in any order, 
for instance, like
SELECT col3, col1, col2
If column order is very important, then an alternative is to create a new table and add the columns in the specific order they should appear.


Question
In the context of this exercise 75, how is ALTER different from UPDATE?
Answer
Although similar in the sense that both statements will modify a table, these statements are quite different.
The ALTER statement is used to modify ![#1589F0](https://placehold.it/15/1589F0/000000?text=+)columns![#1589F0](https://placehold.it/15/1589F0/000000?text=+). With ALTER, you can add columns, remove them, or even modify them.
The UPDATE statement is used to modify ![#1589F0](https://placehold.it/15/1589F0/000000?text=+)rows![#1589F0](https://placehold.it/15/1589F0/000000?text=+). However, UPDATE can only update a row, and cannot remove or add rows.


The DELETE FROM statement deletes one or more rows from a table. 
SQL is case-insensitive for text values.

Question
Can we alias multiple columns in a single query?
Answer
Yes, you can alias multiple columns at a time in the same query.
It is advisable to always include quotes around the new alias. Quotes are required when the alias contains spaces, punctuation marks, special characters or reserved keywords. It is simply more convenient to always include quotes around the new alias.
Example
SELECT course_id AS "Course ID", exercise_id AS "Exercise ID"
FROM bugs;


Question
When using SQL LIKE operators, how do we search for patterns containing the actual characters “%” or “_”?
Answer
When searching for a pattern containing the specific characters % or _, we can utilize the escape character \, similarly to its use in Python.
If we want to search for these specific characters, we can simply add the escape character immediately before them.
Example
/* 
In this pattern, we use an escape character before '%'.
This will only match "%" and not be used like the
wildcard character.
This query will match any titles that end with
' 100%'.
*/
SELECT *
FROM books
WHERE title LIKE '% 100\%';


LIKE is not case sensitive. ‘Batman’ and ‘Man of Steel’ will both appear in the result of the query 'man' above.


Question
When storing missing data, should I store them as NULL?
Answer
It can depend entirely on how you need the data to be stored and utilized.
Let’s say that you have a table of employee information, which included their address. Say that we wanted to check all rows of this table and find where any addresses are missing. If we stored the addresses as TEXT values, we might choose to store all the missing values as either '' or as NULL.
If we stored the missing address values as an empty string '' then these values are not NULL. Empty strings are seen as a string of length 0. So, if we ran a query using
WHERE address IS NULL
it would not give us the rows with missing address values. We would have to check using
WHERE address = ''
With a table containing many different data types, it may be helpful and more convenient to store any missing values in general as just NULL so that we can utilize the IS NULL and IS NOT NULL operators.


The BETWEEN operator is used in a WHERE clause to filter the result set within a certain range. It accepts two values that are either numbers, text or dates.
When the values are text, BETWEEN filters the result set for within the alphabetical range.
In this statement, BETWEEN filters the result set to only include movies with names that begin with the letter ‘A’ up to, but not including ones that begin with ‘J’.
SELECT *
FROM movies
WHERE name BETWEEN 'A' AND 'J';
However, if a movie has a name of simply ‘J’, it would actually match. This is because BETWEEN goes up to the second value — up to ‘J’. So the movie named ‘J’ would be included in the result set but not ‘Jaws’.


Question
In SQL, when applying the BETWEEN operator on a range of TEXT values, each value must be compared somehow to be ordered correctly. What kind of comparison is done on TEXT values?
Answer
In most programming languages, including SQLite and Python, TEXT or string values are compared based on their lexicographical ordering, and when using the BETWEEN operator for a range of TEXT values in SQL, the values will be sorted in this way.
Lexicographical ordering is basically the ordering you would find words in a dictionary. If we had two words, they would be compared starting from their first letter, second letter, and so on, until we find a non-matching letter. The word which has the letter that comes first in the alphabet would ultimately be sorted to come first in this lexicographical ordering.
If two words have different lengths, but match up to the last letter of the shorter word, the shorter word will appear first in the ordering.
Example
A = "Alien"
B = "Aliens"
C = "Alike"
/* 
   Because A and B share the same sequence of characters 
   up to the last character of A, which is shorter, A < B. 
   Also, because "k" comes after "e" in the alphabet, C will 
   come last in the ordering of these 3 words.
   A < B < C
*/


Question
Is the AND used in BETWEEN the same as the AND operator used between multiple conditions?
Answer
No, although they may be assumed to be the same thing, the AND used with a BETWEEN, like
BETWEEN 1990 AND 1999
is not quite the same AND used when combining multiple conditions. When used in a BETWEEN statement, we are not combining two separate conditions, but providing a range of values to obtain the values within that range.
However, we can easily rewrite a BETWEEN to one with two conditions, like these queries which would be identical.
SELECT *
FROM movies
WHERE year BETWEEN 1990 AND 1999;
SELECT * 
FROM movies
WHERE year >= 1990
AND year <= 1999;


