select * from cx_live.person1
union 
select * from cx_live.person2;


select * from cx_live.person1
union all
select * from cx_live.person2;


select * from cx_live.person1
intersect
select * from cx_live.person2;
-- this is giving error but working 


select * from cx_live.person1
except
select * from cx_live.person2;
-- this is giving error but working 
