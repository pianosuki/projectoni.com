import secret_config
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, login_required, UserMixin, RoleMixin, current_user
from flask_security.utils import hash_password
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from flask_security.forms import ConfirmRegisterForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

### App Configuration
app.config["DEBUG"] = True

### Database
app.config["SQLALCHEMY_DATABASE_URI"] = secret_config.DB_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

### Security
app.config["SECRET_KEY"] = secret_config.SECRET_KEY
app.config["SECURITY_PASSWORD_SALT"] = secret_config.SECURITY_PASSWORD_SALT

### Registration
app.config["SECURITY_REGISTERABLE"] = True
app.config["SECURITY_CONFIRMABLE"] = True
app.config["SECURITY_SEND_REGISTER_EMAIL"] = True
app.config["SECURITY_EMAIL_SUBJECT_REGISTER"] = "Project ONI Signup Confirmation"
app.config["SECURITY_POST_REGISTER_VIEW"] = "/register"

### Username
app.config['SECURITY_USERNAME_ENABLE'] = True
app.config['SECURITY_USERNAME_REQUIRED'] = True
app.config['SECURITY_USERNAME_MIN_LENGTH'] = 1
app.config['SECURITY_USERNAME_MAX_LENGTH'] = 32
app.config['SECURITY_USERNAME_REQUIRED'] = True

### Mail
app.config["MAIL_SERVER"] = "127.0.0.1"
app.config["MAIL_USERNAME"] = secret_config.MAIL_USERNAME
app.config["MAIL_PASSWORD"] = secret_config.MAIL_PASSWORD
app.config["MAIL_PORT"] = 1025
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_DEFAULT_SENDER"] = "gamemaster@projectoni.com"

db = SQLAlchemy(app)
bcrypt = Bcrypt()
mail = Mail(app)

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True)

    def __repr__(self):
        return self.name

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True)
    username = db.Column(db.String(32), unique = True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship('Role', secondary = roles_users, backref = db.backref('users', lazy = 'dynamic'))

    def __repr__(self):
        return self.username

class ExtendedRegisterForm(ConfirmRegisterForm):
    username = StringField("Username", [DataRequired()])

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, confirm_register_form = ExtendedRegisterForm)

class UserView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated)
    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for('security.login'))

class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next = request.url))

class AdminView(AdminMixin, ModelView):
    pass

class HomeAdminView(AdminMixin, AdminIndexView):
    pass

admin = Admin(app, index_view = HomeAdminView())
admin.add_view(AdminView(User, db.session))

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
