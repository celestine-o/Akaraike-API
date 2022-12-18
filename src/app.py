from flask import Flask, abort, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from functools import wraps
import jwt
import logging

from generator import *
gen = PasswordGenerator()
chars = ''

app = Flask(__name__)

app.config['SECRET_KEY'] = '$Celestine$'

CORS(app, resources={r"*/api/*": {"origins": "*"}})

logging.basicConfig(
    filename='app.log', filemode='w', format='%(levelname)s in %(module)s: %(message)s', 
    datefmt='%d-%b-%y %H:%M:%S'
)

'''
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get('Authorization', None)
    if not auth:
        raise AuthError({
            'code': 'authorization_header_missing',
            'description': 'Authorization header is expected.'
        }, 401)

    parts = auth.split()
    if parts[0].lower() != 'bearer':
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must start with "Bearer".'
        }, 401)

    elif len(parts) == 1:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Token not found.'
        }, 401)

    elif len(parts) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must be bearer token.'
        }, 401)

    return parts[1]
    
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = get_token_auth_header()
        if 'x-access-tokens' in request.headers:
            #token = request.headers['x-access-tokens']
            token = request.args.get('token')

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except Exception:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator
'''

@app.route('/')
@cross_origin()
def index():
    try:
        return jsonify({
            'success': True
        })
    except Exception:
        abort(400)

@app.route('/alpha')
@cross_origin()
def alphabet():

    body = request.get_json()
    length = int(body.get("length"))

    chars = gen.lower_char + gen.upper_char
    password = gen.generate_password(length, chars)
    strength = gen.check_password_strength(password)
    return jsonify({
        'success': True,
        'password': password,
        'strength': strength
    })

@app.route('/alphanumeric')
@cross_origin()
def alphanumeric():

    body = request.get_json()
    length = int(body.get("length"))

    chars = gen.lower_char + gen.upper_char + gen.numbers
    i_pass = gen.generate_password(length, chars)

    for i in gen.numbers:
        if i in i_pass:
            return i_pass
        else:
            alphanumeric()
        return i_pass
    password = i_pass

    strength = gen.check_password_strength(password)
    return jsonify({
        'success': True,
        'password': password,
        'strength': strength
    })

@app.route('/alphanumx')
@cross_origin()
def alphanumx():

    body = request.get_json()
    length = int(body.get("length"))
    
    chars = gen.lower_char + gen.upper_char + gen.numbers + gen.special_char
    i_pass = gen.generate_password(length, chars)

    for i in gen.numbers:
        if i in i_pass:
            return i_pass
        else:
            alphanumx()
        return i_pass
    for i in gen.special_char:
        if i in i_pass:
            return i_pass
        else:
            alphanumx()
        return i_pass

    strength = gen.check_password_strength(i_pass)
    return jsonify({
        'success': True,
        'password': i_pass,
        'strength': strength
    })

@app.errorhandler(400)
@cross_origin()
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400


@app.errorhandler(401)
@cross_origin()
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Unauthorized"
    }), 401

@app.errorhandler(404)
@cross_origin()
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource Not Found"
    }), 404

@app.errorhandler(405)
@cross_origin()
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "Method Not Allowed"
    }), 405

@app.errorhandler(422)
@cross_origin()
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable"
    }), 422