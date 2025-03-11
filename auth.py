from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user
from database import db
from models import User
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cur = db.connection.cursor()
        cur.execute("SELECT id, username, password FROM admins WHERE username=%s", (username,))
        user_data = cur.fetchone()
        cur.close()

        if user_data and check_password_hash(user_data[2], password):
            user = User(user_data[0], user_data[1], user_data[2])
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        
        flash("Invalid credentials!", "danger")
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
