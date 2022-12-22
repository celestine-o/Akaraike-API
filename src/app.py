from flask import Flask, abort, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from functools import wraps
from flask_migrate import Migrate
import jwt
import logging
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from datetime import datetime, timezone, timedelta
from database.models import  User, db_drop_and_create_all, setup_db, db
from generator import *

app = Flask(__name__)
setup_db(app)
app.config['SECRET_KEY'] = '*7f8A5+)-8@54$>t+t>t73?5jUc32+I8BB*i8-fi52a2StjitI'
bcrypt = Bcrypt(app)
CORS(app, resources={r"*/api/*": {"origins": "*"}})
migrate = Migrate(app, db)

logging.basicConfig(
    filename='app.log', filemode='a', format='%(levelname)s in %(module)s: %(message)s', 
    datefmt='%d-%b-%y %H:%M:%S'
)

current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# with app.app_context():
#   db_drop_and_create_all()

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

@app.route('/')
@cross_origin()
def index():
    try:
        return jsonify({
            'success': True
        })
    except Exception:
        abort(400)

@app.route('/register', methods=['POST'])
@cross_origin()
def register():
    '''
    Used to register a new account, expected input should come in this format \n
    {
        "email": "test005@test.com",
        "username": "Bee5",
        "password": "test5"
    }
    '''
    body = request.get_json()
    # # Get user info
    email = body.get("email")
    username = body.get("username")
    password = body.get("password")

    # New user's details are saved to the database
    try:
        new_user = User(
            email=email,
            username=username,
            password=generate_password_hash(password, 10),
            public_id=str(generate_password(30, lower_char, numbers)),
            date_created=current_time,
        )
        if user := User.query.filter_by(username=username).first():
            return jsonify({
                "message": "Username already exist"
            })
        elif user := User.query.filter_by(email=email).first():
            return jsonify({
                "message": "Email already exist"
            })
        new_user.insert()

        return jsonify({"success": True, "message": f"{username} created"})
    except Exception:
        abort(400)

@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    '''
    Used to login user, expected input should come in this the format \n
    {
    "username": "Bee5",
    "password": "test5"
    }
    '''
    body = request.get_json()
    # Get user login details
    username = body.get("username")
    password = body.get("password")

    #User should be able to login with his username to access resources
    try:
        user = User.query.filter_by(username=username).first()
        if not user and not check_password_hash(user.password, password):
            return ({
                "success": False,
                "message": "Invalid username or password"
            })
        # Public_id was used so that user's details e.g username does not appear when
        # the token is decoded.
        token = jwt.encode(
            {
                'public_id': user.public_id, 'exp': datetime.now(timezone.utc) + timedelta(minutes=45)
            }, app.config['SECRET_KEY'], "HS256"
        )
        return jsonify({'token' : token})
    except Exception:
        abort(400)


@app.route('/alpha')
@cross_origin()
@token_required
def alphabet():

    body = request.get_json()
    length = int(body.get("length"))

    password = generate_password(length, lower_char, upper_char)
    strength = check_password_strength(password)
    return jsonify({
        'success': True,
        'password': password,
        'strength score': strength
    })

@app.route('/alphanumeric')
@cross_origin()
@token_required
def alphanumeric():

    body = request.get_json()
    length = int(body.get("length"))

    password = generate_password(length, upper_char, lower_char, numbers)
    strength = check_password_strength(password)
    return jsonify({
        'success': True,
        'password': password,
        'strength score': strength
    })

@app.route('/alphanumx')
@cross_origin()
@token_required
def alphanumx():

    body = request.get_json()
    length = int(body.get("length"))
    
    password = generate_password(length, upper_char, lower_char, numbers, special_char)
    strength = check_password_strength(password)
    return jsonify({
        'success': True,
        'password': password,
        'strength score': strength
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

@app.errorhandler(AuthError)
@cross_origin()
def authentication_error(auth_error):
    return jsonify({
        "success": False,
        "error": auth_error.status_code,
        "message": auth_error.error
    }), auth_error.status_code