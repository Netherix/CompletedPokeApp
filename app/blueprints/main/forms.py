from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, IntegerField
from wtforms.validators import DataRequired

class PokemonForm(FlaskForm):
    pokemon = StringField('Pokemon', validators=[DataRequired()])
    submit = SubmitField('Submit')
    poke_name = HiddenField('poke_name', validators=[DataRequired()])
    img_url = HiddenField('Image URL', validators=[DataRequired()])
    ability = HiddenField('Ability', validators=[DataRequired()])
    hp = HiddenField('HP', validators=[DataRequired()])
    attack = HiddenField('Attack', validators=[DataRequired()])
    defense = HiddenField('Defense', validators=[DataRequired()])

class CapturePokemon(FlaskForm):
    poke_name = HiddenField('Pokemon Name', validators=[DataRequired()])
    img_url = HiddenField('Image URL', validators=[DataRequired()])
    ability = HiddenField('Ability', validators=[DataRequired()])
    hp = HiddenField('HP', validators=[DataRequired()])
    attack = HiddenField('Attack', validators=[DataRequired()])
    defense = HiddenField('Defense', validators=[DataRequired()])
    user_id = IntegerField('User ID')


