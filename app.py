from flask import Flask, render_template, flash, redirect, url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, PasswordField, validators
from passlib.handlers.sha2_crypt import sha256_crypt

app = Flask(__name__)

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
    app.run(debug = True)
