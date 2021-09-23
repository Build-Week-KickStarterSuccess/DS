import kickstarter_project
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import numpy as np
from decouple import config
import pickle
import pdb

DB = SQLAlchemy()

#def create_app():
APP = Flask(__name__)

APP.config["SQLALCHEMY_DATABASE_URI"] = config('DATABASE_URI')
APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

DB.init_app(APP)
# Set up the main route
@APP.route('/')
def main():
        return render_template('landing.html')
@APP.route('/about')
def about():
        return render_template('index.html')

@APP.route('/predict/', methods=['GET','POST'])
def predict():

        if request.method == 'POST':
                # Get form data
                goal = request.form.get('goal')
                year = request.form.get('year')
                duration = request.form.get('duration')
                time_since_last_project = request.form.get('time_since_last_project')
                month = request.form.get('month')
                currency = request.form.get('currency')
                country = request.form.get('country')
                main_category = request.form.get('main_category')
                

                prediction = preprocessDataAndPredict(goal, year, duration, time_since_last_project, 
                                                      month, currency, country, main_category, )
                                                       

                return render_template('predict.html', prediction = prediction)

def preprocessDataAndPredict(goal, year, duration, time_since_last_project, month,
                             currency, country, main_category):

        test_data = [goal, year, duration, time_since_last_project, month,
                currency, country, main_category]

        print(test_data)

        test_data = np.array(test_data)

        test_data = test_data.reshape(1, -1)
        print(test_data)

        #file = open("model.pkl", "wb")
        model = pickle.load(open('model.pkl', 'rb'))

        prediction = model.predict(test_data)

        print(prediction)
        
        return prediction         



if __name__ == '__main__':
        APP.run()