--how many countries speak french
SELECT COUNT("Languages")
FROM country_data
WHERE "Languages" LIKE '%French%';


--how many countries speak english
SELECT COUNT("Languages")
FROM country_data
WHERE "Languages" LIKE '%English%';


--how many country have more than 1 official language
SELECT COUNT("Languages")
FROM country_data
WHERE "Languages" LIKE '%,%';


--how many country official currency is euro
SELECT COUNT("Currency_name")
FROM country_data
WHERE "Currency_name" LIKE '%Euro%';

-- How many country is from West europe
SELECT COUNT(*)
FROM country_data
WHERE "Sub_region" = 'Western Europe';

-- How many country has not yet gain independence
SELECT COUNT(*)
FROM country_data
WHERE "Independence" is False;

-- How many distinct continent and how many country from each
SELECT "Continents", COUNT("Country_name")
FROM country_data
GROUP BY "Continents";

SELECT  COUNT(DISTINCT "Continents") 
FROM country_data;

-- How many country whose start of the week is not Monday
SELECT COUNT("Start_Of_Week") 
FROM country_data
WHERE "Start_Of_Week" != 'monday';

-- How many countries are not a United Nation member
SELECT COUNT(*)
FROM country_data
WHERE "United_Nation_members" is False;

-- How many countries are United Nation member
SELECT COUNT(*)
FROM country_data
WHERE "United_Nation_members" is True;

-- Least 2 countries with the lowest population for each continents
SELECT "Country_name", "Population"
FROM country_data
ORDER BY "Population" ASC
LIMIT 2;

-- Top 2 countries with the largest Area for each continent
WITH temp_table AS 
	(SELECT "Country_name", "Continents", "Area", ROW_NUMBER() OVER(PARTITION BY "Continents" ORDER BY "Area" DESC) AS row_num
	FROM country_data)
SELECT *
FROM temp_table
WHERE row_num < 3;

-- Top 5 countries with the largest Area
SELECT "Country_name", "Area"
FROM country_data
ORDER BY "Area" DESC
LIMIT 5;

-- Top 5 countries with the lowest Area
SELECT "Country_name", "Area"
FROM country_data
ORDER BY "Area" ASC
LIMIT 5;
