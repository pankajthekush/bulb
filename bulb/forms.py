from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import URL

class LoadUrl(FlaskForm):
    content_url = StringField('url',validators=[URL(message='please enter a valid url')])
    submit = SubmitField('Go')