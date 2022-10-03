from one_hot_encoder import fit_transform
import pytest


test_cases = [
    ([0, 0], [(0, [1]), (0, [1])]),
    (['A+', 'A', 'B', 'C'], )
]


def test_one_category():
    categories = [0, 0]
    expected = [(0, [1]), (0, [1])]
    assert fit_transform(categories) == expected, categories


def test_many_categories():
    categories = ['A', 'B', 'C', 'B', 'A']
    expected = [
        ('A', [0, 0, 1]),
        ('B', [0, 1, 0]),
        ('C', [1, 0, 0]),
        ('B', [0, 1, 0]),
        ('A', [0, 0, 1]),
    ]
    assert fit_transform(categories) == expected, categories


def test_args():
    expected = [
        ('A', [0, 1]),
        ('B', [1, 0]),
        ('B', [1, 0]),
    ]
    assert fit_transform('A', 'B', 'B') == expected, "'A', 'B', 'B'"


def test_wrong_input():
    with pytest.raises(TypeError):
        fit_transform()