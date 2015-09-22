import datetime
from flask import url_for
from mock_requests import db
import uuid

class MockResponse(db.Document):
	guid = db.UUIDField(default=uuid.uuid1(), required=True)
	created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
	code = db.IntField(required=True)
	body = db.StringField(default="")
	method = db.IntField(required=True)


