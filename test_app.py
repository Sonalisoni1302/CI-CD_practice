
import pytest
from app import div


def test_division_by_zero():
    with pytest.raises(ValueError):
        div(10, 0)


def test_normal_division():
    assert div(10, 2) == 5
