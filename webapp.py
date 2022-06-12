import flask 
from flask import render_template, request 
import json
import sys
import subprocess

app = flask.Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    '''
    Run the home page of the website. 
    '''
    output = subprocess.run(["php", "index.php"], stdout=subprocess.PIPE)
    return output.stdout

@app.route('/signup')
def signup():
    '''
    Run the sign up page. 
    '''
    return render_template('signup.php')

@app.route('/login')
def login():
    '''
    Run the log in page.
    '''
    return render_template('login.php')

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