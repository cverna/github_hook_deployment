from flask import Flask

from .webhooks import webhook

def create_app():
    """ Create, configure and return the Flask application """

    app = Flask(__name__)
    app.config['GITHUB_SECRET'] = 'asupersecretpassphraseformywebhook'
    app.config['REPO_PATH'] = '/root/github_hook_deployment/'
    app.register_blueprint(webhook)

    return(app)
