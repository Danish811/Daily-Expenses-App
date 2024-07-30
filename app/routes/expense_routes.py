from flask import Blueprint, request, jsonify
from ..services.expense_service import add_expense, get_user_expenses, get_all_expenses, generate_balance_sheet
from ..utils.validators import validate_expense_input

bp = Blueprint('expense', __name__, url_prefix='/api/expenses')

@bp.route('', methods=['POST'])
def add_expense_route():
    data = request.json
    if not validate_expense_input(data):
        return jsonify({"error": "Invalid input"}), 400
    expense = add_expense(data)
    return jsonify(expense.to_dict()), 201

@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_expenses_route(user_id):
    expenses = get_user_expenses(user_id)
    return jsonify([e.to_dict() for e in expenses])

@bp.route('', methods=['GET'])
def get_all_expenses_route():
    expenses = get_all_expenses()
    return jsonify([e.to_dict() for e in expenses])

@bp.route('/balance-sheet', methods=['GET'])
def get_balance_sheet_route():
    balance_sheet = generate_balance_sheet()
    return jsonify(balance_sheet)