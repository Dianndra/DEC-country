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
