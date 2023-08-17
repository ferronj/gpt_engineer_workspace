from flask import Blueprint, render_template

home_blueprint = Blueprint('home', __name__)
blog_blueprint = Blueprint('blog', __name__)
projects_blueprint = Blueprint('projects', __name__)
contact_blueprint = Blueprint('contact', __name__)

@home_blueprint.route('/')
def home():
    return render_template('index.html')

@blog_blueprint.route('/blog')
def blog():
    return render_template('blog.html')

@projects_blueprint.route('/projects')
def projects():
    return render_template('projects.html')

@contact_blueprint.route('/contact')
def contact():
    return render_template('contact.html')
