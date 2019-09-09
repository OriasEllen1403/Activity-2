from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InsertDatabase(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), nullable=True)
	password = db.Column(db.String(60), nullable=True)

	def __repr__(self):
		return '<name %r>' % self.name