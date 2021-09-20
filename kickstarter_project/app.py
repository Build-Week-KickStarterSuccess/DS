from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import joblib

DB = SQLAlchemy()
APP = Flask(__name__)

APP.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

DB.init_app(APP)
# Set up the main route
@APP.route('/')
def main():
        return render_template('landing.html')
@APP.route('/about')
def about():
    return render_template('index.html')

if __name__ == '__main__':
        APP.run()