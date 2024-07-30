from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from .routes import user_routes, expense_routes
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(expense_routes.bp)

    return app