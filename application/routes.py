from flask import render_template

from application import app, db
from application.forms import ClassForm, StaffForm
from application.models import Classes, Staff

@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home')

@app.route('/')
@app.route('/staff')
def staff_register():
    form = StaffForm()
    staffData = Staff(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            DBS_status = form.DBS_content.data
            )
    db.session.add(staffData)
    db.session.commit()

    return render_template('staff.html', title='Staff Register', form=form)

@app.route('/')
@app.route('/class')
def class_register():
    form = ClassForm()
    staffData = Classes(
            class_name = form.class_name.data,
            age_range = form.age_range.data,
            room_number = form.room_number.data,
            )
    db.session.add(ClassesData)
    db.session.commit()

    return render_template('class.html', title='Class Register', form=form)
