
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
表單
```python
class RegisterForm(FlaskForm):
    
    username = StringField('Username', validators = [DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=8, max=20))
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
