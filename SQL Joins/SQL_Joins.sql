select * from cx_live.users1 t1
cross join cx_live.groups t2;
-- This above is the representation of the cross join


select * from cx_live.membership t1
inner join cx_live.users1 t2
on t1.user_id = t2.user_id;
-- this is example of the inner join which is most commonly used 


select * from cx_live.membership t1
left join cx_live.users1 t2
on t1.user_id = t2.user_id;
-- lEFT JOIN Example


select * from cx_live.membership t1
right join cx_live.users1 t2
on t1.user_id = t2.user_id;
-- RIGHT JOIN Example


select * from cx_live.users1 t1
join cx_live.users1 t2
on t1.emergency_contact = t2.user_id;
--  this is self join example


select * from cx_live.students t1
join cx_live.class t2
on t1.class_id = t2.class_id and t1.enrollment_year = t2.class_year;
-- join on more than 1 column


select * from orders.order_details t1
join orders.orders t2
on t1.order_id = t2.order_id
join orders.users t3 
on t2.user_id = t3.user_id;


select t1.order_id,t1.amount,t1.profit,t3.name from orders.order_details t1
join orders.orders t2
on t1.order_id = t2.order_id
join orders.users t3 
on t2.user_id = t3.user_id;


select t1.order_id , t2.vertical
from orders.order_details t1
join orders.category t2
on t1.category_id = t2.category_id;


select * from orders.orders t1
join orders.users t2
on t1.user_id = t2.user_id 
where t2.city = 'Pune';
