# Design Document for the Charleys-Place Web App

# Technically, how did we built this web app?
To build our web app, we started off by using the codebase from the CS50 Finance pset assignment, which is written in python, HTML (w/ Jinja templating), CSS,
and JavaScript and features a SQLite3 databse integration. Just as we did with CS50 Finance, we used the python-based web framework, Flask. We decided to take this approach
by recommendation of the CS50 teaching staff, plus we have some familiarity with these languages and the Flask framework based on our work in the web development track.

Next we stripped the codebase of irrelevant code and libraries in the python files application.py and helpers.py which hold our site's routes and functions.
Then we reviewed our HTML templates - adding and removing HTML files until we were left with the HTML files for the relevant pages for our app.

# Create a Menu
To create the menu we needed to seek input on dishes which would be on the menu from the admin. The challenge was that the number of dishes on the menu on a given day varies from a single dish to several dishes a day (we observed this in the live menus during the past couple of weeks). To address this challenge we created a dynamically expanding and contracting form in which new field rows could be added or removed conveniently using buttons. The functionality was built using JavaScript jQuery and bootstrap CSS.
In the form we used several input field types such as dropdown lists for “country of origin” for which we linked the select dropdown menu to the database which had the list of all countries using jinja loops.
As an enhancement we wanted to add the live search feature in the lengthy dropdowns to improve the user experience. We could successfully make it work using a bootstrap open source JS library for a single row of dish input. But unfortunately the live search feature couldn’t work with multiple rows of dishes due to a bug in the JS online selectpicker library and hence we dropped the live search feature.

# Ratings
As part of our site experience, we wanted to make it possible for users to rate the Charley's Place menu. After some debate, we aligned on a 'thumbs up' and
'thumbs down' rating scheme for each dish versus a 5-star rating. Our goal was to create a frictionless user experience, which meant that we didn't want users
to have to be logged in to rate dishes. The goal was for users to be able to quickly and easily rate the day's menu items.
Each item has a thumbs up / thumbs down understand which can be click. Once clicked it posts and updates our database which tracks counts of likes and dislikes. Clicking also takes you to another page which notifies you that your click was successful. We update multiple elements including average ratings, total counts, and total likes and dislikes using the thumbs up / thumbs down. All this data is then viewed through the Dashboard.

# Dashboard
A dashboard is made available to Charley's Place administrator users only. A logged in admin has access to a dashboard that draws from the user dish ratings data and shows the top/bottom dishes by rating and review quantity.
The objective of having a dashboard was for the admin to view the top rated and worst rated dishes so they may take action accordingly. We enabled this by storing the required data in an easily quarriable format and updating it as and when a new feedback is received by users. When /dashboard route is activated we retrieve the required data and posted it in the form of a table using jinja loop on the html page.


# Email Suggestions
Our initial goal was to make it possible for site users to send the Charley's Place management plaintext feedback on menu items and suggestions for
menu additions. As we set out to build this function we soon discovered that Yale Hospitality has an existing customer feedback form. If we were to
build a similar form, then we would be adding to the complexity of Charley's Place communications, rather than simplifying it further. For this reason
we decided to instead provide a link-out to the Yale SOM Hospitality customer feedback form for visitors to our site.

As developers of this site, we also want feedback from those who experience our page. That's why we added a user form to our site to collect direct
feedback from visitors about the site's functionality and features. To do so, we started by exploring the SendGrid API. Unfortunately, a drawback of building
our site on an AWS Cloud9 server (CS50 IDE) is that certain API integrations do not "play nice". The SendGrid API is one such API, so we had to find another way
to receive email feedback from our users. That other way involved JavaScript manipulation to make it possible for users to send a member of a team a direct email
with the body of their feedback form passed through to their local email client. This functionality is written as a script function within the body of our
suggestions.html page. While this is not the exact user experience we had set out to achieve, users are able to perform the functionality - send feedback via email -
that we desired.
