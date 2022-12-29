from flask import Flask, flash, render_template, request, redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_security import current_user
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import User, Role

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