select count(*) as 'no._of_phones',brand_name from campusx.smartphones_cleaned_v6
group by brand_name;
-- select count(*),brand_name from campusx.smartphones_cleaned_v6 where brand_name='apple';  --this is just to check the output 

 
select count(*) as 'no_of_phones',brand_name,avg(price) as 'avg_price',max(rating) as 'max_rating', avg(screen_size) as 'avg_screen_size', avg(battery_capacity) as 'avg_battery_capacity'
from campusx.smartphones_cleaned_v6
group by brand_name
order by no_of_phones desc;


select has_5g, avg(price) , avg(rating)
from campusx.smartphones_cleaned_v6
group by has_5g;


select has_5g, has_nfc,avg(price) , avg(rating)
from campusx.smartphones_cleaned_v6
group by has_5g,has_nfc; -- multiple column based groupby


select brand_name, processor_brand, avg(price) as 'avg_Price' , avg(rating) as 'avg_rating'
from campusx.smartphones_cleaned_v6
group by brand_name, processor_brand
order by avg_rating desc;


select brand_name,avg(price) as 'avg_price'
from campusx.smartphones_cleaned_v6
group by brand_name
order by avg_price desc limit 10;


select brand_name , count(*) as 'num_phone'
from campusx.smartphones_cleaned_v6
where has_ir_blaster='true' and has_nfc= 'True'
group by brand_name
order by num_phone desc limit 1;