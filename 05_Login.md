
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

```python
class RegisterForm(FlaskForm):
    
    username = StringField('Username', validators = [DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=8, max=20))
    confirm = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')
    
    def validate_username
```
