from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://adwbwtpnxuanga:d4ad61ad0a8d340b3bb2c668ff0ca24732a0f35218bc03287cb7a3ba00a17d5d@ec2-23-21-115-109.compute-1.amazonaws.com:5432/d8kblmf4rj7tjj"
heroku = Heroku(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Student(db.Model):
  __tablename__ = "students"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  linkedin = db.Column(db.String(100), unique=True)
  github = db.Column(db.String(100), unique=True)
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
  hired = db.Column(db.Boolean)

  def __init__(self, name, linkedin, github, image, summary, python_skill, react_skill, github_skill, json_skill, css_scss_skill, data_type_skill, sql_skill, javascript_skill, html_skill, uml_skill, ui_ux_skill, control_structures, algorithms, quality, project_management, problem_solving, agile, oop, functional_programming, software_engineering, apis, hired):
    self.name = name
    self.linkedin = linkedin
    self.github = github
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
    self.hired = hired

class StudentSchema(ma.Schema):
  class Meta:
    fields = ("id", "name", "linkedin", "github", "image", "summary", "python_skill", "react_skill", "github_skill", "json_skill", "css_scss_skill", "data_type_skill", "sql_skill", "javascript_skill", "html_skill", "uml_skill", "ui_ux_skill", "control_structures", "algorithms", "quality", "project_management", "problem_solving", "agile", "oop", "functional_programming", "software_engineering", "apis", "hired")

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


@app.route("/")
def home():
  return "<h1>Bottega Quick Cards API</h1>"

# add student
@app.route("/add-student", methods=["POST"])
def add_student():
  if request.content_type == "application/json":
  
    name = request.json["name"]
    linkedin = request.json["linkedin"]
    github = request.json["github"]
    image = request.json["image"]
    summary = request.json["summary"]
    python_skill = request.json["python_skill"]
    react_skill = request.json["react_skill"]
    github_skill = request.json["github_skill"]
    json_skill = request.json["json_skill"]
    css_scss_skill = request.json["css_scss_skill"]
    data_type_skill = request.json["data_type_skill"]
    sql_skill = request.json["sql_skill"]
    javascript_skill = request.json["javascript_skill"]
    html_skill = request.json["html_skill"]
    uml_skill = request.json["uml_skill"]
    ui_ux_skill = request.json["ui_ux_skill"]

    control_structures = request.json["control_structures"]
    algorithms = request.json["algorithms"]
    quality = request.json["quality"]
    project_management = request.json["project_management"]
    problem_solving = request.json["problem_solving"]
    agile = request.json["agile"]
    oop = request.json["oop"]
    functional_programming = request.json["functional_programming"]
    software_engineering = request.json["software_engineering"]
    apis = request.json["apis"]
    hired = request.json["hired"]

    register_student = Student(name, linkedin, github, image, summary, python_skill, react_skill, github_skill, json_skill, css_scss_skill, data_type_skill, sql_skill, javascript_skill, html_skill, uml_skill, ui_ux_skill, control_structures, algorithms, quality, project_management, problem_solving, agile, oop, functional_programming, software_engineering, apis, hired)

    db.session.add(register_student)
    db.session.commit()
    return "Student Successfully Submitted"
  return "POST failed"

# update student
@app.route("/student/<id>", methods=["PUT"])
def update_student(id):
  student = Student.query.get(id)

  student.name = request.json["name"]
  student.linkedin = request.json["linkedin"]
  student.github = request.json["github"]
  student.image = request.json["image"]
  student.summary = request.json["summary"]
  student.python_skill = request.json["python_skill"]
  student.react_skill = request.json["react_skill"]
  student.github_skill = request.json["github_skill"]
  student.json_skill = request.json["json_skill"]
  student.css_scss_skill = request.json["css_scss_skill"]
  student.data_type_skill = request.json["data_type_skill"]
  student.sql_skill = request.json["sql_skill"]
  student.javascript_skill = request.json["javascript_skill"]
  student.html_skill = request.json["html_skill"]
  student.uml_skill = request.json["uml_skill"]
  student.ui_ux_skill = request.json["ui_ux_skill"]

  student.control_structures = request.json["control_structures"]
  student.algorithms = request.json["algorithms"]
  student.quality = request.json["quality"]
  student.project_management = request.json["project_management"]
  student.problem_solving = request.json["problem_solving"]
  student.agile = request.json["agile"]
  student.oop = request.json["oop"]
  student.functional_programming = request.json["functional_programming"]
  student.software_engineering = request.json["software_engineering"]
  student.apis = request.json["apis"]
  student.hired = request.json["hired"]
  
  db.session.commit()
  return student_schema.jsonify(student)


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

# delete student
@app.route("/student/<id>", methods=["DELETE"])
def delete_student(id):
  student = Student.query.get(id)
  db.session.delete(student)
  db.session.commit()

  return jsonify("Student Deleted")


if __name__ == "__main__":
  app.debug = True
  app.run()