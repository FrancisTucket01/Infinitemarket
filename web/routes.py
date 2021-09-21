from web import app, login_manager
from flask_login import login_user, logout_user, login_required
from flask import render_template, flash, url_for, redirect
from web.models import Item, User
from web import db
from werkzeug.security import check_password_hash, generate_password_hash
from web.forms import RegisterForm, LoginForm
from functools import wraps
from flask import Flask, session

@app.route('/home')
@app.route('/')
def home():

    return render_template("home.html")


@app.route('/market')
def market():
    
    items =  Item.query.all()

    return render_template("market.html", items=items)


@app.route("/login" , methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        correct_password_hash = User.query.filter_by(username=form.username.data).first()
        
        if attempted_user and check_password_hash(correct_password_hash.password_hash, form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('home'))
        else:
            flash('The username and password provided do not mach!!! Please try again.', category='danger')

    return render_template('login.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('market'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have Successfuly Loged out!", category='info')
    return redirect(url_for("home"))


@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route("/admin")
def admin():
    items =  Item.query.all()
    return render_template("admin.html", items=items)