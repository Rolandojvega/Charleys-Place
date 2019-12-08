# User's Manual for the Charleys-Place Web App

# What did we build?
A website that displays the Charley's Place lunch menu, provides an admin the ability to update the menu and view a preferences dashboard,
and allows users to rate the menu items. The web app was built using HTML, CSS, JavaScript, Python, and the Flask web framework.

# How to get started as user?
As a user you can view the latest lunch menu on the homepage simply by visiting our website - no login required.

This simple action - viewing the day's menu on the homepage - solves a main painpoint for existing eaters at Charley's Place,
who typically do not know what the daily menu is before visiting the cafeteria. Awareness of alternative means of discovering
the daily lunch menu is low and cumbersome (menu is buried behind multiple clicks on the Yale Hospitality site and native iOS/Android app).

In addition to the menu - divided among the three cafeteria stations (Al Forno, Wok, and Salad and Sandwich Bar) - users are presented
with 'thumbs up' and 'thumbs down' buttons to rate the daily assortment of dishes. The rating information is then registered in an
admin database and viewable in aggregate terms on the admin dashboard.

Users, if interested, can also read more about Charley's Place on the About page, accessible via the top bar navigation.

Lastly, users can provide the web team with suggestions on how to improve the online Charley's Place menu. A complete submission form
will send an email to our team directly. Paragraph text makes it clear that the form will not go to the Charley's Place management team.
A link is provided to the Yale Hospitality feedback form for those users who want to surface comments or suggestions to Charley's Place
directly.

# How to get started as admin?
As an admin you can view the daily lunch menu, create/update the lunch menu, and view the user preference dashboard - login required.

Unfortunately, there is no pre-existing API for Charley's Place that would allow us to pull the daily menu directly. This is because
the Charley's Place management team does not operate like other Yale dining halls - there is no recurring menu items and the daily menu
can change up to a few hours before opening. For this reason, our web app allows an admin to create a menu with ease.

Once logged in, under the 'Create' tab, an admin can add the daily menu dish by dish. The create form requires an admin to select
the category (or dining station), name the dish, select its country of origin, and list the ingredients. To validate the data, the admin must
add a comment (e.g. "Menu for 12/10/2019") before submitting the form. Upon submission the form will update the menu viewable on the site
homepage.

An admin has access to a dashboard page where they can view the top 5 and bottom 5 dishes, ranked by percentage approval (or 'thumbs up') rating
by users. The dashboard also displays a count of the number of reviews.

# Descriptions of all pages

# Homepage / Menu
The daily lunch menu is displayed prominently on the landing page along with ratings buttons per each dish ('thumbs up' and 'thumbs down').

# About
The about page includes paragraph text information about Charley's Place and includes helpful hyperlinks out to the Yale SOM homepage
and the management team's inspiration.

# Suggestions
The suggestions page includes a submission form with 'email', 'category', and an open comment fields. Once submitted this form will send
an email to the website management team (i.e. that's us).

# Create
The create page is viewable only to a registered admin. On this page, admins can create the daily menu dish-by-dish.

# Dashboard
This page displays an admin only dashboard that records historical user ratings on the top and bottom 5 dishes.

# Register
For registering new admin users.

# Log In
For admin login.


