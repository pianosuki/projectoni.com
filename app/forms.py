from flask_security.forms import ConfirmRegisterForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ExtendedRegisterForm(ConfirmRegisterForm):
    pass
