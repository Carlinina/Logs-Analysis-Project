# Logs-Analysis-Project
Internal reporting tool of a newspaper site that will use information from the database to discover what kind of articles the site's readers like.
It will be answering 3 questions:
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?
## Requirements
You'll need:
1. Database software (provided by 
a Linux virtual machine)
2. Data to analyze, newsdata.sql file. The database includes three tables:
  - The authors table includes information about the authors of articles.
  - The articles table includes the articles themselves.
  - The log table includes one entry for each time a user has accessed the site.
## Instructions
The file news_tool.py is the reporting tool in Python 2.7 program using the psycopg2 module to connect to the database.
In building this tool, I add 8 views to the database.

The create view commands are:
  
  Question1:
  
  	CREATE VIEW popular_path AS SELECT title, slug, path FROM articles JOIN log ON log.path = CONCAT('/article/',articles.slug);
  
  Question2:
  
    CREATE VIEW popular_authors AS SELECT author, slug, path FROM articles JOIN log ON log.path = CONCAT('/article/',articles.slug);
 	  
    CREATE VIEW authors_views AS SELECT author, count(*) AS views FROM popular_authors GROUP BY author ORDER BY views DESC;
  
  Question3:

  	CREATE VIEW date_status AS SELECT DATE(time), status FROM log ORDER BY DATE(time);
  
  	CREATE VIEW date_error AS SELECT DATE(time), status FROM log WHERE status='404 NOT FOUND' ORDER BY DATE(time);

  	CREATE VIEW total_entries AS SELECT date, count(*) AS total_number FROM date_status GROUP BY date ORDER BY date ASC;
  
  	CREATE VIEW error100 AS SELECT date, count(*)*100 AS errors FROM date_error GROUP BY date ORDER BY date ASC;
  
  	CREATE VIEW percentage AS SELECT error100.date, (errors*1.00)/total_number AS percentage_errors FROM error100, total_entries WHERE total_entries.date=error100.date ORDER BY percentage_errors DESC;
  
 You will need to run python news_tool.py in the command line.
 
## Example of the program's output

program_out_example.txt is a plain text file that is a copy of what the program prints out.
