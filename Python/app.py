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
    result = [user for user in userList if user.get('gender').lower() == args['gender'].lower()]
  
  print(result)
  return jsonify(result)

if __name__ == '__main__':
  app.run(port=3200)