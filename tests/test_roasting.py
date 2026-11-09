import pytest

from password_roaster import roast_password


@pytest.mark.parametrize('password, fragment', [
    ('', 'honor system'), (' \t', 'loading screen'),
    ('PASSWORD', 'fan club'), ('P@ssword2026!', 'fan club'),
    ('abcabcabcabc', 'rerun'), ('safeAAA7!', 'rerun'),
    ('Z9!abcdefghijk', 'keyboard for a walk'),
    ('Go7!', 'full version'), ('8472936158', 'tracking number'),
    ('VelvetOtter7!Moonrise', 'overachiever'),
    ('sillygoose', 'All letters'), ('sillygoose!', 'avoiding math'),
    ('sillygoose7', 'outside the club'),
    ('R7! T2? MN', 'gym membership'),
    ('VelvetOtter7!', 'coffee'),
])
def test_roast_targets_weakness(password, fragment):
    assert fragment in roast_password(password)


@pytest.mark.parametrize('password', [None, 42, True, b'secret', [], {}])
def test_invalid_input(password):
    with pytest.raises(TypeError, match='password must be a string'):
        roast_password(password)


@pytest.mark.parametrize('password', ['VelvetOtter7!', 'P@ssword2026!', 'abcabcabcabc'])
def test_roasts_do_not_expose_password(password, capsys):
    message = roast_password(password)
    assert password not in message
    assert capsys.readouterr().out == ''
    assert capsys.readouterr().err == ''


def test_common_password_takes_priority_over_short_length():
    assert 'fan club' in roast_password('admin')


def test_roast_is_repeatable():
    assert roast_password('VelvetOtter7!') == roast_password('VelvetOtter7!')
