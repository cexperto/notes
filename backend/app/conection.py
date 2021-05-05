from app.config import host,port, database, user, password
import psycopg2


connection = psycopg2.connect(user= "ylgcuwgqfktndd",
                                password= "5cb7fdab06b8649f26b9b46f97cae5c38d6c1c0b7c3bf466509a46914bb4a9a0",
                                host= "ec2-18-214-195-34.compute-1.amazonaws.com",
                                port="5432",
                                database="dde3v21e2ktfom")
