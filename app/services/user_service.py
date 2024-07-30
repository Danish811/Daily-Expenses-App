from ..models import User
from .. import db

def create_user(data):
    user = User(email=data['email'], name=data['name'], mobile=data['mobile'])
    db.session.add(user)
    db.session.commit()
    return user

def get_user(user_id):
    return User.query.get(user_id)