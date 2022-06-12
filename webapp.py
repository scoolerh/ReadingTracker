import flask 
from flask import render_template, request 
import json
import sys

app = flask.Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    '''
    Run the home page of the website. 
    '''
    return render_template('index.php')

@app.route('/about')
def about():
    '''
    Run the about page of the website. 
    '''
    return render_template('about.html')

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