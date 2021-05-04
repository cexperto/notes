from flask import Flask, request, jsonify, make_response
from sqlalchemy import *


from app.config import *

import psycopg2


app = Flask(__name__)




conn_str = f'postgresql://{user}:{password}@{host}/{database}'
engine = create_engine(conn_str)
connection = engine.connect()
metadata = MetaData()

connection = psycopg2.connect(user= "ylgcuwgqfktndd",
                                password= "5cb7fdab06b8649f26b9b46f97cae5c38d6c1c0b7c3bf466509a46914bb4a9a0",
                                host= "ec2-18-214-195-34.compute-1.amazonaws.com",
                                port="5432",
                                database="dde3v21e2ktfom")

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
