from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:123456@localhost/first_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db =SQLAlchemy(app)
errors =""
def validation_preprocessor(data, *args, **kwargs):
    # validate data by any of your cool-validation-frameworks
    if errors:
        raise ProcessingException(description='Something went wrong', code=400)

class Upsinfo(db.Model):
    #__tablename__ = 'example'
    id =db.Column('id',db.Integer,primary_key=True)
    name = db.Column('name',db.Unicode)
    ip = db.Column('ip',db.Unicode)
    port = db.Column('port',db.Unicode)
    community = db.Column('community',db.Unicode)
    version = db.Column('version',db.Unicode)
class Displaystatus(db.Model):
    id =db.Column('id',db.Integer,primary_key=True)
    probetime =db.Column('probetime',db.Time)
    probetime =db.Column('probetime',db.Time)
    outletstatus =db.Column('outletstatus',db.Integer)
    batteryconsumption =db.Column('batteryconsumption',db.Integer)
    remainingtime =db.Column('remainingtime',db.Time)
class emonpi(db.Model):
    id =db.Column('id',db.Integer,primary_key=True)
    name =db.Column('name',db.Unicode)
    address =db.Column('address',db.Unicode)

db.create_all() 
manager = APIManager(app, flask_sqlalchemy_db =db)
manager.create_api(Upsinfo,methods=['GET','POST','DELETE','PUT'],preprocessors=dict(POST=[validation_preprocessor]))
manager.create_api(Displaystatus,methods=['GET','POST','DELETE','PUT'])
manager.create_api(emonpi,methods=['GET','POST','DELETE','PUT'],preprocessors=dict(POST=[validation_preprocessor]))
if __name__ == "__main__":
      app.run(debug=True)
