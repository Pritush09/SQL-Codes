SELECT * from subqueries.film
where gross - budget = (select max(gross - budget) from subqueries.film);


select count(*) from subqueries.film
where score > (select avg(score) from subqueries.film);


select * from subqueries.film
where year = 2000 and score  = (select max(score) from subqueries.film where year = 2000);


select * from subqueries.film
where votes = (select max(votes) from subqueries.film where votes > (select avg(votes) from subqueries.film)); 