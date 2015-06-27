from scrumble import app
from flask import request, url_for, render_template
import os
import requests

from trolly.client import Client

@app.route('/')
def main():
    """Index Controller"""
    return render_template('index.html')
  

@app.route('/teacherindex.html')
def teacherindex():
    """Index Controller"""
    return render_template('teacherindex.html')

@app.route('/rebuild/<boardname>')
def rebuild(boardname):
    """Rebuild Controller"""
    api_key = "bf71d01b024c31a1c294b4755af55add"
    token = "404f4361c2e9bf578e355862ffaf603226c9bddfde60b4c44f6a3e9ed7d917cd"
    c = Client(api_key, token)
    return c.get_boards()
    ##return str([str(x) for x in c.get_boards()])
    

@app.errorhandler(404)
def handle_error(e):
    return render_template('404.html')
