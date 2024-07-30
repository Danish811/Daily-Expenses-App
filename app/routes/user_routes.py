from flask import Blueprint, request, jsonify
from ..services.user_service import create_user, get_user
from ..utils.validators import validate_user_input

bp = Blueprint('user', __name__, url_prefix='/api/users')

@bp.route('', methods=['POST'])
def create_user_route():
    data = request.json
    if not validate_user_input(data):
        return jsonify({"error": "Invalid input"}), 400
    user = create_user(data)
    return jsonify(user.to_dict()), 201

@bp.route('/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({"error": "User not found"}), 404