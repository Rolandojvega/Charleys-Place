import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import datetime


from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
# app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///charley.db")

@app.route("/")
def homepage():
    """Show todays menu"""
    # Redirect user to menu
    return redirect("/home")



@app.route("/home")
def home():
    """Show todays menu"""
    if request.method == "GET":
        # Query database
        #dishes = db.execute("SELECT * FROM dishes JOIN menu_details ON ID = dish_ID WHERE menu_ID = 1")
        menu = db.execute("SELECT * FROM dishes WHERE ID IN (SELECT dish_ID FROM menu_details WHERE menu_ID IN(SELECT MAX(menu_ID) FROM menu_details))")
        today = datetime.date.today().strftime("%B %d, %Y")

        return render_template("home.html", menu = menu, today = today)
    else:
        return apology("TODO")


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    """dashboard for admin"""
    if request.method == "GET":
        # Query database for top 5
        top = db.execute("SELECT * FROM dishes WHERE avg_rating IS NOT NULL ORDER BY avg_rating DESC LIMIT 5")
        # Query database for bottom 5
        bottom = db.execute("SELECT * FROM dishes WHERE avg_rating IS NOT NULL ORDER BY avg_rating ASC LIMIT 5")
        return render_template("dashboard.html", top = top, bottom = bottom)
    else:
        return apology("TODO")

@app.route("/about", methods=["GET"])
def about():
    """Show about information"""
    if request.method == "GET":
        return render_template("about.html")

@app.route("/form", methods=["GET", "POST"])
@login_required
def form():
    """capture menu inputs"""
    # User reached route via POST (as by submitting a form via POST)

    if request.method == "POST":

        test0 = request.form.get("10")
        print("LOOK HERE!!!!!!!!!!!!!", test0)
        test1 = request.form
        print("SECOND", test1)
        test2 = request.form.get("11")
        print(test2)
        """
        C1 = request.form.get("category1")
        D1 = request.form.get("dish1")
        O1 = request.form.get("country1")
        I1 = request.form.get("ingredient1")

        C2 = request.form.get("category2")
        D2 = request.form.get("dish2")
        O2 = request.form.get("country2")
        I2 = request.form.get("ingredient2")

        C3 = request.form.get("category3")
        D3 = request.form.get("dish3")
        O3 = request.form.get("country3")
        I3 = request.form.get("ingredient3")

        comment = request.form.get("comment")
        today = datetime.date.today().strftime("%Y-%m-%d")
        db.execute("INSERT INTO dishes (name, ingredients, type, country_of_origin) VALUES (:dish, :ingredients, :category, :country)", dish = D1, ingredients = I1, country = O1, category = C1)
        db.execute("INSERT INTO dishes (name, ingredients, type, country_of_origin) VALUES (:dish, :ingredients, :category, :country)", dish = D2, ingredients = I2, country = O2, category = C2)
        db.execute("INSERT INTO dishes (name, ingredients, type, country_of_origin) VALUES (:dish, :ingredients, :category, :country)", dish = D3, ingredients = I3, country = O3, category = C3)

        D1_ID = db.execute("SELECT ID FROM dishes WHERE name = :dish AND creation_date = :date", dish = D1, date = today)
        D2_ID = db.execute("SELECT ID FROM dishes WHERE name = :dish AND creation_date = :date", dish = D2, date = today)
        D3_ID = db.execute("SELECT ID FROM dishes WHERE name = :dish AND creation_date = :date", dish = D3, date = today)

        db.execute("INSERT INTO menu_master (menu_comment) VALUES (:comt)", comt = comment)
        menu_ID = db.execute("SELECT ID FROM menu_master WHERE menu_date = :date AND menu_comment = :comt", comt = comment, date = today)

        db.execute("INSERT INTO menu_details (menu_ID, dish_ID) VALUES (:menu_id, :dish_id)", menu_id = menu_ID[0]['ID'], dish_id = D1_ID[0]['ID'])
        db.execute("INSERT INTO menu_details (menu_ID, dish_ID) VALUES (:menu_id, :dish_id)", menu_id = menu_ID[0]['ID'], dish_id = D2_ID[0]['ID'])
        db.execute("INSERT INTO menu_details (menu_ID, dish_ID) VALUES (:menu_id, :dish_id)", menu_id = menu_ID[0]['ID'], dish_id = D3_ID[0]['ID'])
        """
        return render_template("complete.html")
    else:
        return render_template("form.html")

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    """Show menu creation form"""

    if request.method == "GET":
        return render_template("create.html")

    else:

        Dict = {}
        dishname = request.form.get("dishname")
        ingredients =  request.form.get("ingredients")
        userinput = {dishname : ingredients}
        Dict.update( userinput )
        #if dishname == None:
            #return
        #else:
        return render_template("create.html", Dict = Dict)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/home")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/home")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # When requested via GET, should display registration form
    #Going to look similar to login.html,
    #in addition to user name and password, add password confirmation field
    if request.method == "GET":
        return render_template("register.html")

    else:

    # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

    # Query database for existing username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        if len(rows) > 0:
            return apology("username already exists", 403)

    #error checking is passwords dont match
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords dont match", 403)

    # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

    #hash users password and store hash in database
        else:
            username = request.form.get("username")
            hashpass = generate_password_hash(request.form.get("password"))
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=username, hash = hashpass)


    # Be sure to check for invalid inputs, and to hash the user's password.
    return redirect("/login")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
