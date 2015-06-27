from scrumble import app
from flask import request, url_for, render_template
import os
import requests    

@app.route('/')
def main():
    """Index Controller"""
    return render_template('index.html')


@app.errorhandler(404)
def handle_error(e):
    return render_template('404.html')
