
from flask import Flask, render_template, redirect, url_for, abort, flash, request, current_app, make_response, session
from flask import *

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
  # name = 'None' form 後加 name=name
  form = NameForm()
  if form.validate_on_submit():
    name = form.name.data
    password = form.password.data
    session["name"] = name
    # form.name.data = ''
  return render_template('index.html', form=form)


@app.route('/account',methods=['POST','GET'])
def account():
  data = {
        "lang": "python",
        "note":"研發雲帳號管理",
        "account": "08771",
        "department": "IF-System",
        "member":["Stacy","Apple","Rosa","David","Peter"],
        "my_dict": {"city": "Taipei"},
        "my_list": [1, 2, 3, 4, 5],
        "my_int": 39
         }
  return render_template('account.html', **data)

import pandas as pd
csv_file = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
df = pd.read_csv(csv_file)

@app.route('/menu',methods=['POST','GET'])
def menu():
  """
  etl1s = ETL.query.all()
  if 'eid' in request.form:
      eid = request.form.get('eid' ,type=float)
      step1 = ETL.query.get(eid)
      return render_template("menu.html", etl1s=etl1s, step1=step1)
  """
  #  global eid
  eid = request.form.get('eid') 
  step1 = df[df['country'] == eid]
  # xxx = df.groupby(['country','continent']).size()
  return render_template('menu.html',tables=[step1.to_html(classes='data')], titles = ['Menu', 'Drop-down Menu'])

@app.route('/menu2',methods=['POST','GET'])
def menu2():
  df1 = df['country']
  EID = df1.unique()
  if 'eid' in request.form:
    eid = request.form.get('eid') 
    step2 = df[df['country'] == eid]
    return render_template('menu2.html',tables=[step2.to_html(classes='data')], titles = ['Menu', 'Drop-down Menu'], EID=EID)
  return render_template('menu2.html', EID=EID)



@app.route('/message',methods=['POST','GET'])
def message():
  df1 = df['country']
  EID = df1.unique()
  return render_template('message.html', EID=EID)


 # DB 寫法
"""
class ExamData(db.Model):
  tablename = 'ExamData'
  id = db.Column(db.Integer, primary_key=True)
  eid = db.Column(db.Integer)
  model_Name = db.Column(db.String(255))
  value_without = db.Column(db.Float)
  time = db.Column(db.Float)


@app.route('/', methods=['GET', 'POST'])
def all_persons():
    EID = db.session.query(ExamData.eid).distinct()  # 取得所有EID
    model_Name = db.session.query(ExamData.model_Name).distinct()  # 取得所有model_Name
    if 'eid' in request.form and 'model_Name' in request.form:
        result = ExamData.query.filter_by(eid=int(request.form.get("eid")), model_Name=request.form.get("model_Name"))
        return render_template("index.html", EID=EID, model_Name=model_Name, result=result)
    return render_template("index.html", EID=EID, model_Name=model_Name)


@app.before_first_request
def handle_before_first_request():
    # 在第一次請求處理之前被執行
    eid = request.form.get('eid',type=str)
    print("handle_before_first_request 被執行")
    print(eid)

@app.after_request
def handle_after_request(response):
    # 在每次請求(視圖函数处理)之后都被執行， 前提是視圖函数没有出现異常
    print("handle_after_request 被執行")
    eid = request.form.get('eid',type=str)
    print(eid)
    return response
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)


