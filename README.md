moviesf
=======

What is it?
------------
The Movies application is a Django rest-framework based API that provides a listing of location in the San Francisco area where films have been shot. It provides a full-stack solution with a basic jQuery + Google Maps based front-end, along with a Django/Python back-end.

Why REST? Why Django/Python?
------------
I chose the Django/Python stack to demonstrate my ability to develop an application using the language of choice as per the Uber Coding Challenge specifications. Furthermore, working with a JSON RESTful API is a very lightweight design than with a SOAP architecture, and given that the offered data sources are also RESTful interfaces, I thought it only makes sense to follow suit.

Known inefficiencies
--------------------
The application provides a basic front-end view that allows the user to search for film locations in the San Francisco area. The UI is very basic and minimal, but it gets the job done. Given that my experience in CSS, Javascript is not one of my strong points, I decided to just offer a basic front-end.

The back-end has one notable inefficiency. The data set retrieved through the SODA API is persisted into the local sqlite3 datbase file on each load of the homepage. I could have done an initial creation of all the data provided, and keep using the data as is, but I decided that due to the possibility of the data source changing, purging the existing data and re-creating all the records would be the solution. This indeed adds overhead, but I wanted to demonstrate my knowledge of the Django models.

Contact
-------
Author: Jun Lee
Email: jklee85@gmail.com
LinkedIn: ca.linkedin.com/in/junleeto
Hosted on: Heroku http://sheltered-coast-3497.herokuapp.com/movies
Github Repo: https://github.com/tigerjk/moviesf
