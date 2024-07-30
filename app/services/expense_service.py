from ..models import Expense, ExpenseSplit, User
from .. import db

def add_expense(data):
    expense = Expense(
        description=data['description'],
        amount=data['amount'],
        split_method=data['split_method'],
        payer_id=data['payer_id']
    )
    db.session.add(expense)
    db.session.flush()

    splits = data['splits']
    for split in splits:
        expense_split = ExpenseSplit(
            expense_id=expense.id,
            user_id=split['user_id'],
            amount=split.get('amount'),
            percentage=split.get('percentage')
        )
        db.session.add(expense_split)

    db.session.commit()
    return expense

def get_user_expenses(user_id):
    return Expense.query.filter_by(payer_id=user_id).all()

def get_all_expenses():
    return Expense.query.all()

def generate_balance_sheet():
    users = User.query.all()
    balance_sheet = {user.id: 0 for user in users}

    expenses = Expense.query.all()
    for expense in expenses:
        payer_id = expense.payer_id
        splits = ExpenseSplit.query.filter_by(expense_id=expense.id).all()

        for split in splits:
            if split.user_id != payer_id:
                balance_sheet[payer_id] += split.amount
                balance_sheet[split.user_id] -= split.amount

    return balance_sheet