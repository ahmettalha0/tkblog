from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, PasswordField, validators
from passlib.handlers.sha2_crypt import sha256_crypt

app = Flask(__name__)

# mysql settings
MySQL = MySQL(app)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "tkblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/article/<string:slug>')
def detail_page(slug):
    return "Article " + slug

if __name__ == '__main__':
    app.run(debug=True)
