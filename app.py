from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://xqvrdtjjrillen:6f2a0915b506c64482dd7be2fd3129ff7d9a57f45ab543cd30cd1691482ca202@ec2-107-20-177-161.compute-1.amazonaws.com:5432/d90t4tcbeg7t43"
heroku = Heroku(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

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

  control_structures = db.Column(db.String(5))
  algorithms = db.Column(db.String(5))
  quality = db.Column(db.String(5))
  project_management = db.Column(db.String(5))
  problem_solving = db.Column(db.String(5))
  agile = db.Column(db.String(5))
  oop = db.Column(db.String(5))
  functional_programming = db.Column(db.String(5))
  software_engineering = db.Column(db.String(5))
  apis = db.Column(db.String(5))

  def __init__(self, name, linkedin, image, summary, python_skill, react_skill, github_skill, json_skill, css_scss_skill, data_type_skill, sql_skill, javascript_skill, html_skill, uml_skill, ui_ux_skill, control_structures, algorithms, quality, project_management, problem_solving, agile, oop, functional_programming, software_engineering, apis):
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

    self.control_structures = control_structures
    self.algorithms = algorithms
    self.quality = quality
    self.project_management = project_management
    self.problem_solving = problem_solving
    self.agile = agile
    self.oop = oop
    self.functional_programming = functional_programming
    self.software_engineering = software_engineering
    self.apis = apis

class StudentSchema(ma.Schema):
  class Meta:
    fields = ("id", "name", "linkedin", "image", "summary", "python_skill", "react_skill", "github_skill", "json_skill", "css_scss_skill", "data_type_skill", "sql_skill", "javascript_skill", "html_skill", "uml_skill", "ui_ux_skill", "control_structures", "algorithms", "quality", "project_management", "problem_solving", "agile", "oop", "functional_programming", "software_engineering", "apis")

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


@app.route("/")
def home():
  return "<h1>Bottega Quick Cards API</h1>"

@app.route("/add_student", methods=["POST"])
def add_student():
  if request.content_type == "application/json":
  
    name = request.json["name"]
    linkedin = request.json["linkedIn"]
    image = request.json["image"]
    summary = request.json["summary"]
    python_skill = request.json["python"]
    react_skill = request.json["react"]
    github_skill = request.json["github"]
    json_skill = request.json["json"]
    css_scss_skill = request.json["cssScss"]
    data_type_skill = request.json["dataType"]
    sql_skill = request.json["sql"]
    javascript_skill = request.json["javaScript"]
    html_skill = request.json["html"]
    uml_skill = request.json["uml"]
    ui_ux_skill = request.json["uiUx"]

    control_structures = request.json["controlStructures"]
    algorithms = request.json["algorithms"]
    quality = request.json["quality"]
    project_management = request.json["projectManagement"]
    problem_solving = request.json["problemSolving"]
    agile = request.json["agile"]
    oop = request.json["oop"]
    functional_programming = request.json["functionalProgramming"]
    software_engineering = request.json["softwareEngineering"]
    apis = request.json["apis"]

    register_student = Student(name, linkedin, image, summary, python_skill, react_skill, github_skill, json_skill, css_scss_skill, data_type_skill, sql_skill, javascript_skill, html_skill, uml_skill, ui_ux_skill, control_structures, algorithms, quality, project_management, problem_solving, agile, oop, functional_programming, software_engineering, apis)

    db.session.add(register_student)
    db.session.commit()
    return "Student Successfully Submitted"
  return ""

# get all students
@app.route("/students", methods=["GET"])
def return_students():
  all_students = Student.query.all()
  result = students_schema.dump(all_students)
  return jsonify(result.data)

# get one student
@app.route("/student/<id>", methods=["GET"])
def return_student(id):
  student = Student.query.get(id)
  return student_schema.jsonify(student)


if __name__ == "__main__":
  app.debug = True
  app.run()