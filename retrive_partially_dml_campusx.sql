select * from campusx.smartphones_cleaned_v6 where 1;
 -- this gives all the columns and the rows in the table 
 -- where 1 means we dont want to do any operation
 
 
 SELECT os AS 'Operating System',model,battery_capacity AS 'battery_capacity(mah)' FROM campusx.smartphones_cleaned_v6;
 -- as is used to display the column name like the way we want when we are extracting the subset of our dataset
-- star hatake columns ka naam likh do jo chahiye to fetch the columns which you want


SELECT model,
sqrt(resolution_width*resolution_width + resolution_height*resolution_height)/screen_size AS 'Pixel_Per_Inch'
from campusx.smartphones_cleaned_v6;
-- here we can see how to perform a mathemaical operation on and derive a new columns from the xisting ones


SELECT model,'smartphone' AS 'Type' from campusx.smartphones_cleaned_v6;
-- here we used as to create a new column names type with all the values as smartphones


SELECT distinct(brand_name) as "Brands" from campusx.smartphones_cleaned_v6;
-- to get all the unique values inside the brand_name column 


select distinct brand_name,os from campusx.smartphones_cleaned_v6;
-- this is to get the the distinct combinations present in among the columns


SELECT * FROM campusx.smartphones_cleaned_v6 where price > 50000;
-- this is used to get the rows based on certain condition where is used to achieve this


SELECT * FROM campusx.smartphones_cleaned_v6 where price > 50000 and price < 70000;
-- this is used as a between operator but there is another way also 
SELECT * FROM campusx.smartphones_cleaned_v6 where price between 50000 and 60000;
-- another way of doing that


SELECT * FROM campusx.smartphones_cleaned_v6 where price < 15000 and rating>80;
-- multiple criteria for filtering 


select * from campusx.smartphones_cleaned_v6 where brand_name in ('samsung','apple');
-- in and not in query  
 


 