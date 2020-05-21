from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, RadioField
from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

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

@app.route("/forgotPass.html")
def forgotPass():
    return render_template("forgotPass.html")

# Dev Functions
@app.route("/devSignUp.html", methods=['GET', 'POST'])
def devSignUp():
    if session.get("logged_in") == True:
        logout()
    else:
        class RegisterForm(Form):
            name = StringField('Name', [validators.Length(min=1, max=50)])
            username = StringField('Username', [validators.Length(min=4, max=25)])
            email = StringField('Email', [validators.Length(min=6, max=50)])
            password = PasswordField('Password', [validators.DataRequired(),
                        validators.EqualTo('confirm', message="Passwords do not match!")])
            confirm = PasswordField('Confirm Password')

        form = RegisterForm(request.form)
        if request.method == 'POST':
            name = form.name.data
            email = form.email.data
            password = form.password.data

            # Create cursor
            cur = mysql.connection.cursor()

            try:
                # Create new User
                cur.execute("INSERT INTO user(name, email, password) VALUES(%s, %s, %s)", (name, email, password))
                mysql.connection.commit()

                # Get User Id
                cur.execute("SELECT user_id FROM user WHERE email='{0}'".format(email));
                mysql.connection.commit();
                userid = cur.fetchall()[0]['user_id']
                # Create new Developer
                cur.execute("INSERT INTO developer (developer_id) VALUES(%s)", [userid])
                mysql.connection.commit()
            except exc.IntegrityError:
                flash("Email exists already")
                app.logger.info('Email exists already')
                return redirect(url_for("devSignUp"))


            # Close connection
            cur.close()
            flash("You are now registered successfully", 'success')
            return redirect(url_for('index'))
    return render_template("devSignUp.html", form = form)


@app.route("/postQuestion.html" , methods=['Get', 'POST'])
def postQuestion():
    class makeQuestion(Form):
        question = TextAreaField("Question: ",[validators.Required("Please enter Question")])
        answer = TextAreaField("Answer: ",[validators.Required("Please Answer")])
        dept_name = TextAreaField("dept_name: ",[validators.Required("dept_name")])
        difficulty = RadioField("Difficulty", choices=[("e" , "easy") , ('m' , 'medium') , ('l', 'large')])
    form = makeQuestion(request.form)
    if request.method == 'POST':
        # print("in post")
        # Create Cursor
        cur = mysql.connection.cursor()

        question = form.question.data
        answer = form.answer.data
        difficulty = form.difficulty.data
        dept_name = form.dept_name.data
        test_case = ""
        approval = 0

        cur.execute("INSERT INTO Question(dept_name, description, test_case, difficulty, approval)" +
            "VALUES ('{0}', '{1}', '{2}', '{3}', 0)".format(dept_name, question, test_case, difficulty))
        mysql.connection.commit()

        # Get response
        queryResponse = cur.fetchall();

        cur.close()
        return redirect(url_for("devHome"))

    return render_template("postQuestion.html", form = form)

@app.route("/devSignIn.html", methods=['GET', 'POST'])
def devSignIn():
    if session.get("logged_in") == True:
        return redirect(url_for("devHome"))
    elif request.method == 'POST':
        email = request.form['email']
        password_candidate = request.form['password']

        # Create Cursor
        cur = mysql.connection.cursor()

        result = cur.execute("SELECT * FROM user WHERE email = %s", [email])
        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare the passwords
            if password == password_candidate:
                app.logger.info('PASSWORD MATCHED')
                session['logged_in'] = True
                session['email'] = email
                flash("You are now logged in", "success")
                return redirect(url_for('devHome'))
            else:
                return redirect(url_for('devHome'))
                app.logger.info('PASSWORD NOT MATCHED')
                error = 'INVALID LOGIN'
                return render_template("devSignIn.html", error = error)

            # Close cursor
            cur.close()
        else:
            error = 'USER NOT FOUND'
            app.logger.info('USER NOT FOUND')
            return render_template("devSignIn.html", error = error)
    return render_template("devSignIn.html")

@app.route("/logout.html")
def logout():
    session.clear()
    flash("You are logged out!", "success")
    return redirect(url_for("index"))

@app.route("/devHome.html")
def devHome():
    return render_template("devHome.html")

@app.route("/searchQuestion.html")
def searchQuestion():

    class SearchForm(Form):
        input = StringField("Input" ,[validators.Required("Please enter Question")] )

    form = SearchForm(request.form)

    if (request.method == "POST"):

        flush("HI")

    return render_template("searchQuestion.html" , form=form)

@app.route("/searchResult.html")
def searchResult():
    return render_template("searchResult.html")

@app.route("/questionDetails/<string:id>/")
def questionDetails(id):
    # Create cursor
    cur = mysql.connection.cursor()

    cur.execute("SELECT description FROM question WHERE question_id = %s", [id])
    mysql.connection.commit()
    question = cur.fetchone()

    cur.close()

    return render_template("questionDetails.html", id = id, question = question)

@app.route("/postComment.html")
def postComment():
    class makeQuestion(Form):
        question = TextAreaField("Question: ",[validators.Required("Please enter Question")])
    form = makeQuestion(request.form)
    if request.method == 'POST':
        # print("in post")
        # Create Cursor
        cur = mysql.connection.cursor()

        question = form.question.data
        answer = form.answer.data
        difficulty = form.difficulty.data
        dept_name = form.dept_name.data
        test_case = ""
        approval = 0

        cur.execute("INSERT INTO Question(dept_name, description, test_case, difficulty, approval)" +
            "VALUES ('{0}', '{1}', '{2}', '{3}', 0)".format(dept_name, question, test_case, difficulty))
        mysql.connection.commit()

        # Get response
        queryResponse = cur.fetchall();

        cur.close()
        return redirect(url_for("devHome"))

    return render_template("postComment.html")

@app.route("/discussion/<string:id>/")
def discussion(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Create new User
    cur.execute("SELECT discussion_id FROM discussion WHERE question_id = %s", [id])
    mysql.connection.commit()

    discuss = cur.fetchall()[0]['discussion_id']
    print(discuss)
    cur.execute("SELECT * FROM comment WHERE discussion_id = %s", [discuss])
    mysql.connection.commit()

    comments = cur.fetchall()

    cur.close()

    return render_template("discussion.html", comments = comments, id = id)

@app.route("/answerToQuestion/<string:id>/")
def answerToQuestion(id):

    return render_template("answerToQuestion.html", id = id)

@app.route("/track/<string:id>.html/")
def track(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Create new User
    result = cur.execute("SELECT question_id FROM trackquestions WHERE track_id = %s", [id])
    mysql.connection.commit()

    cur.execute("SELECT question_id FROM trackquestions WHERE track_id = %s", [id])
    mysql.connection.commit()

    track = cur.fetchall()
    questions = list()
    for i in track:
        cur.execute("SELECT * FROM question WHERE question_id = %s", [i["question_id"]])
        mysql.connection.commit()
        temp = cur.fetchone()
        questions.append(temp)

    cur.close()

    return render_template("Track.html", questions = questions, id = id)


@app.route("/joinTrack.html", methods = ['GET', 'POST'])
def joinTrack():

    class SelectTrackForm(Form):
        id = StringField('id', [validators.Length(min=1, max=50)])
    form = SelectTrackForm(request.form)

    # Create cursor
    cur = mysql.connection.cursor()

    # Get all the tracks
    result = cur.execute("SELECT * FROM track")
    mysql.connection.commit()
    tracks = cur.fetchall();

    if result > 0:
        if request.method == "POST":
            trackId = form.id.data
            cur.execute("SELECT user_id FROM user WHERE email = %s", [session["email"]])
            mysql.connection.commit()
            userId = cur.fetchone()
            try:
                cur.execute("INSERT INTO trackdeveloper(developer_id, track_id) VALUES(%s, %s)", (userId['user_id'], trackId))
                mysql.connection.commit()
            except:
                flash("Track already added! Redirecting to it", "success")

            return redirect(url_for("track", id = trackId))

        return render_template("joinTrack.html", tracks = tracks);
    else:
        error = 'No Tracks available'
        flash('No Tracks available')
        app.logger.info('No Tracks available')
        return render_template("joinTrack.html", error = error)



# Company Functions

@app.route("/compCreateTrack.html")
def compCreateTrack():

    # Create cursor
    cur = mysql.connection.cursor()

    # Create new User
    cur.execute("SELECT * FROM question")
    mysql.connection.commit()

    queryRespone = cur.fetchall();

    if len(queryRespone) == 0:
        flash ("There is not any question")
    else :
        print (queryRespone)



    return render_template("compCreateTrack.html")

@app.route("/compInviteDeveloper.html")
def compInviteDeveloper():


    # Create cursor
    cur = mysql.connection.cursor()

    # Create new User
    cur.execute("SELECT * FROM developer")
    mysql.connection.commit()

    queryRespone = cur.fetchall();

    if len(queryRespone) == 0:
        flash ("There is not any question")
    else :
        print (queryRespone)



    return render_template("compInviteDeveloper.html")

@app.route("/compHome.html")
def compHome():
    return render_template("compHome.html")

@app.route("/compSelectTrack.html")
def compSelectTrack():

    # Create cursor
    cur = mysql.connection.cursor()

    # Create new User
    cur.execute("SELECT DISTINCT track_id FROM track")
    mysql.connection.commit()

    queryResponse = cur.fetchall();

    if len(queryResponse) == 0:
        flash ("There is not any track")
    else :
        print (queryResponse)

    return render_template("compSelectTrack.html", track = queryResponse)

@app.route("/compReviewTrack.html")
def compReviewTrack():
    return render_template("compReviewTrack.html")

@app.route("/comSignIn.html", methods=['GET', 'POST'])
def comSignIn():

    class SignIn(Form):
        email = StringField('Email', [validators.Length(min=6, max=50)])
        password = PasswordField('Password', [validators.DataRequired(),
                    validators.EqualTo('confirm', message="Passwords do not match!")])

    form = SignIn(request.form)

    if (request.method == "POST"):

        email = form.email.data
        password = form.password.data

        # Create Cursor
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user, compRep " +
         "WHERE User.user_id = compRep.compRep_id AND User.email = '{0}' AND User.password = '{1}'".format(email , password))
        mysql.connection.commit()

        # Get response
        queryResponse = cur.fetchall();

        if (len(queryResponse) == 0):
            flash("Email or Password is incorrect")
        else:
            return redirect(url_for("compHome"))


    return render_template("comSignIn.html" , form=form)

@app.route("/comSignUp.html" , methods=['GET', 'POST'] )
def comSignUp():

    class RegisterForm(Form):

        companyName = StringField('Company Name', [validators.Length(min=1, max=50)])
        agentName = StringField('Agent Name', [validators.Length(min=4, max=25)])
        email = StringField('Email', [validators.Length(min=6, max=50)])
        password = PasswordField('Password', [validators.DataRequired(),
                    validators.EqualTo('confirm', message="Passwords do not match!")])
        confirm = PasswordField('Confirm Password')

    form = RegisterForm(request.form)

    if request.method == 'POST':

        agentName = form.agentName.data
        companyName = form.companyName.data
        email = form.email.data
        password = form.password.data

        # Create cursor
        cur = mysql.connection.cursor()

        # Create new User
        cur.execute("INSERT INTO User(name, email, password) VALUES(%s, %s, %s)", (agentName, email, password))
        mysql.connection.commit()

        # Get User Id
        cur.execute("Select user_id from User where email='{0}'".format(email));
        mysql.connection.commit();
        userid = cur.fetchall()[0]['user_id']

        # Create new Company Rep
        cur.execute("INSERT INTO compRep(compRep_id , comp_name) VALUES(%s , %s)", (userid , companyName))
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash("You are now registered successfully", 'success')

        return redirect(url_for('index'))


    return render_template("comSignUp.html" , form = form)

# Admin Functions

@app.route("/adminSignIn.html")
def adminSignIn():
    return render_template("adminSignIn.html")


if __name__== '__main__':
    app.secret_key = "difficult"
    app.run()
