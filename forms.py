from wtforms import Form, TextAreaField, SelectField, validators
from mox.constants import codes, methods, content_types

class MockResponseForm(Form):
	method = SelectField('Method', [validators.InputRequired()], coerce=int, choices=zip([x for x in xrange(0, len(methods))], methods))
	content_type = SelectField('Content-Type', [validators.InputRequired()], coerce=int, choices=zip([x for x in xrange(0, len(content_types))], content_types))
	code = SelectField('Response Code', [validators.InputRequired()], coerce=int, choices=codes.items())
	body = TextAreaField()