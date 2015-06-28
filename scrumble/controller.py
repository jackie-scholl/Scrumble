from scrumble import app
from flask import request, url_for, render_template
import os
import requests
import cgi


@app.route('/')
def index():
    """Index Controller"""
    return render_template('teacherindex.html')
  

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


@app.route('/rebuild/<boardname>')
def rebuild(boardname):
    """Rebuild Controller"""
    from trolly.client import Client
    from trolly.exceptions import ResourceUnavailable
    import uuid
    api_key = "bf71d01b024c31a1c294b4755af55add"
    token = "404f4361c2e9bf578e355862ffaf603226c9bddfde60b4c44f6a3e9ed7d917cd"
    c = Client(api_key, token)
    boards = c.get_boards()
    board = [x for x in boards if x.name == boardname][0]
    lists = board.get_lists()
    backlog = lists[0]
    groups = [[x.strip() for x in y.name.split(",")] for y in lists[1].get_cards()]
    boards_to_delete = [x for x in boards if x.name.find(boardname) == 0 and len(x.name) > len(boardname)]
    [b.close_board(True) for b in boards_to_delete]
    out = []
    for x in range(len(groups)):
        b = create_board(c, "Cell Biology Group %s" % (x + 1))
        out.append(b)
        for m in groups[x]:
            try:
                b.add_member(get_email(m), m)
            except ResourceUnavailable:
                pass
        l = b.add_list(query_params={"name": "backlog"})
        for c in b.get_cards():
            l.add_card(query_params={"name": "backlog"})
    return cgi.escape(str(out))

def create_board(client, name):
    return client.add_board(name)
    #, "id": uuid.uuid4().hex

def get_email(name):
    map = {"Keller Scholl": "keller.scholl@gmail.com",
     "Jonathon Kwan": "jkwan2011@gmail.com",
     "Aditi Joshi":   "adisababy@gmail.com",
     "Laura Ballek":  "lauraballek@gmail.com"}
    try:
        return map[name]
    except KeyError:
        l = name.split(" ")
        return "%s.%s@example.edu" % (l[0], l[1])
        
