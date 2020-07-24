
登入界面
```html
# 陽春
<form method="post" action="/login">
    <label for="user_id">user_id:</label>
      <input type="text" id="user_id" name="user_id">
    <label for="password">password:</label>
      <input type="password" id="password" name="password">
      <button type="submit">登入</button>
</form>

# 進階
<form method="post" action="/login">

  <div class="form-group row">
    <label for="user_id" class="col-2 offset-1 col-form-label">user_id:</label>
    <div class="col-3">
      <input type="text" class="form-control" id="user_id" name="user_id" placeholder="user_id">
      <small class="form-text">提示： Me</small>
    </div>
  </div>
  
  <div class="form-group row">
    <label for="password" class="col-2 offset-1 col-form-label">password:</label>
    <div class="col-3">
      <input type="password" class="form-control" id="password" name="password" placeholder="password">
      <small class="form-text">提示： myself</small>
    </div>
  </div>
  
  <div class="form-group row">
    <div class="col-2 offset-3">
      <button type="submit" class="btn btn-dirty-purple">登入</button>
    </div>
  </div>
  
</form>
```

Register.html
```html
<!-- 首頁 -->

<div>
  </button>
  <a class="navbar-brand" href="{{ url_for('index') }}">Flask App</a>
</div>

<!-- Collect the nav links, forms, and other content for toggling -->
<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
  <ul class="nav navbar-nav">
    <li class="{% if request.endpoint == 'index'}"}active{% endif %}>
      <a href="{{ url_for('index') }}">Home</a>
    </li>
  </ul>
  <ul class="nav navbar-nav navbar-right">
    <li class="{% if request.endpoint == 'register' %}active{% endif %}">
      <a href="{{ url_for('register')}}">Register</a>
    </li>
  </ul>
</div> <!-- /.navbar-collapse -->

<!-- 登錄網頁 Register.html-->
{% extends 'base.html' %}

{% block app_content %}
  <h1>Register Now</h1>
  <br>
  <div class="row">
    <div class="col-md-6">
      { import 'bootstrap/wtf.html' as wtf %}
      {{ wtf.quick_form(form) }}
    </div>    
  </div>
{% endblock %}

```

表單
```python
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    
    username = StringField('Username', validators = [DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=8, max=20)])
    confirm = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')
    # 驗證
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already token, please choose another one.')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()        
        if user:
            raise ValidationError('Email already token, please choose another one.')
        
```
路由
```python
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Congrats, registeration success', category='success')
        return redirect(url_for('index'))
    retunn render_template('register.html', form=form)    
```

models.py
```python
from flask login import UserMixin
from app import db, login

@login.user_loader
def load_user(id):
    return User.get(id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username
```    
base.html
```html
{% endblock %}

{% block nvbar %}
  {% inculde 'nvbar.html' %}
{% endblock %}

{% block content %}
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        {% with messages = get_flashed_messages(with_categories=True) %}
          {% if messages %}
            {% for category, message in messages %}
              <div class="alert alert-{{ category }}">
                  {{ messages }}
              </div>
            {% endfor %}
          {% endif %}
        {% endwith}
      </div>
    </div>
    {% block app_content %}
    {% endblock %}
  </div>
{% endblock %}

```

```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from config import Config
form forms import RegisterForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/register')
    form = RegisterForm()
    return render_template('register.html', form = form)
    

```
Config.py
```python
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12345678'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite://' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
```
