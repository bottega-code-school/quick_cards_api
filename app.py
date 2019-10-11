from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy import DDL
from flask_heroku import Heroku
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://hrtqfdsschqwmg:490561b2f19d244b24c2b518c62e1398b9bea4f97382e384940bd46956f9901a@ec2-107-20-173-227.compute-1.amazonaws.com:5432/d6fn2vbghq644l"
heroku = Heroku(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)



class Student(db.Model):
  __tablename__ = "students"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  linkedin_url = db.Column(db.String(100))
  github_url = db.Column(db.String(100))
  image_url = db.Column(db.String())
  summary = db.Column(db.String())
  hired = db.Column(db.Boolean)
  cirr_positions = db.Column(db.PickleType)
  skills = db.Column(db.PickleType)

  def __init__(self, name, linkedin_url, github_url, image_url, summary, hired, cirr_positions, skills):
    self.name = name
    self.linkedin_url = linkedin_url
    self.github_url = github_url
    self.image_url = image_url
    self.summary = summary
    self.hired = hired
    self.cirr_positions = cirr_positions
    self.skills = skills

class StudentSchema(ma.Schema):
  class Meta:
    fields = ("id", "name", "linkedin_url", "github_url", "image_url", "summary", "hired", "cirr_positions", "skills")

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


@app.route("/")
def home():
  return "<h1>Bottega Quick Cards API</h1>"

# add student
@app.route("/student", methods=["POST"])
def add_student():
  if request.content_type == "application/json":
  
    name = request.json["name"]
    linkedin_url = request.json["linkedin_url"]
    github_url = request.json["github_url"]
    image_url = request.json["image_url"]
    summary = request.json["summary"]
    hired = request.json["hired"]
    cirr_positions = request.json["cirr_positions"]
    skills = request.json["skills"]

    register_student = Student(name, linkedin_url, github_url, image_url, summary, hired, cirr_positions, skills)

    db.session.add(register_student)
    db.session.commit()
    return "Student Successfully Submitted"
  return "POST failed"

# update student
@app.route("/student/<id>", methods=["PUT"])
def update_student(id):
  student = Student.query.get(id)

  student.name = request.json["name"]
  student.linkedin_url = request.json["linkedin_url"]
  student.github_url = request.json["github_url"]
  student.image_url = request.json["image_url"]
  student.summary = request.json["summary"]
  student.hired = request.json["hired"]
  student.cirr_positions = request.json["cirr_positions"]
  student.skills = request.json["skills"]
  
  db.session.commit()
  return student_schema.jsonify(student)


# get all students
@app.route("/students", methods=["GET"])
def return_students():
  all_students = Student.query.all()
  result = students_schema.dump(all_students)
  return jsonify(result)

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






#add all students (dev use only)
@app.route("/add-multiple-students", methods=["POST"])
def add_multiple_students():
  if request.content_type == "application/json":
    for student in request.json:
      print(student["name"])
  
      name = student["name"]
      linkedin_url = student["linkedin_url"]
      github_url = student["github_url"]
      image_url = student["image_url"]
      summary = student["summary"]
      hired = student["hired"]
      cirr_positions = student["cirr_positions"]
      skills = student["skills"]

      register_student = Student(name, linkedin_url, github_url, image_url, summary, hired, cirr_positions, skills)

      db.session.add(register_student)
      db.session.commit()
    return "All Students Successfully Submitted"
  return "POSTS failed"


if __name__ == "__main__":
  app.debug = True
  app.run()