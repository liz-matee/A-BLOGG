from . import main
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/aboutme')
def about():
    return render_template('about.html')

@main.route('/end')
def end():
    return render_template('end.html')

class RegisterForm(Form):
    name = StringField('Name')
    username = StringField('username' )
    email = StringField('email')
    password = PasswordField('password',[ validators.DataRequired(),validators.EqualTo('confirm', message='passwords do not match')])
    confirm = PasswordField('confirm password')

@main.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html')
    return render_template('register.html', form=form)
