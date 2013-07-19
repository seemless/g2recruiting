__author__ = 'matthew smith'

from wtforms import Form, BooleanField, TextField, FileField, validators


class RegistrationForm(Form):
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    resume = FileField("Upload your resume",
        validators=[])
    #accept_tos = BooleanField('I accept the TOS', [validators.Required()])

    allowed_extensions = ['doc','docx','pdf','txt','rtf','odf','ods']

    def hidden_tag(self):
        return ''