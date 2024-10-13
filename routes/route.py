from flask import Flask, render_template, request, jsonify
from server import app
from controllers.control import *

@app.route('/')
def home_page():
    return func_home_page()

@app.route('/register_page')
def register():
    return func_register()
  
@app.route('/register_user', methods=["post"])
def register_user():
    return func_register_user()

@app.route('/consult_page')
def consult():
    return func_consult()

@app.route('/consult_user', methods=["post"])
def consult_user():
    print(request.get_json())
    return func_consult_user()