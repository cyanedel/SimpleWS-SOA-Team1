# import os
# import json
from flask import Flask, jsonify, request

import psycopg2
from psycopg2 import Error

app = Flask(__name__)
# dirname = os.path.dirname(__file__)

# with open(os.path.join(dirname,'user-list.json'), errors="ignore") as f:
#   userList = json.load(f)

def db_conn():
  return psycopg2.connect(user="postgres", password="password", host="127.0.0.1", port="5432", database="soa")

def db_query(query):
  cursor = db_conn().cursor()
  cursor.execute(query)

  r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]

  # result = cursor.fetchall()
  cursor.connection.close()
  return r

@app.get("/getuserlist")
def get_userListDB():
  args = request.args
  select_query = "SELECT * FROM customer WHERE 1=1 "

  if 'gender' in args:
    if args['gender'] != "":
      select_query += " AND LOWER(gender) = '" + args['gender'].lower() +"'"

  if 'firstname' in args:
    if args['firstname'] != "":
      select_query += " AND LOWER(firstname) = '" + args['firstname'].lower() +"'"
  
  if 'lastname' in args:
    if args['lastname'] != "":
      select_query += " AND LOWER(lastname) = '" + args['lastname'].lower() +"'"

  if 'occupation' in args:
    if args['occupation'] != "":
      select_query += " AND LOWER(occupation) = '" + args['occupation'].lower() +"'"
  
  if 'id' in args:
    if args['id'] != "":
      select_query += " AND id = '" + args['id'] +"'"

  print(select_query)
  res = db_query(select_query)
  return jsonify(res)

# @app.get("/getuserlist2")
# def get_userList():
#   args = request.args
#   result = userList

#   if 'gender' in args:
#     if args['gender'] != "":
#       result = [user for user in result if user.get('gender').lower() == args['gender'].lower()]

#   if 'firstname' in args:
#     if args['firstname'] != "":
#       result = [user for user in result if args['firstname'].lower() in user.get('firstname').lower()]
  
#   if 'lastname' in args:
#     if args['lastname'] != "":
#       result = [user for user in result if args['lastname'].lower() in user.get('lastname').lower()]

#   if 'occupation' in args:
#     if args['occupation'] != "":
#       result = [user for user in result if args['occupation'].lower() in user.get('occupation').lower()]
  
#   return jsonify(result)

if __name__ == '__main__':
  app.run(port=3200)