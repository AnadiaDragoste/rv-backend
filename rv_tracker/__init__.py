from flask import Flask
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from .extensions import db, migrate
from .maintenance import maintenance_bp


def create_app(config_name="development"):
    app = Flask(__name__)

    config_options = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }

    config_class = config_options.get(config_name, DevelopmentConfig)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(maintenance_bp)

    return app