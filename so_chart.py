from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/")
def index():
    return render_template("index.html")

#run using python -m flask or flask
# full command would be flask --app so_chart run

#somehow make it so route for search gets sent to api and api then sends search result number to 
# chart