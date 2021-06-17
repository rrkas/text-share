from flask import Flask
from .config import Config


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    app.app_context().push()

    from .main.routes import main_bp
    app.register_blueprint(main_bp)

    return app
