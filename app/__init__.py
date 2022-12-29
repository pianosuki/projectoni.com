from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail
from flask_migrate import Migrate
from app.forms import ExtendedRegisterForm

app = Flask(__name__)

# Load the configuration from a separate file
app.config.from_pyfile("config.py")

# Initialize the database and Flask-Security
db = SQLAlchemy(app)

from app.models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, confirm_register_form=ExtendedRegisterForm)
mail = Mail(app)
migrate = Migrate(app, db)

# Import the routes and models modules to register them with the app
from app import views, models, admin
