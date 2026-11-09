# Password Roaster

[![Build and test](https://github.com/benzaslavsky/python-package-exercise-dreamteam/actions/workflows/tests.yml/badge.svg)](https://github.com/benzaslavsky/python-package-exercise-dreamteam/actions/workflows/tests.yml)

Scores passwords and roasts the weaknesses. For fun...

## Install and use

With Python 3.11+:

```sh
python -m pip install dreamteam-password-roaster
```

[View the package on PyPI](https://pypi.org/project/dreamteam-password-roaster/).

```python
from password_roaster import score_password, roast_password

print(score_password("Password123!"))  # 10
print(roast_password("Password123!"))
# Your password has a fan club. Unfortunately, they're all hackers.
```

- `score_password(password)` returns 0–100 based on length, character variety,
  common passwords, repetition, and sequences. Blank input scores 0.
- `roast_password(password)` returns a joke about the password's weaknesses.

These functions accept strings and raise `TypeError` otherwise. Neither stores or sends
passwords. See [the example](examples/roast_demo.py) for more inputs.

## Password face-off

`compare_passwords(first, second)` returns both scores and a winner:
`first`, `second`, or `tie`. Equal scores are a tie even if the passwords differ.
Both inputs must be strings. The result does not include either password.

```python
from password_roaster import compare_passwords

print(compare_passwords("Go7!", "VelvetOtter7!"))
# {'first_score': 30, 'second_score': 79, 'winner': 'second'}
```

After installing the local package, run `python -m examples.faceoff_demo` from
the repository root to see both winners and a tie. These are game scores,
not a guarantee that the winning password is safe.

## Development

Run from the repository root:

```sh
python -m pip install pipenv
pipenv sync --dev
pipenv run python -m pytest
pipenv run python -m examples.roast_demo
pipenv run python -m build
```

Use `python3` on macOS/Linux or `py` on Windows if needed. Pipenv manages the
virtual environment. No environment variables, secrets, or database setup needed.
GitHub Actions builds and tests PRs on Python 3.13 and 3.14.

## Team

- [Ben Zaslavsky](https://github.com/benzaslavsky)
- [TEMP](https://github.com/temp)
- [TEMP](https://github.com/temp)
- [TEMP](https://github.com/temp)
- [TEMP](https://github.com/temp)
