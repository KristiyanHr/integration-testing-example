# user_module.py

def validate_user(email, password):
    """
    Валидира потребителски данни.
    """
    if "@" not in email or len(password) < 6:
        return False
    return True
