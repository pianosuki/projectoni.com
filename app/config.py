import os
from dotenv import load_dotenv

load_dotenv()
# Set the debug mode
DEBUG = True

# Set the database configuration
SQLALCHEMY_DATABASE_URI = os.environ.get("DB_PATH")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Set the secret key and security password salt
SECRET_KEY = os.environ.get("SECRET_KEY")
SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT")

# Set the registration configuration
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_SEND_REGISTER_EMAIL = True
SECURITY_EMAIL_SUBJECT_REGISTER = "Project ONI Signup Confirmation"
SECURITY_POST_REGISTER_VIEW = "/register"

# Set the username configuration
SECURITY_USERNAME_ENABLE = True
SECURITY_USERNAME_REQUIRED = True
SECURITY_USERNAME_MIN_LENGTH = 1
SECURITY_USERNAME_MAX_LENGTH = 32
SECURITY_USERNAME_REQUIRED = True

# Set the email configuration
MAIL_SERVER = "127.0.0.1"
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_PORT = 1025
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_DEFAULT_SENDER = "gamemaster@projectoni.com"