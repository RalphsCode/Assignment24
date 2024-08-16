### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL is an open-source relational database management system (RDBMS). PostgreSQL's database management system is built on top of a SQL database. It is used to administer the database, and also to run queries. It can be used for DDL (Data Definition Language - how data and database are structured) purposes, and DML (Data Modification Language - how the data is accessed, used, queries, etc).
 

- What is the difference between SQL and PostgreSQL?
SQL is a database, PostgreSQL is is a management system that assists in managing and using the SQL database. In essence, SQL is the language, while PostgreSQL is a database system that uses and extends SQL.

- In `psql`, how do you connect to a database?
To connect to a database using 'psql' I type in the username, the host, and optionally the database I wish to connect to. I will then be prompted to enter the password for the username. For example:
psql -U postgres -h Localhost my_database

- What is the difference between `HAVING` and `WHERE`?
WHERE is used to filter to certain rows/data from a database, and HAVING can then be added to group those filtered results. WHERE works on row data, and HAVING works on grouped data.

- What is the difference between an `INNER` and `OUTER` join?
An INNER join means that the returned data must exist in both tables being joined. An OUTER join however means that the retrieved data is not necessarily in both of the tables. There are three types of OUTER joins: 
(I) LEFT OUTER JOIN (or simply LEFT JOIN), 
(II) RIGHT OUTER JOIN (or RIGHT JOIN) 
(III) FULL OUTER JOIN

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
A LEFT OUTER join means everything in the left side table will be included in the returned data, along with the matching rows from the right table.
A RIGHT OUTER join means everything in the right side table will be included in the returned data, along with the matching rows from the left table. 

- What is an ORM? What do they do?
ORM stands for Object-Relational Mapping, and is a way for Object Orientated Programming to interact with relational databases such as SQL. ORM allows objects in a programming language to interact smoothly with the database when generating database operations. SQLAlchemy is an example of an ORM that we learned.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

There are quite a lot of differences stemming from the fact that AJAX requests run on the client's browser, while requests run on the server. Some differences:
AJAX: Limited by browser security policies (e.g., Same-Origin Policy).
Server-side: Not restricted by browser policies, can access any URL.
AJAX: Visible to users, less secure for private keys.
Server-side: Can keep sensitive information hidden from clients.
AJAX: Us.es client resources, can offload work from server.
Server-side: Uses server resources, may increase server load.
AJAX: Can update parts of a page without full reload.
Server-side: Typically requires page refresh to show new data.

- What is CSRF? What is the purpose of the CSRF token?
CSRF - Cross-Site Request Forgery is used by a bad actor to try and imitate a form submission and gain access to a server. WTForms  uses a CSRF token to prevent form submissions from anywhere other than the form itself. For example; another website cannot submit a post request to the form's server, because that submission will not include the CSRF token inserted by the form's originating server. The purpose of the token is to provide a digital key, that the form submits, and must be validated at the receiving end in order for the form to be accepted.

- What is the purpose of `form.hidden_tag()`?
The purpose of form.hidden_tag() is to avoid CSRF by generating a CSRF token when a form is submitted. The CSRF token passes with the form info to the POST request where is validated and the form info accepted by the server.
