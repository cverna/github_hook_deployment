import os
from flask import Flask

from .webhooks import webhook

def create_app():
    """ Create, configure and return the Flask application """

    app = Flask(__name__)
    app.config['GITHUB_SECRET'] = os.environ.get('GITHUB_SECRET')
    app.config['REPO_PATH'] = os.environ.get('REPO_PATH')
    app.register_blueprint(webhook)

    return(app)
