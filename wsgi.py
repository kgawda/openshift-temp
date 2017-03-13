import os

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/test")
def testpage():
    return "Test passed for "+os.environ.get('APP_MAIN_USER','user')

@application.route("/post")
def post():
    return "TBD"

if __name__ == "__main__":
    application.run()
