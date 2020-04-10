SQL lets us use column reference(s) in our GROUP BY that will make our lives easier.

1 is the first column selected
2 is the second column selected
3 is the third column selected
and so on.

The DELETE FROM statement deletes one or more rows from a table. 

SQL is case-insensitive for text values.

LIKE is not case sensitive. ‘Batman’ and ‘Man of Steel’ will both appear in the result of the query 'man' above.

COUNT() is used to take a name of a column, and counts the number of ![#1589F0](https://placehold.it/15/1589F0/000000?text=+)non-empty![#1589F0](https://placehold.it/15/1589F0/000000?text=+) values in that column.

The BETWEEN operator is used in a WHERE clause to filter the result set within a certain range. It accepts two values that are either numbers, text or dates.
When the values are text, BETWEEN filters the result set for within the alphabetical range.
In this statement, BETWEEN filters the result set to only include movies with names that begin with the letter ‘A’ up to, but not including ones that begin with ‘J’.
SELECT *
FROM movies
WHERE name BETWEEN 'A' AND 'J';
However, if a movie has a name of simply ‘J’, it would actually match. This is because BETWEEN goes up to the second value — up to ‘J’. So the movie named ‘J’ would be included in the result set but not ‘Jaws’.

The WHERE clause filters rows, whereas the HAVING clause filter groups.

SQL has strict rules for appending data:(UNION)
Tables must have the same number of columns.
The columns must have the same data types in the same order as the first table.

Difference between UNION and UNION ALL
Whether include duplicate rows.

The WITH statement allows us to perform a separate query (such as aggregating customer’s subscriptions)

Subqueries are used to complete an SQL transformation by nesting one query within another query.
A non-correlated subquery is a subquery that can be run independently of the outer query and can be used to complete a multi-step transformation.
A correlated subquery is a subquery that cannot be run independently of the outer query. The order of operations in a correlated subquery is as follows:
1. A row is processed in the outer query.
2. Then, for that particular row in the outer query, the subquery is executed.

INTERSECT is used to combine two SELECT statements, but returns rows only from the first SELECT statement that are identical to a row in the second SELECT statement. 
This means that it returns only common rows returned by the two SELECT statements.
It's the same like show distinct column by inner join.

EXCEPT is constructed in the same way, but returns distinct rows from the first SELECT statement that aren’t output by the second SELECT statement.

Aggregate functions compute a single result from a set of multiple input values. You can think of aggregate data as data collected from multiple rows at a time. In this lesson, we’ll continue learning about aggregate functions by focusing on conditionals, sums, and combining aggregate functions.

Conditional Aggregates are aggregate functions that compute a result set based on a given set of conditions.

Date Functions:

DATETIME; Returns the date and time of the column specified. This can be modified to return only the date or only the time.
DATETIME(time1, +X hours, Y minutes, Z days): Increments the specificed column by a given number of hours, minutes, or days.
Numeric Functions:

(number1 + number2);: Returns the sum of two numbers, or other mathematical operations, accordingly.
CAST(number1 AS REAL) / number2;: Returns the result as a real number by casting one of numeric inputs as a real number
ROUND(number, precision);: Returns the numeric value rounded off to the next value specified.
String Functions:

'string1' || ' ' || 'string2';: Concatenates string1 and string 2, with a space between.
REPLACE(string,from_string,to_string): Returns the string with all occurrences of the string from_string replaced by the string to_string.


--When the columns to join have the same name in both tables you can use using instead of on. 
--Our use of the using keyword is in this case equivalent to this clause:

from daily_revenue
  join daily_players using (dt);
  
 from daily_revenue
  join daily_players on
    daily_revenue.dt = daily_players.dt;


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


Question
Is there a limit to the number of columns a table can have?
Answer
Yes, there is a limit to the number of columns a table can have.
In SQLite in particular, the upper bound for this number of columns is stored in a parameter called SQLITE_MAX_COLUMN, and by default, it is set to 2000 columns.
This value can be changed during compile time and can be set up to a maximum value of 32767. However, realistically, your tables will probably never need these many columns, but, it is available as an option if ever needed.


Question
In the context of this exercise 2, are 0 and "" empty values?
Answer
No, although logically, we may think that 0 represents some empty number or count, or that "" represents an empty text, which is not wrong, this does not mean they are empty values. In SQL tables, they are still considered to be values.
Instead, empty values in SQL would be represented with NULL, which means the absence of any value.


Question
In the context of this lesson 1, are identifiers, like the id column, always numerical values?
Answer
No, identifiers of a table do not always have to be numerical values. It is most common to use numerical values because the values are easy to keep track of, and for each new row, we simply increment the number by 1, but it is not absolutely necessary.
Instead of numerical values, you can use non-numerical values, such as text values or even dates, as long as they are unique for each row. You can even use multiple columns, in combination, to determine an identifier for each row.
For an example of a non-numerical identifier, consider a table of employees, with a column for emails, which can be used as the id column because each employee has a unique email. Another example is a table of transactions, where dates are specified to milliseconds that they were applied. Transactions cannot happen at the same time, so these dates might be used as the identifier.


Question
In the context of this code challenge 4, do we have to select the column which we are ordering by in a SQL statement?
Answer
No, you do not have to select the column, or columns, that you are applying the ORDER BY clause on. For example, if you were applying the clause like so,
ORDER BY column_1
you do not have to select column_1 in your statement.
Most of the time, for the sake of clarity of how the data is being ordered, it might make sense to include that column in your SELECT statement, but it is not absolutely necessary. The following would be valid,
SELECT column_1, column_2
FROM table
ORDER BY column_3;


Question
In the context of this code challenge 1, can we match for a specific casing of text?
Answer
Yes, this is possible.
By default, text matching using LIKE is case-insensitive, however we can utilize a special type of statement in SQLite, known as a PRAGMA statement. PRAGMA statements are a specific type of statement in SQLite, and can be used to modify certain behaviors of the available functionality.
The following is an example of how it can be applied.
/* Run this statement to allow case-sensitive
matching on the LIKE operator */
PRAGMA case_sensitive_like = true;
/* This statement will now only match text that 
contains the exact casing of "Code" */
SELECT *
FROM table
WHERE column LIKE '%Code%';


Question
When using the SQL COUNT() function for a column, does it include duplicate values?
Answer
Yes, when using the COUNT() function on a column in SQL, it will include duplicate values by default. It essentially counts all rows for which there is a value in the column.
If you wanted to count only the unique values in a column, then you can utilize the DISTINCT clause within the COUNT() function.
Example
/* This will return 22, the number of distinct category values. */
SELECT COUNT(DISTINCT category)
FROM fake_apps;


Question
If multiple rows have the minimum or maximum value, which one is returned when using MAX/MIN?
Answer
Typically, when you have more than one row that contains the minimum or maximum value in a column, the topmost row containing that value will be returned in the result.
For example, if the table contained multiple rows with the minimum price of 0.0, then the result of a query with MIN(price) will choose the topmost row from the table that had this price value.


Question
What’s the difference between COUNT(1), COUNT(*), and COUNT(column_name)?
Answer
It’s important to note that depending on the ‘flavor’ of SQL you are using (MySQL, SQLite, SQL Server, etc.), there may be very slight differences in performance between COUNT(1) and COUNT(*), but generally speaking COUNT(1) and COUNT(*) will both return the number of rows that match the condition specified in your query.
As for COUNT(column_name), this statement will return the number of rows that have a non-null value for the specified column.
Let’s say we have the following table called people:
When we run either of these queries:
SELECT COUNT(1) FROM people;
SELECT COUNT(*) FROM people;
we’re going to get a result of 3 because there are three rows in the table. But If we run this query:
SELECT COUNT(favorite_color) FROM people;
we will get a result of 2 because the third row contains a value of NULL for favorite_color, therefore that row does not get counted.


Question
What do the numbers refer to in a statement like ‘GROUP BY 1’ or ‘ORDER BY 2’?
Answer
When you see numbers after a GROUP BY or ORDER BY statement, they are referring to the columns that were selected in the query. These are called column reference numbers. The 1 signifies the first column selected, the 2 signifies the second column selected, and so on. Here’s an example:
SELECT alpha, bravo, charlie FROM table GROUP BY 1 ORDER BY 2;
In this query, 1 is referring to alpha and 2 is referring to bravo.
The main reason we use column reference numbers is because sometimes it can be a pain to type out a really long or complex column name. As you can imagine, it’s a whole lot easier typing a number than something like customer_order_number.


Question
With SQL functions like ROUND, if a parameter is optional, should you still provide a value for it?
Answer
Before I can give an answer to this question, it’s important to note that the documentation for functions like ROUND can slightly differ depending on the flavor of SQL you are using. In the SQLite documentation 39, we can see that the second parameter for the ROUND function is optional, whereas the SQL Server documentation 38 shows that same parameter as required. Always make sure you’re checking the proper documentation!
As for the original question, it’s really up to you as the programmer to decide, you just have to be consistent with your decision. If you provide a value for an optional parameter, you should be doing that everywhere else in your code. The only real benefit to including a default value for an optional parameter is that it’s more explicitly clear as to what’s going on. Imagine someone reading your code who isn’t all that familiar with SQL, they might be able to get a better idea of what’s going on if you do provide values for the optional parameters.


Question
Is it possible for a table to have more than one unique identifier column, like an id column?
Answer
Yes, it is possible for a table to have more than one column which can uniquely identify a row of data. A column that can uniquely identify a record of data is known as a "Candidate Key". Tables can have multiple "Candidate Key"s, each of which could potentially be the "Primary Key", but there must only be one "Primary Key" per table. Usually, the column chosen as the "Primary Key" follows the naming convention like customer_id or product_id.
For example, say that we had a table of employee records, with the columns employee_id and phone_number. Every employee has a unique employee_id value, and a unique phone_number value. Both of these columns can be unique identifiers for a row, so they are "Candidate keys", but the "Primary Key" would most likely be set to employee_id.


Question
What happens if the tables we perform the UNION operator on have duplicate rows?
Answer
When you combine tables with UNION, duplicate rows will be excluded.
To explain why this is the case, recall a Venn Diagram, which shows the relations between sets. If we perform UNION on two sets of data (tables), say A and B, then the data returned in the result will essentially be
A + B - (A intersect B)
In the first part,
A + B
will add together all the rows of both tables, including duplicates.
The second part,
- (A intersect B)
will remove every duplicate, which is where A and B intersected.
If, however, you wanted to include duplicates, certain versions of SQL provides the UNION ALL operator.


Question
Can we use WITH for more than one nested query in SQL?
Answer
Yes, you can use WITH for more than one nested query. You can do so by listing each query using commas after the WITH.
For example,
WITH
query1 AS (SELECT column1 FROM table1 WHERE condition1),
query2 AS (SELECT column2 FROM table2 WHERE condition2)


When dividing, we need to be sure to multiply by 1.0 to cast the result as a float:
SELECT 1.0 * 
(
  SELECT COUNT(*)
  FROM subscriptions
  WHERE subscription_start < '2016-12-01'
  AND (
    subscription_end
    BETWEEN '2016-12-01'
    AND '2016-12-31'
  )
) / (
  SELECT COUNT(*) 
  FROM subscriptions 
  WHERE subscription_start < '2016-12-01'
  AND (
    (subscription_end >= '2016-12-01')
    OR (subscription_end IS NULL)
  )
) 
AS result;
