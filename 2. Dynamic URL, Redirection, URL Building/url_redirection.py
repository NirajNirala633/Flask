from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome to the Home Page! <h1>"

@app.route("/pass")
def passed():
    return "<h1> You have passed </h1>"

@app.route("/fail")
def failed():
    return "<h1> You have failed </h1>"


@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
        time.sleep(1)
        #  redirect user to page 'fail'
        return redirect(url_for("failed"))
    else: 
        time.sleep(1)
        # redirect user to page 'pass'
        return redirect(url_for("passed"))


if __name__ == "__main__":
    app.run(debug=True)