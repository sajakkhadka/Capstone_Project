from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models.database import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Check if user already exists
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({'message': 'User already exists'}), 400
    
    # Hash the password
    hashed_password = generate_password_hash(data['password'])
    
    # Create new user
    new_user = User(
        full_name=data['full_name'],
        email=data['email'],
        password=hashed_password,
        role=data['role']
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201


@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Find user by email
    user = User.query.filter_by(email=data['email']).first()
    
    # Check if user exists and password is correct
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid email or password'}), 401
    
    # Create token
    access_token = create_access_token(identity={
        'id': user.id,
        'email': user.email,
        'role': user.role
    })
    
    return jsonify({
        'message': 'Login successful',
        'token': access_token,
        'role': user.role
    }), 200
