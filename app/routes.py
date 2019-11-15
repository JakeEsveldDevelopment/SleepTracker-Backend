from app import app
import json
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Entry


db = SQLAlchemy(app)

@app.route('/register', methods=['POST'])
def create_user():
    data = request.get_json()
    password_hash = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=password_hash, email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "new user created", "id": new_user.id})

@app.route('/login', methods=['POST'])
def login():
    return ''

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    return ''



