import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Stores messages between requests
messages = []

# root of our website
@app.route("/")
def landing_page():
    return render_template("index.html")

# Type in user name
@app.route("/login")
def get_username():
    username = request.args.get('user')
    return redirect(username)
    
# Username page opens chat.html
@app.route("/<username>")
def get_user_page(username):
    return render_template("chat.html", the_username = username, the_messages = messages)
#                                       

# username/new is a dump file for the chat form
@app.route("/<username>/new", methods=["POST"])
def add_message(username):
    text = request.form['message']
    
    message = {
        'sender':username,
        'body': text
    }
    messages.append(message)
    return redirect(username)









app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug = True)


