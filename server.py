from flask import Flask, render_template, request
from database.db import connectionSQL, add_user

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/register_page')
def register():
    return render_template("register.html")

@app.route('/register_user', methods=["post"])
def register_user():
    data_user = request.form
    id = data_user["id"]
    name = data_user["name"]
    lastname = data_user["lastname"]
    birthday = data_user["birthday"]
    add_user(id, name, lastname, birthday)
    return "User added"

if __name__ == "__main__":
    ip = "172.31.20.248"
    port = "80"
    app.run(ip, port, debug=True)