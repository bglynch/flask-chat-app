import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Stores messages between requests
messages = []

# root of our website
@app.route("/")
def landing_page():
    return render_template("index.html")

# 
@app.route("/<username>")
def get_user_page(username):
    return str(messages)
    

@app.route("/<username>/<message>")
def add_message(username, message):
    message = "<strong>{0}: </strong> {1}".format(username, message)
    messages.append(message)
    return str(messages)

@app.route("/login")
def get_username():
    username = request.args.get('received_name')
    return redirect(username)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug = True)


