from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import sys


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
        print("here")
        if request.method == 'POST':
            name = form.name.data
            email = form.email.data
            password = form.password.data

            # Create cursor
            cur = mysql.connection.cursor()

            # Create new User and check if already exists
            try:
                cur.execute("INSERT INTO User(name, email, password) VALUES(%s, %s, %s)", (name, email, password))
                mysql.connection.commit()
            except:
                app.logger.info('Email exists already')
                
                return redirect(url_for("devSignUp"))

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
            return redirect(url_for('index'))
    return render_template("devSignUp.html", form = form)

@app.route("/devSignIn.html", methods=['GET', 'POST'])
def devSignIn():
    if session.get("logged_in") == True:
        return redirect(url_for("devHome"))
    elif request.method == 'POST':
        email = request.form['email']
        password_candidate = request.form['password']

        # Create Cursor
        cur = mysql.connection.cursor()

        result = cur.execute("SELECT * FROM User WHERE email = %s", [email])
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

compCreatedTrackId = 0;

@app.route("/compCreateTrack.html", methods=['GET', 'POST'])
def compCreateTrack():

    # Create cursor
    cur = mysql.connection.cursor()

    # Create new User
    cur.execute("SELECT * FROM Question")      
    mysql.connection.commit()

    queryResponse = cur.fetchall();

    if len(queryResponse) == 0:
        flash ("There is not any question")
    #else :
     #   print (queryResponse)

    #print(len(queryResponse), file=sys.stderr)
    
    
    #trackResult[0];

    class CreateTrackForm(Form):
        id = StringField('id', [validators.Length(min=1, max=50)])
    form = CreateTrackForm(request.form)

    global compCreatedTrackId 

    if request.method == "POST":
        id = form.id.data
        print(id, file=sys.stderr)
        print(compCreatedTrackId)
        print("IDIDIDIDIDID===",id)

        if id !='0':
            cur.execute("INSERT INTO trackquestions (question_id, track_id) VALUES(%s,%s)", [id,compCreatedTrackId]);      
            mysql.connection.commit()   
        else:
            return redirect(url_for('compReviewTrack')) 
    else:
        trackName = "Track";
        cur.execute("INSERT INTO track (track_name) VALUES(%s)", [trackName]);      
        mysql.connection.commit() 
        
        cur.execute("SELECT track_id FROM track");      
        mysql.connection.commit() 
        trackResult = cur.fetchall();
        
        compCreatedTrackId = (trackResult[len(trackResult)-1]["track_id"]);
        print (compCreatedTrackId);

        #print (buttons[0], buttons[1],buttons[2],buttons[3])
        #return redirect(url_for('compHome'))
       
    return render_template("compCreateTrack.html", question = queryResponse)

@app.route("/compInviteDeveloper.html",methods=['GET', 'POST'])
def compInviteDeveloper():


    # Create cursor
    cur = mysql.connection.cursor()

    # Create new User
    cur.execute("SELECT name FROM user, developer WHERE user_id = developer_id")      
    mysql.connection.commit()
    queryResponse = cur.fetchall();

    print(queryResponse)

    if len(queryResponse) == 0:
        flash ("There is not any developer")
    else :
        print (queryResponse)

    
    class InviteForm(Form):
        id = StringField('id', [validators.Length(min=1, max=50)])
    form = InviteForm(request.form)

    global compCreatedTrackId 

    if request.method == "POST":
        id = form.id.data
        print(id, file=sys.stderr)



    return render_template("compInviteDeveloper.html",developer = queryResponse)

@app.route("/compHome.html")
def compHome():
    return render_template("compHome.html")


@app.route("/compSelectTrack.html")
def compSelectTrack():

    # Create cursor
    cur = mysql.connection.cursor()

    # Create new User
    cur.execute("SELECT * FROM Track")        
    mysql.connection.commit()

    queryRespone = cur.fetchall();

    if len(queryRespone) == 0:
        flash ("There is not any track")
    else :
        print (queryRespone)

    return render_template("compSelectTrack.html", track = queryRespone);

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

@app.route("/adminSignIn.html")
def adminSignIn():
    return render_template("adminSignIn.html")

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
