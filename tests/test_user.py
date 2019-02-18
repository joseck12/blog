import unittest
from app.models import User
from app import db

#the setup method creates an instances of our user
class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = 'joseck',password = 'qwerty', email = 'jogachi4@gmail.com')



    def save_user(self):
        db.session.add(self.new_user)
        db.session.commit()


    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)


    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password


    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('qwerty'))
