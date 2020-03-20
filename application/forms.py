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
    DBS_status= StringField('DBS Status',
        validators = [
            DataRequired(),
            Length(min=2, max=10)
        ]
    )
    submit = SubmitField('Create new staff member')


class ClassForm(FlaskForm):
    
    class_name = StringField('Class Name',
        validators = [
            DataRequired(),
            Length(min=2, max=5)
        ]
    )
    age_range = StringField('Age',
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
