from application import db


class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(10), nullable=False)
    age_range = db.Column(db.String(10), nullable=False)
    room_number = db.Column(db.String(2), nullable=False)


    teacher_assigned = db.Column(db.Integer, db.ForeignKey('staff.id'))
    teacher = db.relationship("Staff", backref='class')

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    email= db.Column(db.String(60), nullable=False)
    DBS_status = db.Column(db.String(15), nullable=False)
    
    
    class_assigned = db.relationship("Classes", backref='current_teacher')
 

