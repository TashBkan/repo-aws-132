from flask import Flask, render_template, request
from database.db import connectionSQL, add_user
from controllers.admin_s3 import *

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
    data_photo = request.files
    id = data_user["id"]
    name = data_user["name"]
    lastname = data_user["lastname"]
    birthday = data_user["birthday"]
    photo = data_photo["photo"]
    confirm = add_user(id, name, lastname, birthday)
    if confirm:
        photo_path, photo_name = save_file(photo, id)
        upload_file(photo_path, photo_name)
        return "User added"
    else:
        return "Error creating the user"
    

if __name__ == "__main__":
    ip = "172.31.20.248"
    port = "80"
    app.run(ip, port, debug=True)