from flask import Blueprint, request, make_response, jsonify, render_template
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from constants import codes, methods, content_types
from forms import MockResponseForm

mocks = Blueprint('mocks', __name__)

def tuh(id, method):
	from models import MockResponse
	r = MockResponse.objects.get_or_404(pk=id)
	if r.method != method:
		return '', 404
	return make_response((r.body, r.code, {"Content-Type":content_types[r.content_type]}))

@mocks.route('/<id>', methods=methods)
def show(id):
	method = methods.index(request.method)
	return tuh(id, method)

@mocks.route('/', methods=['GET','POST'])
def make():
	form = MockResponseForm(request.form)
	if request.method == 'POST' and form.validate():
		# Creating a mock response
		from models import MockResponse
		mr = MockResponse(
			code=form.code.data, 
			method=form.method.data, 
			content_type=form.content_type.data, 
			body=form.body.data
		)

		# Check for existing and return it if exists
		existing = MockResponse.objects(
			code=mr.code, 
			method=mr.method, 
			content_type=mr.content_type,
			body=mr.body
		).first()

		if existing is None:
			mr.save()
		else:
			mr = existing
		return jsonify(id=str(mr.id))

	return render_template('home.html', form=form)




