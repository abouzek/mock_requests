import datetime
from flask import url_for
from mox import db
import uuid

class MockResponse(db.Document):
	created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
	code = db.IntField(required=True)
	body = db.StringField(default="")
	method = db.IntField(required=True)
	content_type = db.IntField(required=True)


