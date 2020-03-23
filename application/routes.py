from flask import render_template, redirect, url_for, request

from application import app, db
from application.forms import ClassForm, ClassUpdateForm, StaffForm, StaffUpdateForm
from application.models import Classes, Staff

@app.route('/')
@app.route('/home')
def home():
    
    staffData = Staff.query.all()
    return render_template('home.html', title='Home', staff=staffData)

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


@app.route('/staff/update/<int:staff_id>', methods=['GET', 'POST'])
def staff_update(staff_id):
    form = StaffUpdateForm() 
    update_staff=Staff.query.filter_by(id=staff_id).first()
    if form.validate_on_submit():
                
        update_staff.first_name = form.first_name.data,
        update_staff.last_name = form.last_name.data,
        update_staff.email = form.email.data,
        update_staff.DBS_status = form.DBS_status.data
        

        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.first_name.data = update_staff.first_name
        form.last_name.data = update_staff.last_name
        form.email.data = update_staff.email
        form.DBS_status.data = update_staff.DBS_status

                     
    return render_template('staff.html', title='Staff Register', form=form)

        
@app.route('/staff/delete/<int:staff_id>', methods=['GET', 'POST'])
def staff_delete(staff_id):

    staff_delete=Staff.query.filter_by(id=staff_id).first()
    

    db.session.delete(staff_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/class', methods=['GET', 'POST'])
def class_register():
    form = ClassForm()
    if form.validate_on_submit():
        classData = Classes(
            class_name = form.class_name.data,
            age_range = form.age_range.data,
            room_number = form.room_number.data
            )
        db.session.add(classData)
        db.session.commit()

    return render_template('class.html', title='Class Register', form=form)

@app.route('/class/update', methods=['GET', 'POST'])
def class_update():
    form = ClassUpdateForm()
    if form.validate_on_submit():
        classData = Classes(
            class_name = form.class_name.data,
            age_range = form.age_range.data,
            room_number = form.room_number.data
            )
        db.session.commit()

    return render_template('class.html', title='Class Register', form=form)


@app.route('/class/delete', methods=['GET', 'POST'])
def class_delete():
    db.session.delete(classData)
    db.session.commit()

    return redirect(url_for('class'))
