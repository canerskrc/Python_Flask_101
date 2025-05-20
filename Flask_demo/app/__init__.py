from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fintech_data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'mysecretkey'

    db.__init__app(app)
#uygulamanın farklı bölümlerini blueprint modülleri ile tanımladık.
    from app.routes.main import main_bp
    from app.routes.data import data_bp
    from app.routes.analytics import analytics_bp
#blueprint'lerin tamamını flask içerisine kaydetme. Routes klasöründe yazacağımız yapıları aktifleştirir.
    app.register_blueprint(main_bp)
    app.register_blueprint(data_bp)
    app.register_blueprint(analytics_bp)

    with app.app_context():
        db.create_all()

    return app

