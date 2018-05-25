import os
from flask import Flask, redirect, render_template, request

# creates the flask app.
app = Flask(__name__)

# Stores messages between requests
messages = []

banned_words = ['feck', 'arse', 'girls']

# rooms = {
#     ?? : ??
# }
''' Creates new rooms, need dictionary '''
# @app.route('rooms/add')
# def add_room():
#     roomname = request.form['roomname']
#     rooms[roomname] = []
#     return redirect(....)

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


# username/new is a dump file for the chat form
@app.route("/<username>/new", methods=["POST"])
def add_message(username):
    text = request.form['message']
    # if a word in the list equals a word in the banned list,
    # replace word with ***

    words_list = text.split()
    new_words_list = []
    for individual_word in words_list:
        if individual_word in banned_words:
            new_words_list.append(len(individual_word)*'*')
        else:
            new_words_list.append(individual_word)
    text = ' '.join(new_words_list)
    
    '''
    List comprehension method
    words = text.split()
    words = [ "*" * len(word) if word.lower() in banned_words else word for word in words]
    text = " ".join(map(str,words))
    '''
    
    message = {
        'sender':username,
        'body': text
    }
    messages.append(message)
    return redirect(username)


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')))


