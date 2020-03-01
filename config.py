from flask import Flask
from flask_sqlalchemy import SQLAlchemy #pylint: disable=import-error
from flask_migrate import Migrate #pylint: disable=import-error

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dojos_ninjas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)