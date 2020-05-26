from flask import Flask, render_template, request, session
from flask_session import Session
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
#app = Flask(__name__)


'''posts = [
        {
        "name":"John",
        "date":"13.3.2020",
        "topic":"Coronavirus school shutdowns",
        },
    ]'''

@app.route("/", methods = ["GET", "POST"])
def index():
    if session.get("posts") is None:
        session["posts"] = [
        {
        "name":"John",
        "date":"13.3.2020",
        "topic":"Coronavirus school shutdowns",
        },
    ]
    if request.method == "POST":
        mydict = {}
        for key,val in request.form.items():
            mydict[key] = val
            print(mydict)
        session["posts"].append(mydict)

    return render_template("index.html",posts = session["posts"])

@app.route("/write")
def write():
    return render_template("master.html")
