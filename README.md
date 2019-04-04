# udacity_fullstack_project3

## **PROJECT**
log analysis of a preconfigured database in a udacity VM

## **DEPENDENCIES**
* Python 3+
* psycopg2 library

## **SETUP/INSTALLATION & USAGE**
* To Setup: follow guidelines provided in the udacity vagrant vm setup. then load all files (minus this readme as it's uneccessary) into the shared folder of a vagrant instance (assuming instructor set up is the same if not make sure that the newsdata.sql database is also present and loaded into the vm) 

* To Run: in you vagrant vm cd to the part of the shared directory where you inserted the files and run the app with "python log_analysis.py", the output will show automatically.

### **NOTES**
No views were used although when you look at the SQL it seems like I probably should have turned at least part of the first and seocnd query into a view, but I had a little fun reimplementing UNPIVOT functionality in Postgres and didn't think about it.

The queries are stored in separate files to keep the pep8 compliance nice and simple.

