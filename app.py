from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.debug = True

# MYSQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

userid = 0

# Initialize db
mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [validators.DataRequired(),
                validators.EqualTo('confirm', message="Passwords do not match!")])
    confirm = PasswordField('Confirm Password')


@app.route("/devSignUp.html", methods=['GET', 'POST'])
def devSignUp():
    form = RegisterForm(request.form)
    print("here")
    if request.method == 'POST':
        name = form.name.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO User(name, email, password) VALUES(%s, %s, %s)", (name, email, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash("You are now registered successfully", 'success')

        print("here22")
        return redirect(url_for('index'))
    return render_template("devSignUp.html", form = form)

@app.route("/devSignIn.html")
def devSignIn():
    return render_template("devSignIn.html")



@app.route("/adminSignIn.html")
def adminSignIn():
    return render_template("adminSignIn.html")

@app.route("/comSignIn.html")
def comSignIn():
    return render_template("comSignIn.html")

@app.route("/comSignUp.html")
def comSignUp():
    return render_template("comSignUp.html")

@app.route("/forgotPass.html")
def forgotPass():
    return render_template("forgotPass.html")

@app.route("/devHome.html")
def devHome():
    return render_template("devHome.html")

@app.route("/searchQuestion.html")
def searchQuestion():
    return render_template("searchQuestion.html")

@app.route("/searchResult.html")
def searchResult():
    return render_template("searchResult.html")

@app.route("/questionDetails/<string:id>/")
def questionDetails(id):
    return render_template("questionDetails.html", id = id)

@app.route("/discussion.html/<string:id>.html/")
def discussion(id):
    return render_template("discussion.html", id = id)

if __name__== '__main__':
    app.secret_key = "difficult"
    app.run()
