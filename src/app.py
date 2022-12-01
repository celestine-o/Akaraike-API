from flask import Flask, jsonify, abort
from flask_cors import CORS, cross_origin

from generator import *



app = Flask(__name__)
CORS(app, resources={r"*/api/*": {"origins": "*"}})


@app.route('/')
def index():
    try:
        return jsonify({
            'success': True
        })
    except Exception:
        abort(400)


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