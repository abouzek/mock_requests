from flask import Flask
from flask.ext.mongoengine import MongoEngine
from views import mocks
import os

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
	"db": "mox"
}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

if os.environ.get('HEROKU') == 1:
	app.config["MONGODB_SETTINGS"]["host"] = os.environ.get("MONGODB_URI")

db = MongoEngine(app)
app.register_blueprint(mocks)

if __name__ == '__main__':
	app.run()