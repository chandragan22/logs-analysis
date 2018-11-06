#!/usr/bin/env python2.7
import psycopg2

db = psycopg2.connect("dbname=news")

cur = db.cursor()

cur.execute("select title, num FROM articlepath, pathname \
    where articlepath.path = pathname.path \
    group by articlepath.title, pathname.num \
    order by pathname.num desc limit 3;")

results = cur.fetchall()
print("These are the most popular three articles"
      " in the database with how many views they got.")
for result in results:
    print('"{}" - {} views'.format(result[0], result[1]))
print('\n')

cur.execute("select name, sum(num) from authorarticle, articleviews \
    where authorarticle.title = articleviews.title \
    group by authorarticle.name \
    order by sum(num) desc;")

results = cur.fetchall()
print("These are the most popular article authors")
for result in results:
    print('{} - {} views'.format(result[0], result[1]))
print('\n')

cur.execute("select days, error*100 from dayerror where (error*100)>1;")

results = cur.fetchall()
print("This is the day where more than 1 percent"
      " of the requests led to errors in the database.")
for result in results:
    print ' '.join(str(n) for n in result)+'%'
