from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    poke = db.relationship('Poke', backref='author', lazy='dynamic')

    # hashes our password when user signs up
    def hash_password(self, signup_password):
        return generate_password_hash(signup_password)
    
    # This method will assign our columns with their respective values
    def from_dict(self, user_data):
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.email = user_data['email']
        self.password = self.hash_password(user_data['password'])


class Poke(db.Model):
    poke_name = db.Column(db.String, primary_key=True)
    img_url = db.Column(db.String, nullable=False)
    ability = db.Column(db.String, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    # FK
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    # This method will assign our columns with their respective values
    def from_dict(self, poke_data):
        print('poke data here')
        print(poke_data) 
        self.poke_name = poke_data['poke_name']
        self.img_url = poke_data['img_url']
        self.ability = poke_data['ability']
        self.hp = poke_data['hp']
        self.attack = poke_data['attack']
        self.defense = poke_data['defense']
        self.user_id = int(poke_data['user_id'])

# only need the model


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

