from flask import render_template

from application import app, db
from application.forms import ClassForm, StaffForm
from application.models import Classes, Staff

@app.route('/')
@app.route('/home')
def home(): 
    return render_template('home.html', title='Home')

@app.route('/staff', methods=['GET', 'POST'])
def staff_register():
    form = StaffForm()
    if form.validate_on_submit():
        staffData = Staff(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            DBS_status = form.DBS_status.data
            )
        db.session.add(staffData)
        db.session.commit()

    return render_template('staff.html', title='Staff Register', form=form)


@app.route('/class', methods=['GET', 'POST'])
def class_register():
    form = ClassForm()
    if form.validate_on_submit():
        classData = Classes(
            class_name = form.class_name.data,
            age_range = form.age_range.data,
            room_number = form.room_number.data,
            )
        db.session.add(classData)
        db.session.commit()

    return render_template('class.html', title='Class Register', form=form)
