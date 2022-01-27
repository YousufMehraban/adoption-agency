from model import db, Pet
from app import app


db.drop_all()
db.create_all()


    
cat = Pet(name='Lagy Blue', species='cat', photo_url='/static/cat.jpeg', age=5, notes='He is so lovely', available=True)
dog = Pet(name='Maxi Rock', species='dog', photo_url='/static/dog.jpeg', age=7, notes='He is so caring', available=True)
goat = Pet(name='Grass Boy', species='goat', photo_url='/static/goat.jpeg', age=2, notes='He is so naughty', available=True)
squirrel = Pet(name='Squirrel', species='squirrel', photo_url='/static/squirrel.jpeg', age=5, notes='He is not good', available=True)


db.session.add_all([cat, dog, goat, squirrel])
db.session.commit()
