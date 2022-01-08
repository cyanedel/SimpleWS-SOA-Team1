import os
import json
from flask import Flask, jsonify

app = Flask(__name__)
dirname = os.path.dirname(__file__)

with open(os.path.join(dirname,'countryList.json'), errors="ignore") as f:
  countryList = json.load(f)

with open(os.path.join(dirname,'user_list.json'), errors="ignore") as f:
  userList = json.load(f)

@app.get("/getcountrylist")
def get_countries():
    return jsonify(countryList)

@app.get("/getuserlist")
def get_userList():
    return jsonify(userList)

if __name__ == '__main__':
  app.run(port=3200)