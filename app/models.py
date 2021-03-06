from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog',backref = 'user',lazy = "dynamic")
    comment = db.relationship('Comment',backref = 'user',lazy = "dynamic")



    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')


    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__='blogs'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    category = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment = db.relationship('Comment',backref = 'blogs',lazy = "dynamic")
    email = db.Column(db.String(255),unique = True,index = True)


    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls,id):
        blogs = Blog.query.all()
        return blogs

    def delete_blog(self):
        db.session.query(Blog).delete()
        db.session.commit()

    def __repr__(self):
        return f'User {self.name}'



class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.all()
        return comments

    def __repr__(self):
        return f'User {self.name}'

class Quote:
   '''
   Quote class to define Quote Objects
   '''

   def __init__(self,count,recipes,publisher):
       self.count =count
       self.recipes = recipes
       self.publisher = publisher
       SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'
       ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
       API_KEY= os.environ.get('API_KEY')
       SECRET_KEY = os.environ.get('SECRET_KEY')

class Subscriber(UserMixin, db.Model):
    __tablename__="subscribers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)


    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_subscribers(cls,id):
        return Subscriber.query.all()


    def __repr__(self):
        return f'User {self.email}'
