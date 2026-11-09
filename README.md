# Password Roaster

[![Build and test](https://github.com/benzaslavsky/python-package-exercise-dreamteam/actions/workflows/tests.yml/badge.svg)](https://github.com/benzaslavsky/python-package-exercise-dreamteam/actions/workflows/tests.yml)

Scores passwords and roasts the weaknesses. For fun...

## Install and use

With Python 3.11+, run from the repository root:

```sh
python -m pip install .
```

```python
from password_roaster import score_password, roast_password, password_feedback

print(score_password("Password123!"))
print(roast_password("Password123!"))
print(password_feedback("Go7!"))
# ['Use at least 12 characters, not counting spaces.']
```

- `score_password(password)` returns 0–100 based on length, character variety,
  common passwords, repetition, and sequences. Blank input scores 0.
- `roast_password(password)` returns a joke about the password's weaknesses.
- `password_feedback(password)` returns a list of short improvement tips for
  length, missing character types, common passwords, repetition, and sequences.
  Blank input returns `['Enter a password.']`. If no rule finds a weakness,
  it returns `['No obvious weaknesses found.']`; this is not a security guarantee.

All three accept strings and raise `TypeError` otherwise. None stores or sends
passwords. See [the example](examples/roast_demo.py) for more inputs.

## Development

Run from the repository root:

```sh
python -m pip install pipenv
pipenv sync --dev
pipenv run python -m pytest
pipenv run python examples/roast_demo.py
pipenv run python -m build
```

Use `python3` on macOS/Linux or `py` on Windows if needed. Pipenv manages the
virtual environment. No environment variables, secrets, or database setup needed.
GitHub Actions builds and tests PRs on Python 3.13 and 3.14.

## Team

- [Ben Zaslavsky](https://github.com/benzaslavsky)
