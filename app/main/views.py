from . import main
from flask import Flask, render_template,flash,redirect,url_for,session,logging
from flask_sqlalchemy import SQLAlchemy
from wtf forms import Form, striigfield, TextAreaField, PasswordField, validators
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
