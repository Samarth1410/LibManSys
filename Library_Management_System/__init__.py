"""
The flask application package.
"""

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdnfl' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(path.abspath(path.dirname(__file__)), 'data.sqlite')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)
