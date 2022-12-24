import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# used th get the absolute path of this directory
basedir = os.path.abspath(os.path.dirname(__file__))
database_path = f"sqlite:///{os.path.join(basedir, 'database.db')}"

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    public_id = db.Column(db.Integer)
    date_created = db.Column(db.String)

    def __repre__(self):
        return f'<User {self.id} {self.first_name} {self.last_name}>'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    # def delete(self):
    #    db.session.delete(self)
    #    db.session.commit()

    def update(self):
        db.session.commit()