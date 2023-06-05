from flask import request, render_template, redirect, url_for, flash
import requests
from app import app, db
from app.blueprints.auth.forms import PokemonForm, LoginForm, SignUpForm
from app.models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/pokemon_search', methods=['GET', 'POST'])
@login_required
def pokemon_search():
    form = PokemonForm()
    if request.method == 'POST':
        pokemon = request.form.get('pokemon')
        
        def getPokemonInfo():
            base_url = 'https://pokeapi.co/'
            url = f'{base_url}api/v2/pokemon/{pokemon}'
            response = requests.get(url)
            if response.ok:
                data = response.json()
                front_shiny = data['sprites']['front_shiny']
                ability = data['abilities'][0]['ability']['name']
                hp_stat = data['stats'][0]['base_stat']
                attack_stat = data['stats'][1]['base_stat']
                defense_stat = data['stats'][2]['base_stat']
                
                return {
                    'name': pokemon,
                    'front_shiny': front_shiny,
                    'ability': ability,
                    'hp_stat': hp_stat,
                    'attack_stat': attack_stat,
                    'defense_stat': defense_stat
                }
            else:
                return "Pokemon not found"

        pokemon_info = getPokemonInfo()
        return render_template('pokemon_search.html', form=form, pokemon_info=pokemon_info)

    return render_template('pokemon_search.html', form=form)


# AUTHENTICATION
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        queried_user = User.query.filter(User.email == email).first()
        if queried_user and check_password_hash(queried_user.password, password):
            login_user(queried_user)
            flash(f"Welcome back {queried_user.first_name}!", 'success')
            return redirect(url_for('main.home'))
        else:
            error = 'Invalid email or password'
            return render_template('login.html', form=form, error=error)
    else:
        return render_template('login.html', form=form)
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        # This dats is coming from the signup form
        user_data = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'email': form.email.data.lower(),
            'password': form.password.data
        }

        # Create user instance
        new_user = User()

        # Set user_data to our User attributes
        new_user.from_dict(user_data)

        # save to database
        db.session.add(new_user)
        db.session.commit()

        flash(f'Thank your for signing up {user_data["first_name"]}', 'success')
        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out!', 'warning')
    return redirect(url_for('main.home'))