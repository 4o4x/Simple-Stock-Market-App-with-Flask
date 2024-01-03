from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask import current_app as app
from app.models.user import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.find_by_username(app.db, username)

        if user and User.check_password(user['password'], password):
            session['username'] = user['username']
            flash('You were successfully logged in')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        existing_user = User.find_by_username(app.db, username)

        if existing_user is None:
            new_user = User(app.db, username, User.hash_password(password))
            new_user.save_to_db()
            flash('Account created successfully')
            return redirect(url_for('auth.login'))
        else:
            flash('Username already exists', 'error')

    return render_template('register.html')

@auth.route('/logout')
def logout():
    session.pop('username', None)
    flash('You were logged out')
    return redirect(url_for('auth.login'))
