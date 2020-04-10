--Using the same pattern from the example above, find flight information about flights where the origin elevation is less than 2000 feet.

SELECT dep_month, dep_day_of_week, dep_date, 
SUM(distance) flight_distance, COUNT(*) flight_count
FROM flights
GROUP BY 1,2,3
ORDER by 5 DESC;


--Using the same pattern, find flight information about flights where 
--the Federal Aviation Administration region (faa_region) is the Southern region (ASO).

SELECT dep_month, dep_day_of_week, dep_date, 
SUM(distance) flight_distance, COUNT(*) flight_count
FROM flights
GROUP BY 1,2,3
ORDER by 5 DESC;


--Using a subquery, find the average total distance flown by day of week and month.
--Be sure to alias the outer query as average_distance and the inner query as flight_distance.\

SELECT dep_month, dep_day_of_week, AVG(flight_distance), flight_count
FROM(SELECT dep_month, dep_day_of_week, dep_date, 
SUM(distance) flight_distance, COUNT(*) flight_count
FROM flights
GROUP BY 1,2,3
ORDER by 5 DESC)
GROUP BY 1,2
ORDER by 4 DESC;


--Find the id of the flights whose distance is below average for their carrier.

SELECT id
FROM flights f
WHERE distance <
(
  SELECT AVG(distance)
  FROM flights
  WHERE carrier = f.carrier
);


--Using the same pattern, write a query to view flights by origin, flight id, and sequence number. 
--Alias the sequence number column as flight_sequence_number.

SELECT origin, id,
    (SELECT COUNT(*)
FROM flights f
WHERE f.id < flights.id
AND f.origin=flights.origin) + 1
 AS flight_sequence_number
FROM flights;


--Using the same pattern, utilize a subquery to find the average sale price over both order_items and order_items_historic tables.

SELECT id, AVG(sale_price)
FROM(
SELECT id, sale_price FROM order_items
UNION ALL
SELECT id, sale_price FROM order_items_historic)
GROUP BY 1;


Select the items in the category column that are both in the newly acquired new_products table and the legacy_products table.

SELECT category FROM new_products
INTERSECT
SELECT category FROM legacy_products;


Find the percentage of high elevation airports (elevation >= 2000) by state from the airports table.
In the query, alias the percentage column as percentage_high_elevation_airports.

SELECT state, 
    (100.0*(COUNT(CASE WHEN elevation >= 2000 THEN elevation ELSE NULL END))/COUNT(elevation)) as percentage_high_elevation_airports FROM airports
GROUP BY state;


