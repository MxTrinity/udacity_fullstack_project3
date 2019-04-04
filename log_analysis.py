#! /usr/bin/env python3
# Python 3.7.2
import psycopg2 as dbapi
from queries import article_query, author_query, log_query


try:
    conn = dbapi.connect("dbname = news")
except dbapi.DatabaseError as e:
    # the rest of the script won't function without a DB
    # and you should probably figure out what broke anyway.
    print("<error message>" + "Terminating program")
    sys.exit
cur = conn.cursor()


# find the most popular three articles of all time
print(
    "\nThe 3 most popular articles of all " +
    "time in descending order by views:\n")
try:
    cur.execute(article_query)
    for record in cur:
        print(record[0] + " - " + str(record[1]) + " views")
except dbapi.DatabaseError as e:
    print("There was an error getting the top articles! " + "<error message>")

# find who are the most popular article authors of all time
print("\nThe most popular authors of all time in descending order by views:\n")
try:
    cur.execute(author_query)
    for record in cur:
        print(record[0] + " - " + str(record[1]) + " views")
except dbapi.DatabaseError as e:
    print("There was an error getting the top authors! " + "<error message>")

# and find on which days did more than 1% of requests lead to errors
print(
    "\nThe days where the request error " +
    "rate was greater than or equal to 1%:\n")
try:
    cur.execute(log_query)
    for record in cur:
        print(str(record[0].date().strftime("%b %d, %Y")) +
              " - " + str(round(record[1], 4)*100) + "% errors")
except dbapi.DatabaseError as e:
    print("There was an error getting error rates! " + "<error message>")
print(" ")

conn.close()
