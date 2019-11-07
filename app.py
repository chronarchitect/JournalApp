import hashlib
import sqlite3
from flask import Flask, render_template, redirect, url_for, request

user_logged_in = "N/A"
DATABASE_PATH = 'static/database.db'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion == False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('timeline')
    return render_template('login.html', error=error)

@app.route('/timeline', methods=['GET'])
def timeline():
    return 'timeline page'

@app.route('/secret', methods=['GET'])
def secret():
    return "secret page"

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (check_user_exists(username)):
            error = 'Username already taken'
        else:
            add_user(username, password)
            return redirect(url_for('login'))
    return render_template('register.html', error=error)

def check_user_exists(username):
    exists = False
    con = sqlite3.connect(DATABASE_PATH)
    with con:
        cur = con.cursor()
        cur.execute("SELECT username FROM USERS WHERE username=\'" + username + "\'" )
        if(len(cur.fetchall()) != 0):
            exists = True
    return exists        

def add_user(username, password):
    con = sqlite3.connect(DATABASE_PATH)
    with con:
        cur = con.cursor()
        cur.execute('INSERT INTO USERS (USERNAME, PASSWORD) VALUES (?, ?)', (username, password))

def check_password(dbPass, password):
    return dbPass == password

def validate(username, password):
    con = sqlite3.connect(DATABASE_PATH)
    completion = False
    with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[0]
                    dbPass = row[1]
                    if dbUser==username:
                        completion=check_password(dbPass, password)
    return completion
