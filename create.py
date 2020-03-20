from application import db
from application.models import Classes, Staff

db.drop_all()
db.create_all()

