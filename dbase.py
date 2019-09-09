from flask import Flask
from model import *

DB_NAME = "postgres"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:admin@localhost/activity2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def create_tables():
	db.create_all()


if __name__=="__main__":
	# app.run()
	with app.app_context():
		create_tables()