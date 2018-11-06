# Logs Analysis Project

This database setup and the queries allow the user to find:
1. The most popular three articles in the database
2. The most popular article authors
3. Which days more than 1% of the requests led to errors in the database. 

## Installation

Have PostgreSQL installed and the psql command prompt running.
Download the Linux-based Virtual Machine.
Download Vagrant from this repo: https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile
Download the data from Udacity's Full Stack Web Developer Nanodegree Program under Logs Analysis Project using the link: 
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip


## Running the Code

Open the file downloaded through the installation steps.
Move the newsdata.sql file into the vagrant directory.
The code uses the create views functions to separate the code so that the queries will run.

### Creating Views

In order to create these views, run these steps:
1. Open the Vagrant directory
2. Run vagrant up
3. Run vagrant ssh
4. cd into the vagrant directory
5. Run psql-d news -f newsdata.sql
6. Run the following lines:
```psql
CREATE VIEW articlepath AS
		SELECT path, slug, title FROM log, articles
		WHERE substring(log.path FROM 10) = articles.slug;
CREATE VIEW top4 AS 
		SELECT path, count(*) AS num
		FROM log
		GROUP BY path
		ORDER BY num desc
		LIMIT 4;
CREATE VIEW pathname AS 
		SELECT path, count(*) AS num
		FROM log
		GROUP BY path
		ORDER BY num desc;
CREATE VIEW authorarticle AS
		select title, name
		from articles, authors
		where articles.author = authors.id;
CREATE VIEW articleviews AS
		select title, num
		from articlepath, pathname
		where articlepath.path = pathname.path
		group by articlepath.title, pathname.num
		order by pathname.num desc;
CREATE VIEW DayError AS
		select time::date as days, avg((status<>'200 OK')::int) as error 
		from log
		group by days;
```
Run the python file logs_analysis.py to get the results from the queries.

## Acknowledgements

The Udacity Nanodegree program to becoming a Full-Stack Web Developer was used to lay out the structure of the code and organize the code.
The PostgrSQL documentation was used to further understand the aggregate functions, converting data into different formats, and clauses: https://www.postgresql.org 