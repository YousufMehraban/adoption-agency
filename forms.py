
from lib2to3.pgen2.token import OP
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange



class AddPet(FlaskForm):
    """add a new pet"""

    name = StringField('Pet Name')
    sepcies = StringField('Species', validators=[AnyOf(values=['cat', 'dog', 'porcupine'])])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Add Note')



class EditPet(FlaskForm):
    """creating a form to edit a pet information"""

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = StringField('Add Note')
    available = BooleanField('Availability')
    