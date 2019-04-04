# udacity_fullstack_project3

## **PROJECT**
log analysis of a preconfigured database in a udacity VM

## **DEPENDENCIES**
* Python 3+
* psycopg2 library

## **SETUP/INSTALLATION & USAGE**
* To Setup: follow guidelines provided in the udacity vagrant vm setup. vagrant can be found  here https://www.vagrantup.com/downloads.html, the vagrant box files can be downloaded here https://github.com/udacity/fullstack-nanodegree-vm. extract the vagrant box to any folder you have access two and navigate to it. input the command "vagrant up" to launch your virtual machine. after the vm has been intiallized use "vagrant ssh" to enter into the vagrant vm. then load all files (minus this readme as it's uneccessary) into the shared folder of a vagrant instance's shared folder directory (/vagrant under the vm's extracted location on the host machine). next you will need to download the database from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip. extract the files to the same directory you placed the included files in and extract the newdata files there. Then execute "psql -d news -f newsdata.sql" to set up the data base so you can run the script.

* To Run: in you vagrant vm cd to the part of the shared directory where you inserted the files and run the app with "python log_analysis.py", the output will show automatically.


### **NOTES**
No views were used although when you look at the SQL it seems like I probably should have turned at least part of the first and seocnd query into a view, but I had a little fun reimplementing UNPIVOT functionality in Postgres and didn't think about it.

The queries are stored in separate files to keep the pep8 compliance nice and simple.

