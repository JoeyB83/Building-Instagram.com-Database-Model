import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
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
      

    def serialize(self):
        return{
            "id" : self.id,
            "user_id" : self.user_id,
            "post_name" : self.post_name,
            "post_description" : self.post_description,            
        }

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)    
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
      

    def serialize(self):
        return{  
            "id" : self.id,          
            "user_from_id" : self.user_from_id,
            "user_to_id" : self.user_to_id                        
        }

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))       

    def serialize(self):
        return{
            "id" : self.id,
            "comment_text" : self.comment_text,
            "author_id" : self.author_id                        
        }

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum, nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))       

    def serialize(self):
        return{
            "id" : self.id,
            "type" : self.type,
            "url" : self.url,
            "post_id": self.post_id                        
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