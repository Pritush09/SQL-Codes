--  having clause does the same thing that where does for the select 

select brand_name,avg(price) as 'avg_price', count(*) as 'num_phones'
from campusx.smartphones_cleaned_v6
group by brand_name
having num_phones > 20
order by avg_price desc limit 10;


select brand_name,count(*) as 'num_phone' ,
avg(ram_capacity) as 'avg_ram'
from campusx.smartphones_cleaned_v6
where refresh_rate > 90 and fast_charging_available = 1
group by brand_name
having num_phone > 10
order by avg_ram desc limit 7;


