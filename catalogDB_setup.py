import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Item(Base):
    __tablename__ = 'item'

    title = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    added_by = Column(String(80), nullable=False)
    created_at = Column(Date, default=datetime.utcnow, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)


# We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'added_by': self.added_by,
            'created_at': self.created_at,
        }


engine = create_engine('sqlite:///categoryitem.db')


Base.metadata.create_all(engine)