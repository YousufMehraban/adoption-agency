from flask import Flask, render_template, session, redirect
from model import db, Pet
from forms import AddPet, EditPet


app = Flask(__name__)

app.config['SECRET_KEY'] = 'NOTHING'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


db.app = app
db.init_app(app)

@app.route('/')
def show_all_pets():
    """Showing list of all the pets"""

    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def show_pet_form():
    """display a from to add a new pet"""

    form = AddPet()

    if form.validate_on_submit():
        name = form.name.data
        species = form.sepcies.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name = name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')

    else:
        return render_template('add_pet.html', form = form)

@app.route('/display/<int:pet_id>')
def show_pet_details(pet_id):
    """display details of a pet"""

    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)

@app.route('/edit/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet_info(pet_id):
    """display a form to edit a pet information"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPet(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect('/')

    else:
        return render_template('edit_pet.html', pet=pet, form=form)
