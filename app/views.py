from flask import render_template, redirect, url_for
from app import app
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user

@app.route("/")
def index():
    return render_template("index.html")

class UserView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated)
    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for('security.login'))