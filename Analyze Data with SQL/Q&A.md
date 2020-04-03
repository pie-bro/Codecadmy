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

