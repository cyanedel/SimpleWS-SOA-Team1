import os
import json
from flask import Flask, jsonify, request

app = Flask(__name__)
dirname = os.path.dirname(__file__)

with open(os.path.join(dirname,'user_list.json'), errors="ignore") as f:
  userList = json.load(f)

@app.get("/getuserlist")
def get_userList():
  args = request.args
  result = userList

  if 'gender' in args:
    if args['gender'] != "":
      result = [user for user in result if user.get('gender').lower() == args['gender'].lower()]

  if 'firstname' in args:
    if args['firstname'] != "":
      result = [user for user in result if args['firstname'].lower() in user.get('first_name').lower()]
  
  if 'lastname' in args:
    if args['lastname'] != "":
      result = [user for user in result if args['lastname'].lower() in user.get('last_name').lower()]
  
  print(result)
  return jsonify(result)

if __name__ == '__main__':
  app.run(port=3200)