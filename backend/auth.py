from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password):
    """
    Convert plain password into a secure hashed password.
    """

    return generate_password_hash(password)


def verify_password(password, hashed_password):
    """
    Compare entered password with stored hashed password.
    """

    return check_password_hash(hashed_password, password)