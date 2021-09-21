from flask import Flask
from flask_login import LoginManager
from .config import DevConfig
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(DevConfig)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
secret_key = "5accdb11b2c10a78d7c92c5fa102e"
app.config['SECRET_KEY'] = secret_key
from web import routes