-- use moviesdb  <-- by writing this we say that the moviesdb is our default databas
use moviesdb;
select * from movies where industry='Bollywood';

select count(*) from moviesl;-- return the count of the dataframe 

select distinct industry from movies;-- return the unique values present in the dataframe

select * from movies where title like '%thor%'; -- this gives me the movies which as thor in there title % is for neglecting whats before and after that word 
 
select * from movies where studio=""; 

select * from movies where imdb_rating>=9;

select * from movies where imdb_rating between 6 and 9;-- better way

select * from movies where industry='Bollywood' order by imdb_rating desc limit 5;  -- asc for ascending

select * from movies where industry='Bollywood' order by imdb_rating desc limit 5 offset 1; -- to get the top 5 movies from 2nd highest onwards