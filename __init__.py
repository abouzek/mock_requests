from flask import Flask
from flask.ext.mongoengine import MongoEngine
from mock_requests.views import mocks

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "mock_requests"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)
app.register_blueprint(mocks)

if __name__ == '__main__':
	app.run()