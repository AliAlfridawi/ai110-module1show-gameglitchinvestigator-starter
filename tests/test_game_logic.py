import pytest

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


@pytest.mark.parametrize(
    "difficulty, expected",
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 100)),
        ("Hard", (1, 50)),
        ("Unknown", (1, 100)),
    ],
)
def test_get_range_for_difficulty(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected


@pytest.mark.parametrize(
    "raw, expected",
    [
        (None, (False, None, "Enter a guess.")),
        ("", (False, None, "Enter a guess.")),
        ("abc", (False, None, "That is not a number.")),
        ("42", (True, 42, None)),
        ("42.9", (True, 42, None)),
    ],
)
def test_parse_guess_cases(raw, expected):
    assert parse_guess(raw) == expected


def test_winning_guess():
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_update_score_win_adds_points():
    assert update_score(current_score=0, outcome="Win", attempt_number=1) == 80


def test_update_score_win_has_floor_of_10_points():
    assert update_score(current_score=0, outcome="Win", attempt_number=20) == 10


def test_update_score_too_high_even_attempt_adds_points():
    assert update_score(current_score=10, outcome="Too High", attempt_number=2) == 15


def test_update_score_too_high_odd_attempt_subtracts_points():
    assert update_score(current_score=10, outcome="Too High", attempt_number=3) == 5


def test_update_score_too_low_subtracts_points():
    assert update_score(current_score=10, outcome="Too Low", attempt_number=2) == 5


def test_update_score_unknown_outcome_keeps_score():
    assert update_score(current_score=10, outcome="???", attempt_number=2) == 10
