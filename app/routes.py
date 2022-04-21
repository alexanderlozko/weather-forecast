from flask import render_template, redirect, request, flash, url_for, session, send_file
from app import app

from werkzeug.utils import secure_filename
from app.forms import ForecastForm

import os
import pickle
import pandas as pd

filename = 'app/model/finalized_model.sav'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/forecast_manually', methods=["GET", "POST"])
def forecast_manually():
    form = ForecastForm(request.form)
    if request.method == "POST":
        Location = form.Location.data
        MinTemp = form.MinTemp.data
        MaxTemp = form.MaxTemp.data
        Rainfall = form.Rainfall.data
        Evaporation = form.Evaporation.data
        Sunshine = form.Sunshine.data
        WindGustDir = form.WindGustDir.data
        WindGustSpeed = form.WindGustSpeed.data
        WindDir9am = form.WindDir9am.data
        WindDir3pm = form.WindDir3pm.data
        WindSpeed9am = form.WindSpeed9am.data
        WindSpeed3pm = form.WindSpeed3pm.data
        Humidity9am = form.Humidity9am.data
        Humidity3pm = form.Humidity3pm.data
        Pressure9am = form.Pressure9am.data
        Pressure3pm = form.Pressure3pm.data
        Cloud9am = form.Cloud9am.data
        Cloud3pm = form.Cloud3pm.data
        Temp9am = form.Temp9am.data
        Temp3pm = form.Temp3pm.data
        RainToday = form.RainToday.data
        year = form.year.data
        month_sin = form.month_sin.data
        month_cos = form.month_cos.data
        day_sin = form.day_sin.data
        day_cos = form.day_cos.data

        data = pd.DataFrame(data={'Location':Location, 'MinTemp':MinTemp, 'MaxTemp':MaxTemp, 'Rainfall':Rainfall,
                                    'Evaporation':Evaporation, 'Sunshine':Sunshine, 'WindGustDir':WindGustDir,
                                    'WindGustSpeed':WindGustSpeed, 'WindDir9am':WindDir9am, 'WindDir3pm':WindDir3pm,
                                    'WindSpeed9am':WindSpeed9am, 'WindSpeed3pm':WindSpeed3pm, 'Humidity9am':Humidity9am,
                                    'Humidity3pm':Humidity3pm, 'Pressure9am':Pressure9am, 'Pressure3pm':Pressure3pm,
                                    'Cloud9am':Cloud9am, 'Cloud3pm':Cloud3pm, 'Temp9am':Temp9am, 'Temp3pm':Temp3pm,
                                    'RainToday':RainToday, 'year':year, 'month_sin':month_sin, 'month_cos':month_cos,
                                    'day_sin':day_sin, 'day_cos':day_cos}, index=[0])
        columns = data.columns
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict(data)
        if result:
            return render_template('result.html', data=data, columns=columns,  result=result)
    return render_template('forecast_manually.html', form=form)



@app.route('/forecast_csv', methods=['GET', 'POST'])
def forecast_csv():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save('app/data/' + filename)
        data = pd.read_csv('app/data/' + filename, header=None)
        d = data[1]
        data = pd.DataFrame(columns=list(data[0]), index=[0])
        data.iloc[0] = d[1]
        columns = data.columns
        loaded_model = pickle.load(open('app/model/finalized_model.sav', 'rb'))
        result = loaded_model.predict(data)
        return render_template('result.html', data=data, columns=columns, result=result)
    return render_template('forecast_csv.html')

