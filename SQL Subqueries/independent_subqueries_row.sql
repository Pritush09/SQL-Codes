SELECT * FROM subqueries.users
where user_id not in (select distinct(user_id) from subqueries.orders);


with top_directors as (select director from subqueries.film group by director order by sum(gross) desc limit 3)
-- the above statement is the use of common table expression used to create an temporary table which we can use in our sql for other purpose
select * from subqueries.film
where director in (select * from top_directors);

with stars as (select star from subqueries.film where votes>25000 group by star having avg(score)>8.5)
select * from subqueries.film
where star in (select * from stars);