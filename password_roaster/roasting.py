"""Give passwords the constructive disrespect they deserve."""

from .scoring import _has_repetition, _has_sequence, _is_common, score_password


def roast_password(password: str) -> str:
    """Roast the most obvious weakness, then fall back to the score.

    More specific weaknesses take priority over generic score-based lines.
    The returned message never includes the supplied password.
    """
    score = score_password(password)

    if not password:
        return "No password? Bold of you to use the honor system."
    if password.isspace():
        return "All spaces? Your password has the same work ethic as a loading screen."
    if _is_common(password):
        return "Your password has a fan club. Unfortunately, they're all hackers."
    if _has_repetition(password):
        return "Your password is a rerun. The hackers have already seen this episode."
    if _has_sequence(password):
        return "You took your keyboard for a walk and called it a password."
    if sum(not c.isspace() for c in password) < 8:
        return "That's a password sample. When does the full version come out?"
    if password.isdecimal():
        return "All numbers? Your password is auditioning to be a tracking number."
    if score >= 80:
        return "Okay, overachiever. Did you let your cat walk across the keyboard?"
    if password.isalpha():
        return "All letters? The numbers and symbols must have declined your invite."
    if not any(c.isdecimal() for c in password):
        return "Not a single digit. Even your password is avoiding math."
    if not any(not c.isalnum() and not c.isspace() for c in password):
        return "You invited the numbers but left every symbol outside the club."
    if score < 40:
        return "A locked diary with a sticky note saying 'key under mat' has better security."
    if score < 60:
        return "You gave your password a gym membership, but it never showed up."
    return "Some effort! The hackers might have to finish their coffee first."
