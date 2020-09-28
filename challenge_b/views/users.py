from flask import Blueprint, request, session, jsonify
from flask_jwt import jwt
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import json
import datetime

from ..models import user_model

user = Blueprint('user', __name__, url_prefix='/users')

# def check_for_token(func):
#     @wraps(func)
#     def wrapped(*args, **kwargs):
#         token = request.args.get('token')
#         if not token:
#             return jsonify({'message': 'Missing token'}), 403
#         try:
#             data = jwt.deconde(token, app.config['SECRET_KEY'])
#         except:
#             return jsonify({'message': 'Invalid token'}), 403
        
#         return func(*args, *kwargs)
#     return wrapped

# @user.route('/auth-check', methods=['POST'])
# @check_for_token
# def auth_check():pass 

# @user.route('/auth', methods=['POST'])
# def authenticate():
#     if request.form['username'] and request.form['password'] == 'password_here':
#         session['logged_in'] = True
#         token = jwt.encode({
#             'user': request.form['username'],
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
#         },
#         app.config['SECRET_KEY'])
#     else:
#         return login

@user.route('/create', methods=["POST"])
def create():
    res = json.loads(request.data)
    res['password'] = generate_password_hash(res['password'])
    user = user_model.create(res)
    return str(type(user))
    return "created user", 201

@user.route('/login', methods=['POST'])
def login():
    body = json.loads(request.data)
    find_user = user_model.find({'email': body['email']})

    if check_password_hash(find_user['password'], body['password']):    
        session['user'] = find_user['username']
        session['logged'] = True
        return "Logged in: %s" % find_user['username'], 200
    

    