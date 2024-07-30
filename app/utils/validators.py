def validate_user_input(data):
    required_fields = ['email', 'name', 'mobile']
    return all(field in data for field in required_fields)

def validate_expense_input(data):
    required_fields = ['description', 'amount', 'split_method', 'payer_id', 'splits']
    if not all(field in data for field in required_fields):
        return False

    if data['split_method'] not in ['equal', 'exact', 'percentage']:
        return False

    splits = data['splits']
    if data['split_method'] == 'percentage':
        total_percentage = sum(split.get('percentage', 0) for split in splits)
        if total_percentage != 100:
            return False

    return True