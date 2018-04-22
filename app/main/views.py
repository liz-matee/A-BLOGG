from . import main
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from wtforms import Form, striigfield, TextAreaField, PasswordField, validators
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
    name = striigfield('Name', [validators.Length(min=2, max=50)])
    username = striigfield('username' [validators.Length(min=4, max=26)])
    email = striigfield('email', [validators.Length(min=2, max=40)])
    password = PasswordField('password',[ validators.DataRequired(),validators.EqualTo('confirm', message='passwords do not match')])
    confirm = PasswordField('confirm password')

@main.route('/register', methords=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.methord == 'POST'an form.validate():
        render_template('regester.html')
    render_template('regester.html', form=form)
