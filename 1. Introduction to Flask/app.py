from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home():
	return "<h1 >Welcome to home page! </h1>"


@app.route("/about")
def about():
	return "<h1 >Welcome to about page! </h1>"


@app.route("/welcome/<name>")
def welcome(name):
	return f"<h1> Hi {name.title()}, you're welcome to this page. </h1>"


@app.route("/addition/<int:num>")
def addition(num):
	return f"<h1> Input is {num}, Output is {num + 10}   </h1>"

@app.route("/additiontwo/<int:num1>/<int:num2>")
def additiontwo(num1, num2):
	return f"<h1> Input is {num1} + {num2}, Output is {num1 + num2} </h1>"


if __name__ == "__main__":
	app.run(debug=True)