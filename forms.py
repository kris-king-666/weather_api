from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField('Search by City', validators=[DataRequired('You must enter a city name')])
    submit = SubmitField('Search')
