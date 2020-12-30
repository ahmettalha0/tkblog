from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, PasswordField, validators
from passlib.handlers.sha2_crypt import sha256_crypt

app = Flask(__name__)
app.secret_key = "tkblog"

# mysql settings
mysql = MySQL(app)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "tkblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# user register form
class RegisterForm(Form):
    name = StringField("Name and Surname", validators=[validators.Length(min= 3, max= 25), validators.DataRequired()])
    username = StringField("Username", validators=[validators.Length(min= 3, max= 35), validators.DataRequired()])
    email = StringField("Email", validators=[validators.DataRequired(), validators.Email("Please enter a valid email address")])
    password = PasswordField("Password", validators=[
        validators.Length(min= 8, max= 40),
        validators.DataRequired(),
        validators.EqualTo(fieldname="confirm",message="Password does not match")
        ])
    confirm = PasswordField("Re-enter your password", validators=[validators.DataRequired()])

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

@app.route('/register', methods = ["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)
        cursor = mysql.connection.cursor()
        user_query = "Insert into users(name,username,email,password) VALUES(%s, %s, %s, %s)"
        cursor.execute(user_query, (name, username, email, password))
        mysql.connection.commit()
        cursor.close()
        flash(message="You have successfully registered.", category= "success")
        return redirect(url_for("index"))
    else:
        return render_template("register.html", form = form)
    

if __name__ == '__main__':
    app.run(debug=True)
