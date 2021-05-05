from flask import Flask, request, jsonify, make_response
from sqlalchemy import *

from app.config import *

import psycopg2
from app.conection import connection

app = Flask(__name__)



@app.route('/')
def index():    
    return 'api notas'

@app.route('/teachers')
def teachers():    
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT id_t, name FROM teachers"
    cursor.execute(postgreSQL_select_Query)
    teachers = cursor.fetchall()
        
    return make_response(
        jsonify({
            "teachers: id, name": str(teachers)
        })
    )


@app.route('/courses')
def courses():
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT id_c, name_c FROM courses"
    cursor.execute(postgreSQL_select_Query)
    courses = cursor.fetchall()
        
    return make_response(
        jsonify({
            "courses: id, name": str(courses)
        })
    )

@app.route('/students')
def students():
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT id_s, name_s FROM students"
    cursor.execute(postgreSQL_select_Query)
    students = cursor.fetchall()
        
    return make_response(
        jsonify({
            "students: id, name": str(students)
        })
    )

@app.route('/tg')
def teachersGroups():
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT DISTINCT t.id_t, t.name, g.name_g, g.fk_teacher FROM teachers as t INNER JOIN groups as g ON t.id_t=g.fk_teacher ORDER BY t.id_t"
    
    cursor.execute(postgreSQL_select_Query)
    tg = cursor.fetchall()
    
           
    return make_response(
        jsonify({
            "teacher name, course name": str(tg)
        })
    )

# teacher gropus students
@app.route('/tgs')
def teachersGroupsStudents():
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT t.id_t, t.name, g.name_g, g.fk_teacher, s.id_s, s.name_s, s.fk_group FROM teachers as t INNER JOIN groups as g  ON t.id_t=g.fk_teacher INNER JOIN students as s ON  g.id_g=s.fk_group ORDER BY t.id_t"
    
    cursor.execute(postgreSQL_select_Query)
    tgs = cursor.fetchall()
    
           
    return make_response(
        jsonify({
            "teacher name, course name, student name": str(tgs)
        })
    )

# name owner teacher group with their students
@app.route('/ts')
def studentsNotes():
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT t.id_t, t.name, g.name_g, g.fk_teacher, s.id_s, s.name_s, s.fk_group FROM teachers as t INNER JOIN groups as g  ON t.id_t=g.fk_teacher INNER JOIN students as s ON  g.id_g=s.fk_group ORDER BY t.id_t"
    # nombre del profesor que tiene este grupo con sus estudiantes
    cursor.execute(postgreSQL_select_Query)
    tgs = cursor.fetchall()
    
           
    return make_response(
        jsonify({
            "teacher name, groupe name, student name": str(tgs)
        })
    )


# request id course for looking student list and notes
@app.route('/notes/<id_c>', methods=['POST','GET'])
def queryNotes(id_c):
    course_id = int(id_c)
    if (course_id>28):
        return make_response("the course doesn't exist")

    cursor = connection.cursor()
    
    query = f"SELECT c.id_c, c.name_c, s.id_s, s.name_s, n.period1,n.period2,n.period3,n.fk_student,n.fk_course FROM courses c INNER JOIN notes as n ON c.id_c={course_id} AND n.fk_course={course_id} INNER JOIN students as s ON n.fk_student=s.id_s"
    cursor.execute(query)
    tgs = cursor.fetchall()
    
           
    return make_response(
        jsonify({
            "notes: id name course, id name student, notes p1 p2 p3, estudent course id ": str(tgs),            
        })
    )


@app.route('/updateNotes', methods=['POST'])
def updateNotes():
    request_data = request.get_json()
    notes =[]
    cursor = connection.cursor()
    for items in request_data.values():
        notes.append(items)
    id = int(notes[0])
    p1 = float(notes[1])
    p2 = float(notes[2])
    p3 = float(notes[3])
    query=f"UPDATE notes SET period1={p1}, period2={p2}, period3={p3} WHERE id_n={id}"
    cursor.execute(query)
    

    return make_response(
        jsonify({
            " ": "ok"
        })
    )

