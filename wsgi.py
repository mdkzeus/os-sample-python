from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Casper!\n updated git repo now with modified code"

if __name__ == "__main__":
    application.run()
