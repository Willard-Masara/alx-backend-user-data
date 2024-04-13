#!/usr/bin/env python3

"""
This module provides functions for hashing passwords and validating them.
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password: A string representing the password to be hashed.

    Returns:
        A salted, hashed password as a byte string.
    """
    # Generate a salt for hashing
    salt = bcrypt.gensalt()

    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate a password against its hashed version using bcrypt.

    Args:
        hashed_password: A byte string representing the hashed password.
        password: A string representing the password to be validated.

    Returns:
        True if the password matches the hashed password, False otherwise.
    """
    # Check if the password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

