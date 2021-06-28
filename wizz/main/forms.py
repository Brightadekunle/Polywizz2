from flask import request
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField
from flask_wtf.file import FileAllowed, FileField


class UploadForm(FlaskForm):
    profile_picture = FileField('Upload picture', validators=[
        FileAllowed(['jpg', 'png', 'pdf'])])

    submit = SubmitField('Submit')

