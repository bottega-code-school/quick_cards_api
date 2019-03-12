from flask import Flask, request, jsonify
from flask_heroku import Heroku

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>Sup Dawggg</h1>"

if __name__ == "__main__":
  app.debug = True
  app.run()
