# Python 3.7.2
import psycopg2 as dbapi
from queries import article_query, author_query, log_query

conn = dbapi.connect("dbname = news")
cur = conn.cursor()


# find the most popular three articles of all time
print(
    "\nThe 3 most popular articles of all " +
    "time in descending order by views:\n")
cur.execute(article_query)
for record in cur:
    print(record[0] + " - " + str(record[1]) + " views")

# find who are the most popular article authors of all time
print("\nThe most popular authors of all time in descending order by views:\n")
cur.execute(author_query)
for record in cur:
    print(record[0] + " - " + str(record[1]) + " views")

# and find on which days did more than 1% of requests lead to errors
print(
    "\nThe days where the request error " +
    "rate was greater than or equal to 1%:\n")
cur.execute(log_query)
for record in cur:
    print(str(record[0].date().strftime("%b %d, %Y")) +
          " - " + str(round(record[1], 4)*100) + "% errors")
print(" ")
