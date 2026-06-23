import pytest
from logic_utils import check_guess


def test_check_guess_too_high():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_check_guess_too_low():
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_check_guess_correct():
    outcome, message = check_guess(42, 42)
    assert outcome == "Correct"
    assert message == "🎉 You got it!"
