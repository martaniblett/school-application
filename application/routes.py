from flask import render_template

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

@app.route('/staff/update', methods=['GET', 'POST'])
def staff_update():
    form = StaffUpdateForm()
    update_staff=Staff.query.filter_by(name=last_name).first()
    if form.validate_on_submit():
         staffData = Staff(        
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            DBS_status = form.DBS_status.data
            )
         db.session.commit()
   
   return redirect(url_for('home'))
    
    
                 
    return render_template('staff.html', title='Staff Register', form=form)
         
@app.route('/staff/delete', methods=['GET', 'POST'])
def staff_delete():

    delete_staff=Staff.query.filter_by(name=last_name).first()
    
    db.session.delete(delete_staff)
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
