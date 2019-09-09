from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_sqlalchemy import SQLAlchemy
from model import *


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Thisisasecret!'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:admin@localhost/activity2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired()])
	password = PasswordField('password', validators=[InputRequired()])

class RegisterForm(FlaskForm):
	# username = StringField('Username', validators=[InputRequired()])
	name = StringField('Name', validators=[InputRequired()])
	email = StringField('Email Address', validators=[InputRequired()])
	password = PasswordField('Password', validators=[InputRequired()])
	conpass = PasswordField('Confirm Password', validators=[InputRequired()])


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	login = LoginForm()

	if login.validate_on_submit():
		user = InsertDatabase.query.filter_by(name=login.username.data).first()
		print(user)
		if user:
			if user.password == login.password.data:
				return '<h3>Welcome, {}! <br><br><h1>Welcome to BSIT 4-1 !'.format(login.username.data)
				# return render_template('home.html', login.username.data)
			else:
				return "Invalid username or password."

	return render_template('login.html', login=login)



@app.route('/register', methods=['GET', 'POST'])
def register():
	regi = RegisterForm()

	if regi.validate_on_submit():
		name = regi.name.data
		email = regi.email.data
		password = regi.password.data

		log = InsertDatabase(name=name, email=email, password=password)

		db.session.add(log)
		db.session.commit()
		return '<h3>{}, you have registered successfully. Click <a href="login">here</a> to login.'.format(regi.name.data)

	return render_template('register.html', register=regi)


if __name__ == '__main__':
	app.run(debug=True)



