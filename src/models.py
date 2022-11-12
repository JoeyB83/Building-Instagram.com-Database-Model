import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    user_post = relationship("Post")
    user_to_follow = relationship("Following", back_populates="follow_to_user")
    user_favorites_post = relationship("Favorites", back_populates="favorites_post") 

    def serialize(self):
        return{
            "id" : self.id,
            "username" : self.username,
            "firstname" : self.firstname,
            "lastname" : self.lastname,
            "email" : self.email,
            "password" : self.password
        }

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_name = Column(String(250), nullable=False)
    post_description = Column(String(250), nullable=False)   

    def serialize(self):
        return{
            "id" : self.id,
            "user_id" : self.user_id,
            "post_name" : self.post_name,
            "post_description" : self.post_description,            
        }

class Following(Base):
    __tablename__ = 'follow'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    follow_id = Column(Integer, primary_key=True)
    follow_to_user = relationship("User", back_populates="user_to_folllow")   

    def serialize(self):
        return{
            "id" : self.id,
            "user_id" : self.user_id,
            "follow_id" : self.follow_id,                        
        }

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    favorites_post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    favorites_post = relationship("User", back_populates="user_favorites_post")   

    def serialize(self):
        return{
            "id" : self.id,
            "user_id" : self.user_id,
            "follow_id" : self.follow_id,                        
        }                                        





render_er(Base, 'diagram.png')        

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# try:
#     result = render_er(Base, 'diagram.png')
#     print("Success! Check the diagram.png file")
# except Exception as e:
#     print("There was a problem genering the diagram")
#     raise e