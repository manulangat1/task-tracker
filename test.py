from datetime import datetime
from app import db
from app.models import User
from flask import current_app as app
import unittest

#user test class

class UserModelCase(unittest.TestCase):
    def setUp(self):
        # app = current_app()
        app.config["SQLALCHEMY_DATABASE_URI"] = postgresql:///tentest
        db.creat_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    def test_save_method(self):
        u = User(username="manu")
        u.set_password('cat')
        u.save()
        us = User.query.all()
        self.assertTrue(us.length > 0)
    def test_delete_method(self):
        u = User(username="manu")
        u.set_password('cat')
        u.save()
        us = User.query.all()
        us.delete()
        self.assertTrue(us.length < 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
