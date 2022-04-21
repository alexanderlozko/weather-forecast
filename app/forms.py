from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms import validators
from wtforms.validators import DataRequired

class ForecastForm(FlaskForm):
    Location = StringField('Location')
    MinTemp = StringField('MinTemp')
    MaxTemp = StringField('MaxTemp')
    Rainfall = StringField('Rainfall')
    Evaporation = StringField('Evaporation')
    Sunshine = StringField('Sunshine')
    WindGustDir = StringField('WindGustDir')
    WindGustSpeed = StringField('WindGustSpeed')
    WindDir9am = StringField('WindDir9am')
    WindDir3pm = StringField('WindDir3pm')
    WindSpeed9am = StringField('WindSpeed9am')
    WindSpeed3pm = StringField('WindSpeed3pm')
    Humidity9am = StringField('Humidity9am')
    Humidity3pm = StringField('Humidity3pm')
    Pressure9am = StringField('Pressure9am')
    Pressure3pm = StringField('Pressure3pm')
    Cloud9am = StringField('Cloud9am')
    Cloud3pm = StringField('Cloud3pm')
    Temp9am = StringField('Temp9am')
    Temp3pm = StringField('Temp3pm')
    RainToday = StringField('RainToday')
    year = StringField('year')
    month_sin = StringField('month_sin')
    month_cos = StringField('month_cos')
    day_sin = StringField('day_sin')
    day_cos = StringField('day_cos')

