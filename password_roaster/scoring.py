"""Simple, transparent scoring for our password roasting game."""

import string


# A small starter list, not a comprehensive database of leaked passwords.
COMMON_PASSWORDS = frozenset({
    "password", "password1", "password123", "password123!", "123456",
    "12345678", "123456789", "1234567890", "qwerty", "qwerty123",
    "abc123", "admin", "letmein", "welcome", "iloveyou", "monkey",
})


def score_password(password: str) -> int:
    """Return a playful heuristic score from 0 to 100.

    Each character earns 5 points (up to 80), an ASCII digit earns a
    10-point bonus, and ASCII punctuation earns another 10-point bonus.
    Known common passwords score zero, ignoring case. Empty input also
    scores zero. Whitespace counts toward length, but is not a symbol.

    This score is for entertainment, not a measure of cracking resistance.
    The password is never printed, stored, or sent anywhere.
    """
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    if password.casefold() in COMMON_PASSWORDS:
        return 0

    length_points = min(len(password) * 5, 80)
    digit_points = 10 if any(c in string.digits for c in password) else 0
    symbol_points = 10 if any(c in string.punctuation for c in password) else 0
    return length_points + digit_points + symbol_points
