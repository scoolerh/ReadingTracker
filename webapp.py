import flask 
from flask import render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import json
import sys
import subprocess

app = flask.Flask(__name__)

app.secret_key = 'your secret key'

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PASSWORD'] = 'your password'
app.config['MYSQL_DB'] = 'readingtrackerlogin'

mysql = MySQL(app)

@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def home():
    '''
    Run the home page of the website. 
    '''
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password, ))
        account = cursor.fetchone()
        if account: 
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in!'
            return render_template('index.html', msg = msg)
        else: 
            msg = "Incorrect username or password."
    return render_template('index.html', msg = msg)

@app.route('logout')
def logout(): 
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    '''
    Run the sign up page. 
    '''
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username, ))
        account = cursor.fetchone()
        if account: 
            msg = "Account already exists."
        elif not re.match(r'[^@+@[^@]+\.[^@]+', email): 
            msg = "Invalid email address."
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = "Username must contain only characters and numbers."
        elif not username or not password or not email: 
            msg = "You are missing at least one field."
        else: 
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s', (username, password, email, ))
            mysql.connection.commit()
            msg = "You have signed up!"
    elif request.mehtod == 'POST': 
        msg = "You are missing at least one field."
    return render_template('signup.html', msg = msg)

@app.route('/login')
def login():
    '''
    Run the log in page.
    '''
    return render_template('login.html')

@app.route('/pagetracker')
def pages():
    ''' 
    Run the page tracker. 
    '''
    return render_template('pages.html')

@app.route('/completedbooks')
def books():
    '''
    Run the bookshelf. 
    '''
    return render_template('books.html')

@app.route('/stats')
def stats():
    '''
    Run the statistics. 
    '''
    return render_template('stats.html')

if __name__ == '__main__': 
    app.run()