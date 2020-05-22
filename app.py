from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, RadioField
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



@app.route("/forgotPass.html")
def forgotPass():
    return render_template("forgotPass.html")

# Dev Functions


@app.route("/devSignUp.html", methods=['GET', 'POST'])
def devSignUp():

    class RegisterForm(Form):
        name = StringField('Name', [validators.Length(min=1, max=50)])
        username = StringField('Username', [validators.Length(min=4, max=25)])
        email = StringField('Email', [validators.Length(min=6, max=50)])
        password = PasswordField('Password', [validators.DataRequired(),
                    validators.EqualTo('confirm', message="Passwords do not match!")])
        confirm = PasswordField('Confirm Password')

    form = RegisterForm(request.form)
    print("here")
    if request.method == 'POST':
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # Create cursor
        cur = mysql.connection.cursor()
        
        # Create new User
        cur.execute("INSERT INTO User(name, email, password) VALUES(%s, %s, %s)", (name, email, password))
        mysql.connection.commit()

        # Get User Id
        cur.execute("Select user_id from User where email='{0}'".format(email));
        mysql.connection.commit();
        userid = cur.fetchall()[0]['user_id']

        print (userid)

        # Create new Developer 
        cur.execute("INSERT INTO Developer (developer_id) VALUES(%s)", [userid])
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash("You are now registered successfully", 'success')

        print("here22")
        return redirect(url_for('index'))
    return render_template("devSignUp.html", form = form)

@app.route("/devSignIn.html", methods=['GET', 'POST'])
def devSignIn():

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
        cur.execute("SELECT * FROM User, Developer " + 
         "WHERE User.user_id = Developer.developer_id AND User.email = '{0}' AND User.password = '{1}'".format(email , password))
        mysql.connection.commit()

        # Get response
        queryResponse = cur.fetchall();

        if (len(queryResponse) == 0):
            flash("Email or Password is incorrect")
        else:
            return redirect(url_for("devHome"))
    

    return render_template("devSignIn.html" , form=form)

@app.route("/devHome.html")
def devHome():
    return render_template("devHome.html")

@app.route("/adminHome.html")
def adminHome():
    return render_template("adminHome.html")

@app.route("/searchQuestion.html")
def searchQuestion():

    class SearchForm(Form):
        input = StringField("Input" ,[validators.Required("Please enter Question")] )

    form = SearchForm(request.form)

    if (request.method == "POST"):

        flush("HI")

    return render_template("searchQuestion.html" , form=form)

@app.route("/adminSearchUser.html")
def adminSearchUser():
    return render_template("adminSearchUser.html")

@app.route("/joinTrack.html")
def joinTrack():
    return render_template("joinTrack.html")

@app.route("/searchResult.html")
def searchResult():
    return render_template("searchResult.html")

@app.route("/adminCreateQuestion.html" , methods=['Get', 'POST'])
def adminCreateQuestion():
    class makeQuestion(Form):
        question = TextAreaField("Question: ",[validators.Required("Please enter Question")])
        answer = TextAreaField("Answer: ",[validators.Required("Please Answer")])
        dept_name = TextAreaField("Department Name: ",[validators.Required("dept_name")])
        difficulty = RadioField("Difficulty", choices=[("e" , "easy") , ('m' , 'medium') , ('l', 'large')])
    form = makeQuestion(request.form)
    if request.method == 'POST':
        print("in post")
        # Create Cursor
        cur = mysql.connection.cursor()

        question = form.question.data
        answer = form.answer.data
        difficulty = form.difficulty.data
        dept_name = form.dept_name.data
        test_case = ""
        approval = 1

        cur.execute("INSERT INTO question(dept_name, description, test_case, difficulty, approval)" +
            "VALUES ('{0}', '{1}', '{2}', '{3}', 0)".format(dept_name, question, test_case, difficulty))
        mysql.connection.commit()

        # Get response
        queryResponse = cur.fetchall();

        cur.close()
        return redirect(url_for("adminHome"))
    return render_template("adminCreateQuestion.html", form = form)

@app.route("/questionDetails/<string:id>/")
def questionDetails(id):
    return render_template("questionDetails.html", id = id)

@app.route("/discussion.html/<string:id>.html/")
def discussion(id):
    return render_template("discussion.html", id = id)

# Company Functions





@app.route("/postQuestion.html" , methods=['Get', 'POST'])
def postQuestion():
    class makeQuestion(Form):
        question = TextAreaField("Question: ",[validators.Required("Please enter Question")])
        answer = TextAreaField("Answer: ",[validators.Required("Please Answer")])
        dept_name = TextAreaField("Department Name: ",[validators.Required("dept_name")])
        difficulty = RadioField("Difficulty", choices=[("e" , "easy") , ('m' , 'medium') , ('l', 'large')])
    form = makeQuestion(request.form)
    if request.method == 'POST':
        print("in post")
        # Create Cursor
        cur = mysql.connection.cursor()

        question = form.question.data
        answer = form.answer.data
        difficulty = form.difficulty.data
        dept_name = form.dept_name.data
        test_case = ""
        approval = 0

        cur.execute("INSERT INTO question(dept_name, description, test_case, difficulty, approval)" +
            "VALUES ('{0}', '{1}', '{2}', '{3}', 0)".format(dept_name, question, test_case, difficulty))
        mysql.connection.commit()

        # Get response
        queryResponse = cur.fetchall();

        cur.close()
        return redirect(url_for("devHome"))

    return render_template("postQuestion.html", form = form)


@app.route("/compCreateTrack.html")
def compCreateTrack():

    # Create cursor
    cur = mysql.connection.cursor()

    # Create new User
    cur.execute("SELECT * FROM Question")      
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
    cur.execute("SELECT * FROM Developer")      
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
    cur.execute("SELECT DISTINCT track_id FROM Track")        
    mysql.connection.commit()

    queryRespone = cur.fetchall();

    if len(queryRespone) == 0:
        flash ("There is not any track")
    else :
        print (queryRespone)

    return render_template("compSelectTrack.html")

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
        cur.execute("SELECT * FROM User, compRep " + 
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

@app.route("/adminSignIn.html", methods=['GET', 'POST'])
def adminSignIn():

    class SignIn(Form):

        email = StringField('Username', [validators.Length(min=6, max=50)])
        password = PasswordField('Password', [validators.DataRequired(),
                    validators.EqualTo('confirm', message="Passwords do not match!")])
    
    form = SignIn(request.form)

    if (request.method == "POST"):

        email = form.email.data
        password = form.password.data

        # Create Cursor
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user, admin " + 
         "WHERE user.user_id = admin.admin_id AND user.name = '{0}' AND user.password = '{1}'".format(email , password))
        mysql.connection.commit()

        # Get response
        queryResponse = cur.fetchall();

        if (len(queryResponse) == 0):
            flash("Username or Password is incorrect")
        else:
            return redirect(url_for("adminHome"))
    

    return render_template("adminSignIn.html" , form=form)


if __name__== '__main__':
    app.secret_key = "difficult"
    app.run()