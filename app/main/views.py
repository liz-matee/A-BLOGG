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
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        cur = sqlalchemy.connection.cursor()

        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",(name, email, username, password))

        sqlalchemy.connection.commit()

        cur.close()

        flash('registered successfully','success')

        redirect(url_for('register.html'))
    return render_template('register.html', form=form)

# @main.route('/')
# def index():
#     return '<h1> Hello World </h1>'
