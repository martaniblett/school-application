from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,  BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


class StaffForm(FlaskForm):
    
    first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    email = StringField('Email',
        validators = [
            DataRequired(),
            Length(min=10, max=30)
        ]
    )
    DBS_status= StringField('DBS Status',
        validators = [
            DataRequired(),
            Length(min=2, max=10)
        ]
    )
    submit = SubmitField('Create new staff member')

class StaffUpdateForm(FlaskForm):        
        
    first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    email = StringField('Email',
        validators = [
            DataRequired(),
            Length(min=10, max=30)
        ]
    )
    DBS_status= StringField('DBS Status',
        validators = [
            DataRequired(),
            Length(min=2, max=10)
        ]
    )         
    submit = SubmitField('Update details')


class ClassForm(FlaskForm):
    
    class_name = StringField('Class Name',
        validators = [
            DataRequired(),
            Length(min=2, max=10)
        ]
    )
    age_range = StringField('Age Range',
        validators = [
            DataRequired(),
            Length(min=1, max=10)
        ]
    )
    room_number = StringField('Room',
        validators = [
            DataRequired(),
            Length(min=1, max=2)
        ]
    )
    
    submit = SubmitField('Create new class')

    
class ClassUpdateForm(FlaskForm):


    class_name = StringField('Class Name',
        validators = [
            DataRequired(),
            Length(min=2, max=10)
        ]
    )
    age_range = StringField('Age Range',
        validators = [
            DataRequired(),
            Length(min=1, max=10)
        ]
    )
    room_number = StringField('Room',
        validators = [
            DataRequired(),
            Length(min=1, max=2)
        ]
    )        
               
    submit = SubmitField('Update class details')
