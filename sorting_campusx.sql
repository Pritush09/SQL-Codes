SELECT model,screen_size FROM campusx.smartphones_cleaned_v6
where brand_name='samsung' 
order by screen_size desc limit 10;


select num_front_cameras + num_rear_cameras as 'total_cameras',model,brand_name from campusx.smartphones_cleaned_v6
order by total_cameras desc;


select round(sqrt(resolution_width*resolution_width+ resolution_height+resolution_height)/screen_size,2) as 'ppi',model,brand_name 
from campusx.smartphones_cleaned_v6
order by ppi desc;


select * from campusx.smartphones_cleaned_v6
order by battery_capacity desc limit 1,1;
-- so the limit is set as kaha se start karna he aur uske baad kitna no. of item print karna he


select model,rating from campusx.smartphones_cleaned_v6
where brand_name='apple'
order by rating limit 1;


select * from campusx.smartphones_cleaned_v6
order by brand_name asc , price asc;




