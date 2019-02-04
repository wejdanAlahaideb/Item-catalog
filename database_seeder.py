from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalogDB_setup import Base, Category, Item

engine = create_engine('sqlite:///categoryitem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#seed database with categories
FruiteCategory = Category(name="Fruit")
VageCategory = Category(name="Vegetable")
ProteinCategory = Category(name="Protein")
DairyCategory = Category(name="Dairy")
session.add(FruiteCategory)
session.add(VageCategory)
session.add(ProteinCategory)
session.add(DairyCategory)
session.commit()