from flask import Flask
from config import Config
from app.models.database import db
from flask_jwt_extended import JWTManager
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'
    app.config['SWAGGER'] = {
        'title': 'Smart Attendance API',
        'version': '1.0.0',
        'description': 'Backend API for Mobile Facial Recognition Attendance System'
    }
    
    db.init_app(app)
    jwt = JWTManager(app)
    Swagger(app)
    
    # Register blueprints
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    with app.app_context():
        db.create_all()
    
    return app
