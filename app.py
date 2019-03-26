from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://xqvrdtjjrillen:6f2a0915b506c64482dd7be2fd3129ff7d9a57f45ab543cd30cd1691482ca202@ec2-107-20-177-161.compute-1.amazonaws.com:5432/d90t4tcbeg7t43"
heroku = Heroku(app)
db = SQLAlchemy(app)

class Student(db.Model):
  __tablename__ = "students"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  linkedin = db.Column(db.String(100), unique=True)
  image = db.Column(db.String())
  summary = db.Column(db.String())
  python_skill = db.Column(db.String(5))
  react_skill = db.Column(db.String(5))
  github_skill = db.Column(db.String(5))
  json_skill = db.Column(db.String(5))
  css_scss_skill = db.Column(db.String(5))
  data_type_skill = db.Column(db.String(5))
  sql_skill = db.Column(db.String(5))
  javascript_skill = db.Column(db.String(5))
  html_skill = db.Column(db.String(5))
  uml_skill = db.Column(db.String(5))
  ui_ux_skill = db.Column(db.String(5))

  def __init__(self, name, linkedin, image, summary, python_skill, react_skill, github_skill, json_skill, css_scss_skill, data_type_skill, sql_skill, javascript_skill, html_skill, uml_skill, ui_ux_skill):
    self.name = name
    self.linkedin = linkedin
    self.image = image
    self.summary = summary
    self.python_skill = python_skill
    self.react_skill = react_skill
    self.github_skill = github_skill
    self.json_skill = json_skill
    self.css_scss_skill = css_scss_skill
    self.data_type_skill = data_type_skill
    self.sql_skill = sql_skill
    self.javascript_skill = javascript_skill
    self.html_skill = html_skill
    self.uml_skill = uml_skill
    self.ui_ux_skill = ui_ux_skill


@app.route("/")
def home():
  return "<h1>Bottega Quick Cards API</h1>"

@app.route("/add_student", methods=["POST"])
def add_student():
  if request.content_type == "application/json":
    post_data = request.get_json()

    name = post_data.get("name")
    linkedin = post_data.get("linkedIn")
    image = post_data.get("image")
    summary = post_data.get("summary")
    python_skill = post_data.get("python")
    react_skill = post_data.get("react")
    github_skill = post_data.get("github")
    json_skill = post_data.get("json")
    css_scss_skill = post_data.get("cssScss")
    data_type_skill = post_data.get("dataType")
    sql_skill = post_data.get("sql")
    javascript_skill = post_data.get("javaScript")
    html_skill = post_data.get("html")
    uml_skill = post_data.get("uml")
    ui_ux_skill = post_data.get("uiUx")

    register_student = Student(name, linkedin, image, summary, python_skill, react_skill, github_skill, json_skill, css_scss_skill, data_type_skill, sql_skill, javascript_skill, html_skill, uml_skill, ui_ux_skill)

    db.session.add(register_student)
    db.session.commit()
    return "Student Successfully Submitted"
  return ""

@app.route("/return_students", methods=["GET"])
def return_students():
  all_students = db.session.query(Student.id, Student.name, Student.linkedin, Student.image, Student.summary, Student.python_skill, Student.react_skill, Student.github_skill, Student.json_skill, Student.css_scss_skill, Student.data_type_skill, Student.sql_skill, Student.javascript_skill, Student.html_skill, Student.uml_skill, Student.ui_ux_skill).all()
  return jsonify(all_students)


if __name__ == "__main__":
  app.debug = True
  app.run()