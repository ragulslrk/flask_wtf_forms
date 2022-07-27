from flask import *
from flask_wtf import FlaskForm
from wtforms import  *
from wtforms.validators import *
app=Flask(__name__,template_folder='template')
app.config['SECRET_KEY']='this is  not a secret'

class forms(FlaskForm):
    name=StringField('Please Enter Your Name',validators=[DataRequired()])
    submit=SubmitField()

@app.route('/')
def home():
    return

if __name__== '__main__':
    app.run()