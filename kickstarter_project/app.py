import kickstarter_project
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import numpy as np
from decouple import config
#import joblib

DB = SQLAlchemy()

def create_app():
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
                return render_template('index.html')\

        return APP

if __name__ == '__main__':
    APP.run()
'''
        @APP.route('/predict/', methods=['GET','POST'])
        def predict():

                if request.method == 'POST':
                        # Get form data
                        goal = request.form.get()
                        month = request.form.get()
                        year = request.form.get()
                        duration = request.form.get()
                        currency = request.form.get()
                        country = request.form.get()
                        main_category = request.form.get()
                        time_since_last_project = request.form.get()

                        try:
                                prediction = preprocessDataAndPredict()

                                return render_template('prediction.html', prediction = prediction)
                        except ValueError:
                                return "Please Enter valid values"
                pass
        pass

        def preprocessDataAndPredict():

                test_data = []

                print(test_data)

                test_data = np.array(test_data)

                test_data = test_data.reshape(1, -1)
                print(test_data)

                file = open("kickstarter_project/model.pckl", "rb")
                model = joblib.load(file)

                prediction = model.predict(test_data)

                print(prediction)
                return prediction

        pass
'''