from flask import Flask,render_template



app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/devSignIn.html")
def devSignIn():
    return render_template("devSignIn.html")

@app.route("/devSignUp.html")
def devSignUp():
    return render_template("devSignUp.html")

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

@app.route("/questionDetails.html")
def questionDetails():
    return render_template("questionDetails.html")

@app.route("/discussion.html")
def discussion():
    return render_template("discussion.html")

if __name__== "__main__":
    app.run(debug = True)