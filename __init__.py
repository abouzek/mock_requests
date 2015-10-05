from flask import Flask
from flask.ext.mongoengine import MongoEngine
from mox.views import mocks
import os

app = Flask(__name__)
app.config["MONGO"]
app.config["MONGODB_SETTINGS"] = {
	"db": "mox"
}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

if os.environ.get('PRODUCTION'):
	app.config["MONGODB_SETTINGS"]["host"] = os.environ.get("PROD_MONGODB")

db = MongoEngine(app)
app.register_blueprint(mocks)

if __name__ == '__main__':
	app.run()