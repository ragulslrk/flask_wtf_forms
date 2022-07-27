import re
from flask import *
from flask_wtf import FlaskForm
from wtforms import  *
from wtforms.validators import *
app=Flask(__name__,template_folder='template')
app.config['SECRET_KEY']='this is  not a secret'

class forms(FlaskForm):
    name=StringField('Please Enter Your Name',validators=[DataRequired()])
    submit=SubmitField()

@app.route('/',methods=['GET','POST'])
def home():
    form=forms()
    if request.method =="POST":
        if  form.validate_on_submit():
            return redirect(url_for('dashboard',data=form.name.data))
        return render_template('form.html',form=form)
        
    else:
        return render_template('form.html',form=form)
    


#route for dashboard page
@app.route('/dashboard/<data>')
def dashboard(data):
    return render_template('dashboard.html',name=data)
if __name__== '__main__':
    app.run(debug=True)