# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)

    grades = db.relationship("Grade", back_populates="student", cascade="all, delete-orphan")

    def average(self):
        if not self.grades:
            return None
        total = sum(g.score for g in self.grades)
        return round(total / len(self.grades), 2)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "roll_number": self.roll_number,
            "grades": {g.subject: g.score for g in self.grades},
            "average": self.average()
        }

class Grade(db.Model):
    __tablename__ = "grades"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Float, nullable=False)

    student = db.relationship("Student", back_populates="grades")

    __table_args__ = (
        db.UniqueConstraint('student_id', 'subject', name='uix_student_subject'),
    )
