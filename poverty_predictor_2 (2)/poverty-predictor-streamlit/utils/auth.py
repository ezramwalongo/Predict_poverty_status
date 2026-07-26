"""
Simple username/password authentication for the Poverty Predictor app.

Users are stored in data/users.csv as: username, salt, password_hash
Passwords are never stored in plain text — each password is hashed with a
per-user random salt (SHA-256).

Rules enforced here (per app requirements):
  - Username = the user's first name (letters only, no spaces/digits).
  - Password = exactly 8 digits (numeric only).
"""

import os
import re
import hashlib
import secrets
import pandas as pd

USERS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'users.csv')

USERNAME_PATTERN = re.compile(r'^[A-Za-z]+$')
PASSWORD_PATTERN = re.compile(r'^\d{8}$')

COLUMNS = ['username', 'salt', 'password_hash']


def _ensure_store():
    os.makedirs(os.path.dirname(USERS_PATH), exist_ok=True)
    if not os.path.exists(USERS_PATH):
        pd.DataFrame(columns=COLUMNS).to_csv(USERS_PATH, index=False)


def _load_users() -> pd.DataFrame:
    _ensure_store()
    try:
        return pd.read_csv(USERS_PATH, dtype=str)
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=COLUMNS)


def _hash_password(password: str, salt: str) -> str:
    return hashlib.sha256((salt + password).encode('utf-8')).hexdigest()


def validate_username(username: str) -> bool:
    """Username must be a first name: letters only, no spaces or digits."""
    return bool(username) and bool(USERNAME_PATTERN.match(username.strip()))


def validate_password(password: str) -> bool:
    """Password must be exactly 8 digits."""
    return bool(password) and bool(PASSWORD_PATTERN.match(password))


# A short blacklist of obviously weak 8-digit passwords (not exhaustive —
# just enough to catch the most common lazy choices).
_WEAK_PASSWORDS = {
    '12345678', '87654321', '00000000', '11111111', '22222222', '33333333',
    '44444444', '55555555', '66666666', '77777777', '88888888', '99999999',
    '01234567', '76543210', '10203040', '90807060', '12341234', '13579246',
}


def is_strong_password(password: str) -> bool:
    """
    A valid (8-digit) password is considered STRONG if it is not an
    obviously weak/guessable pattern: not all the same digit, not a
    straight ascending/descending run, and not in the common-weak list.
    Used only to guide the user (via the strength hint and the "generate
    recommended password" button) — it does not block registration.
    """
    if not validate_password(password):
        return False
    if password in _WEAK_PASSWORDS:
        return False
    if len(set(password)) == 1:
        return False
    digits = [int(c) for c in password]
    ascending = all(digits[i + 1] - digits[i] == 1 for i in range(len(digits) - 1))
    descending = all(digits[i] - digits[i + 1] == 1 for i in range(len(digits) - 1))
    if ascending or descending:
        return False
    return True


def generate_recommended_password() -> str:
    """Generate a random 8-digit password that passes is_strong_password."""
    while True:
        candidate = ''.join(str(secrets.randbelow(10)) for _ in range(8))
        if is_strong_password(candidate):
            return candidate


def user_exists(username: str) -> bool:
    users = _load_users()
    if users.empty:
        return False
    return username.strip().lower() in users['username'].str.lower().values


def register_user(username: str, password: str):
    """
    Register a new user.
    Returns (success: bool, message_key: str) where message_key is an i18n key.
    """
    username = (username or '').strip()
    password = (password or '').strip()

    if not validate_username(username):
        return False, 'error_invalid_username'
    if not validate_password(password):
        return False, 'error_invalid_password'
    if user_exists(username):
        return False, 'error_username_taken'

    users = _load_users()
    salt = secrets.token_hex(16)
    new_row = pd.DataFrame([{
        'username': username,
        'salt': salt,
        'password_hash': _hash_password(password, salt),
    }])
    users = pd.concat([users, new_row], ignore_index=True)
    users.to_csv(USERS_PATH, index=False)
    return True, 'success_registration'


def authenticate_user(username: str, password: str):
    """
    Verify username/password.
    Returns (success: bool, message_key: str).
    """
    username = (username or '').strip()
    password = (password or '').strip()

    if not username or not password:
        return False, 'error_missing_fields'

    users = _load_users()
    if users.empty:
        return False, 'error_user_not_found'

    match = users[users['username'].str.lower() == username.lower()]
    if match.empty:
        return False, 'error_user_not_found'

    row = match.iloc[0]
    expected_hash = _hash_password(password, row['salt'])
    if expected_hash != row['password_hash']:
        return False, 'error_wrong_password'

    return True, 'success_login'
