from scrumble import app
from flask import request, url_for, render_template
import os
import requests    

@app.route('/')
def main():
    """Index Controller"""
    return render_template('index.html')
  

@app.route('/teacherindex')
def teacherindex():
    """Index Controller"""
    return render_template('teacherindex.html')

  
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
