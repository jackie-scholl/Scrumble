from scrumble import app
from flask import request, url_for, render_template, session

import os
import requests
import cgi
from requester import *



@app.route('/')
def index():
    """Index Controller"""
    return render_template('login.html')
  

@app.route('/teacherindex', methods=['POST'])
def teacherindex():
    """Index Controller"""
    session['teacher_name'] = (request.form['teacher_name'])
    teacher_name = session['teacher_name'] 
    session['students'] = get_students(session['teacher_name'])
    return render_template('teacherindex.html', teacher_name=teacher_name)
  
  
@app.route('/teacherindex2')
def teacherindex2():
    """Index Controller"""
    return render_template('teacherindex2.html', teacher_name=teacher_name)

  
@app.route('/managetasks')
def managetasks():
    """Index Controller"""
    teacher_name = session['teacher_name'] 
    return render_template('managetasks.html', teacher_name=teacher_name)
  
  
@app.route('/managetaskspurple')
def managetaskspurple():
    """Index Controller"""
    teacher_name = session['teacher_name'] 
    return render_template('managetaskspurple.html', teacher_name=teacher_name)
  

@app.route('/managegroups')
def managegroups():
    """Index Controller"""
    teacher_name = session['teacher_name'] 
    students = session['students']
    return render_template('managegroups.html', teacher_name=teacher_name, students=students)
  
@app.route('/managestudents')
def managestudents():
    """Index Controller"""
    teacher_name = session['teacher_name'] 
    students = session['students']
    return render_template('managestudents.html', teacher_name=teacher_name, students=students)

def get_client():
    TROLLY_API_KEY = "bf71d01b024c31a1c294b4755af55add"
    TROLLY_TOKEN = "404f4361c2e9bf578e355862ffaf603226c9bddfde60b4c44f6a3e9ed7d917cd"
    from trolly.client import Client
    from trolly.exceptions import ResourceUnavailable
    return Client(TROLLY_API_KEY, TROLLY_TOKEN)
    #boards = client.get_boards()
    #return [x for x in boards if x.name == boardname][0]

@app.route('/rebuild/<boardname>')
def rebuild(boardname):
    """Rebuild Controller"""
    client = get_client()
    boards = client.get_boards()
    board = [x for x in boards if x.name == boardname][0]
    board = get_board(boardname)
    lists = board.get_lists()
    backlog = lists[0]
    groups = [[x.strip() for x in y.name.split(",")] for y in lists[1].get_cards()]
    boards_to_delete = [x for x in boards if x.name.find(boardname) == 0 and len(x.name) > len(boardname)]
    [b.close_board(True) for b in boards_to_delete]
    out = []
    for x in range(len(groups)):
        b = create_board(client, "Cell Biology Group %s" % (x + 1))
        out.append(b)
        for m in groups[x]:
            try:
                b.add_member(get_email(m), m)
            except ResourceUnavailable:
                pass
        [l.update_list(query_params={"closed":"true"}) for l in b.get_lists()]
        b.add_list(query_params={"name": "Sprint"})
        b.add_list(query_params={"name": "Done"})
        back_list = b.add_list(query_params={"name": "Backlog"})
        for card in backlog.get_cards():
            added = copy_card(back_list, card)
            out.append(added)
    return cgi.escape(str(out))

def create_board(client, name):
    return client.add_board(name)

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

def copy_card(list, original):
    c = original.get_card_information()
    c2 = dict()
    c2['name'] = c['name']
    c2['due'] = c['due'] or "null"
    if c['desc'] != '':
         c2['desc'] = c['desc']
    if c['labels']:
        c2['labels'] = ",".join(c['labels'])
    return list.add_card(query_params=c2)

@app.route('/update_assignments/<boardname>')
def update_assignments(boardname):
    client = get_client()
    boards = [x for x in client.get_boards() if x.name.find(boardname) == 0]
    for board in boards:
        for list in board.get_lists():
            is_done = (list.name == "Done")
            for card in list.get_cards():
                ensure_assigned(card, card.get_members(), is_done)
    return "Done!"

def ensure_assigned(card, students, is_done):
    make_assignment(get_assignment(card, students, is_done))

def get_assignment(card, students, is_done):
    card_map = card.get_card_information()
    status = 'TURNED_IN' if is_done else 'IN_PROGRESS'
    students_string = '[' + ",".join([s.name for s in students]) + ']'
    return '{"schoolRefId": "","leaRefId": "","sectionRefId": "","students": %s,"refId": "%s","staffRefId": "","availableDate": "","dueDate": "","name": "%s","description": "%s","creatorRefId": "","administratorRefId": "","sourceObjects": [],"status": "%s"}' % (students_string, card_map['id'], card_map['name'], card_map['desc'], status)


@app.errorhandler(404)
def handle_error(e):
    return render_template('404.html')