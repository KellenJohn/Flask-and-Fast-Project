from flask import Flask, render_template, redirect, url_for, abort, flash, request, current_app, make_response, session

from flask_sqlalchemy import get_debug_queries

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
  name = StringField('請輸入稱謂', validators = [DataRequired()])
  password = StringField('請輸入密碼', validators = [DataRequired()])
  submit = SubmitField('Submit')


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "dsa123a13s1ds"

@app.route('/',methods=['POST','GET'])
def index():
  name = 'None'
  form = NameForm()
  if form.validate_on_submit():
    name = form.name.data
    password = form.password.data
    session["name"] = name
    # form.name.data = ''
  return render_template('index.html', form=form, name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
