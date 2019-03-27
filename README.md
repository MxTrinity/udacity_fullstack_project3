# udacity_fullstack_project3

To run: load all files (minus this readme) into the shared folder of a vagrant instance (assuming instructor set up is the same if not make sure that the newsdata.sql database is also present) and run log_analysis.py.

No views were used although when you look at the SQL it seems like I probably should have turned at least part of the first and seocnd query into a view, but I had a little fun reimplementing UNPIVOT functionality in Postgres and didn't think about it.

The queries are stored in separate files to keep the pep8 compliance nice and simple.