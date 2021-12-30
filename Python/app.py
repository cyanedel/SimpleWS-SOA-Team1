import json
from flask import Flask, jsonify

app = Flask(__name__)

with open('countryList.json', errors="ignore") as f:
  countryList = json.load(f)

@app.get("/getcountrylist")
def get_countries():
    return jsonify(countryList)

if __name__ == '__main__':
  app.run(port=3200)