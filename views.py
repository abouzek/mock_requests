from flask import Blueprint, request, redirect, url_for, make_response
from flask.views import MethodView

mocks = Blueprint('mocks', __name__, url_prefix='/mocks')

methods = ['GET', 'POST', 'PUT', 'DELETE']

def tuh(guid, method):
	from mock_requests.models import MockResponse
	r = MockResponse.objects.get_or_404(guid=guid)
	if r.method != method:
		return '', 404
	return make_response((r.body, r.code, {"Content-Type":"application/json"}))

@mocks.route('/<guid>', methods=methods)
def show(guid):
	method = methods.index(request.method)
	return tuh(guid, method)