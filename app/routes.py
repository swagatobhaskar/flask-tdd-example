from flask import Blueprint

main_bp = Blueprint(name='/', import_name='/')

@main_bp.route('/')
def home():
    return "Hello, World! With TDD."

@main_bp.route('/about')
def about():
    return "This is the about page."
