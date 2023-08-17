from flask import Flask
from routes import home_blueprint, blog_blueprint, projects_blueprint, contact_blueprint

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(home_blueprint)
    app.register_blueprint(blog_blueprint)
    app.register_blueprint(projects_blueprint)
    app.register_blueprint(contact_blueprint)
