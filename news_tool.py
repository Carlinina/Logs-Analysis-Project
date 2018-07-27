# "New's Tool code for the news database":
# There are seven VIEWS needed, look at the README.

import psycopg2


def get_popular_articles():
    """1. What are the most popular three articles of all time? \
    Which articles have been accessed the most?\
    Sorted list with the most popular article at the top."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # Look VIEW popular_path
    query = "SELECT title, count(*) AS views FROM popular_path GROUP BY title \
  ORDER BY views DESC LIMIT 3;"
    c.execute(query)
    rows = c.fetchall()
    print "Q1. Number of article's views:"
    for row in rows:
        print "   ", " \"", row[0], "\"", "-- ", row[1], "views"
    db.close()


get_popular_articles()


def get_popular_author():
    """2. Who are the most popular article authors of all time?\
    which authors get the most page views?\
    Sorted list with the most popular author at the top."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # Look VIEW popular_authors
    # Look VIEW authors_views
    query = "SELECT name, views FROM authors_views JOIN authors\
  ON authors.id=authors_views.author;"
    c.execute(query)
    rows = c.fetchall()
    print "Q2. Number of authors' views:"
    for row in rows:
        print "   ", " \"", row[0], "\"", "-- ", row[1], "views"
    db.close()


get_popular_author()


def get_days_error_1per():
    """3. On which days did more than 1% of requests lead to errors?\
    The log table includes a column status that indicates the HTTP status code\
    that the news site sent to the user's browser."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # Look VIEW date_status
    # Look VIEW date_error
    # Look VIEW total_entries
    # Look VIEW error100
    # Look VIEW percentage
    query = "SELECT date, percentage_errors FROM percentage WHERE\
  percentage_errors > '1';"
    c.execute(query)
    rows = c.fetchall()
    print "Q3. Days where more than 1% of requests lead to errors:"
    for row in rows:
        print "   ", " \"", row[0], "\"", "-- ", row[1], "% errors"
    db.close()


get_days_error_1per()
