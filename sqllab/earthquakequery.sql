-- Find all of the earthquakes with a magnitude over 7
SELECT * FROM earthquakes WHERE mag > 7;

-- Find all of the earthquakes that occurred on the second of the month with a magnitude > 4
SELECT * FROM earthquakes WHERE extract(day from quaketime) = 2 AND mag > 4;

-- Find all of the earthquakes that occurred in the Philippines
SELECT * FROM earthquakes WHERE longitude BETWEEN 116 AND 126 AND latitude BETWEEN 4 AND 21;

-- Find all earthquakes that happened in Indonesia between 9am and 3pm Central Indonesian Time (GMT + 8)
SELECT * FROM earthquakes WHERE longitude BETWEEN 95 AND 141 AND latitude BETWEEN -11 AND 5 AND extract(hour from quaketime) BETWEEN 1 AND 7;