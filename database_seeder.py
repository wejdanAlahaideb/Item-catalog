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

FruiteItem = Item(title="Strawberry", description="The garden strawberry is a widely grown hybrid species of the genus Fragaria.", added_by="Admin")
VageItem = Item(title="Broccoli", description="Broccoli is an edible green plant in the cabbage family whose large flowering head is eaten as a vegetable.", added_by="Admin")
ProtenItem = Item(title="Chicken breast", description="Boneless chicken breasts continue to balloon in size, from what was a standard 5 to 6 ounces each to nearly 8 ounces.", added_by="Admin")
session.add(FruiteItem)
session.add(VageItem)
session.add(ProtenItem)
session.commit()