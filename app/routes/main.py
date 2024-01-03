from flask import Blueprint, render_template, session, redirect, url_for
import app.utils as utils
from app.models.user import User
from flask import current_app as app



main = Blueprint('main', __name__)

@main.route('/')
def home():
    if 'username' not in session:
        # Eğer kullanıcı giriş yapmamışsa, giriş sayfasına yönlendir
        return redirect(url_for('auth.login'))
    
    existing_user = User.find_by_username2(app.db, session['username'])

    if existing_user is None:
        session.pop('username', None)
        return redirect(url_for('auth.login'))
    
    stock_dict = utils.get_stock_info_dict(existing_user.get_stocks())


    # Kullanıcı giriş yapmışsa ana sayfayı göster
    return render_template('home.html', username=existing_user.username, stocks=stock_dict)



#Bütün hisseleri gösterir.
#Kullanıcı bu hisseleri seçip portföyüne ekleyebilir.
@main.route('/stock_list')
def stock_list():
    if 'username' not in session:
        # Eğer kullanıcı giriş yapmamışsa, giriş sayfasına yönlendir
        return redirect(url_for('auth.login'))
    
    existing_user = User.find_by_username2(app.db, session['username'])

    if existing_user is None:
        session.pop('username', None)
        return redirect(url_for('auth.login'))
    
    all_stock= utils.get_stock_list()
    user_stock = existing_user.get_stocks()

    return render_template('stock_list.html', stocks=all_stock, user_stocks=user_stock)

#Kullanıcının portföyüne hisse eklemesini sağlar.
@main.route('/add_stock/<stock>')
def add_stock(stock):
    if 'username' not in session:
        # Eğer kullanıcı giriş yapmamışsa, giriş sayfasına yönlendir
        return redirect(url_for('auth.login'))
    
    existing_user = User.find_by_username2(app.db, session['username'])

    if existing_user is None:
        session.pop('username', None)
        return redirect(url_for('auth.login'))
    
    existing_user.add_stock(stock)

    return redirect(url_for('main.stock_list'))

#Kullanıcının portföyünden hisse silmesini sağlar.
@main.route('/remove_stock/<stock>')
def remove_stock(stock):
    if 'username' not in session:
        # Eğer kullanıcı giriş yapmamışsa, giriş sayfasına yönlendir
        return redirect(url_for('auth.login'))
    
    existing_user = User.find_by_username2(app.db, session['username'])

    if existing_user is None:
        session.pop('username', None)
        return redirect(url_for('auth.login'))
    
    existing_user.remove_stock(stock)

    return redirect(url_for('main.stock_list'))
