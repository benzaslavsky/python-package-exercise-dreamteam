"""Give passwords the constructive disrespect they deserve."""

from .scoring import score_password


def roast_password(password: str) -> str:
    """Return a roast based on the password's score, without exposing it."""
    score = score_password(password)

    if not password:
        return "No password? Bold of you to use the honor system."
    if score == 0:
        return "Your password has a fan club. Unfortunately, they're all hackers."
    if score < 40:
        return "A locked diary with a sticky note saying 'key under mat' has better security."
    if score < 60:
        return "You gave your password a gym membership, but it never showed up."
    if score < 80:
        return "Some effort! The hackers might have to finish their coffee first."
    if score < 100:
        return "Look at you, making the hackers do a second Google search."
    return "Okay, overachiever. Did you let your cat walk across the keyboard?"
