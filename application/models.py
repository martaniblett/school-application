from application import db
from datetime import datetime

class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(10), nullable=False)
    age_range = db.Column(db.String(10), nullable=False)
    room_number = db.Column(db.Integer, nullable=False)
   
   #class_teacher = db.relationship('Staff', backref='teacher class', lazy=True)
    

    def __repr__(self):
        return ''.join([
            'Class: ', self.form_name, ' ', self.age_range, '\r\n',
            'Classroom: ', self.room_number
        ])

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    email= db.Column(db.String(60), nullable=False)
    DBS_status = db.Column(db.String(5), nullable=False)
    #teacher_class = db.relationship('Classes', backref='class teacher', lazy=True)

    def __repr__(self):
        return ''.join([
            'Name: ', self.first_name, ' ', self.last_name, '\r\n',
            ])
