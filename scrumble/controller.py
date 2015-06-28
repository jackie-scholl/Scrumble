from scrumble import app
from flask import request, url_for, render_template
import os
import requests
import cgi

@app.route('/')
def main():
    """Index Controller"""
    return render_template('index.html')
  

@app.route('/teacherindex')
def teacherindex():
    """Index Controller"""
    return render_template('teacherindex.html')

@app.route('/rebuild/<boardname>')
def rebuild(boardname):
    """Rebuild Controller"""
    from trolly.client import Client
    api_key = "bf71d01b024c31a1c294b4755af55add"
    token = "404f4361c2e9bf578e355862ffaf603226c9bddfde60b4c44f6a3e9ed7d917cd"
    c = Client(api_key, token)
    boards = c.get_boards()
    board = [x for x in boards if x.name.find(boardname) >= 0][0]
    lists = board.get_lists()
    backlog = lists[0]
    groups = [[x.strip() for x in y.name.split(",")] for y in lists[1].get_cards()]
    return cgi.escape(str("backlog: " + str(backlog) + "<br />groups: " + str(groups)))
  
@app.route('/managetasks')
def managetasks():
    """Index Controller"""
    return render_template('managetasks.html')
  
  
@app.route('/managetaskspurple')
def managetaskspurple():
    """Index Controller"""
    return render_template('managetaskspurple.html')
  

@app.route('/managegroups')
def managegroups():
    """Index Controller"""
    return render_template('managegroups.html')
  
@app.route('/managestudents')
def managestudents():
    """Index Controller"""
    return render_template('managestudents.html')

@app.errorhandler(404)
def handle_error(e):
    return render_template('404.html')
