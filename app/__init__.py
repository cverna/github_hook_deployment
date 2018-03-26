from flask import Flask

from .webhooks import webhook

def create_app():
    """ Create, configure and return the Flask application """

    app = Flask(__name__)
    app.config['GITHUB_SECRET'] = 'asupersecretpassphraseformywebhook'
    app.register_blueprint(webhook)

    return(app)
