from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from mox.constants import methods, content_types, codes

mocks = Blueprint('mocks', __name__)

def tuh(id, method):
	from mox.models import MockResponse
	r = MockResponse.objects.get_or_404(pk=id)
	if r.method != method:
		return '', 404
	return make_response((r.body, r.code, {"Content-Type":content_types[r.content_type]}))

@mocks.route('/<id>', methods=methods)
def show(id):
	method = methods.index(request.method)
	return tuh(id, method)

@mocks.route('/', methods=['POST'])
def make():
	from mox.models import MockResponse
	code = request.json.get('code')
	method = request.json.get('method')
	content_type = request.json.get('content_type')
	body = request.json.get('body')

	# Ensure required params present
	if code is None or method is None or content_type is None:
		abort(400)

	# Ensure code, method, content_type are valid
	code_valid = codes[code] is not None
	method_idx = methods.index(method)
	content_type_idx = content_types.index(content_type)
	if not code_valid or method_idx is None or content_type_idx is None:
		abort(400)

	mr = MockResponse(code=code, method=method_idx, content_type=content_type_idx, body=body)
	mr.save()

	b = '{"id":"' + str(mr.id) + '"}"'
	h = {"Content-Type":"application/json"}
	return make_response((b, 200, h))