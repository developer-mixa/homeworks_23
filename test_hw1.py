"""Tests for module calculate_lowest_salaries."""
import pytest

from hw1 import calculate_lowest_salaries

TEST_DATA = (
    (
        ('it', {'Nikiforov': 10.0, 'Litvinov': 20.0, 'Demyanenko': 30.0}),
        None,
        ([10.0, 20.0, 30.0], '100%'),
    ),
    (
        ('it', {'Nikiforov': 10.0, 'Litvinov': 20.0, 'Demyanenko': 30.0}),
        20,
        ([10.0, 20.0], '100%'),
    ),
)

TEST_DATA_ARGS = (
    (
        (
            ('design', {'Ramirez': 40.0, 'Stevenson': 50.0}),
            ('tech_support', {'Daniel': 60.0, 'Patel': 70.0, 'Bolton': 80.0}),
        ),
        None,
        ([40.0, 50.0, 60.0], '50%'),
    ),
    (
        (
            ('management', {'Paul': 30.0, 'Turner': 40.0, 'Peters': 50.0}),
            ('programmers', {'Wang': 60.0, 'Lamb': 70.0, 'Davis': 80.0}),
        ),
        70,
        ([30.0, 40.0, 50.0], '48%'),
    ),
    (
        (
            ('engeneers', {'Fitz': 100.0, 'Crai': 200.0, 'Aco': 300.0, 'Mac': 400.0}),
            ('network_admins', {'Griffin': 600.0, 'Coleman': 70.0, 'Fox': 80.0}),
        ),
        100.0,
        ([70.0, 80.0, 100.0], '100%'),
    ),
)


@pytest.mark.parametrize('company, limit, expected', TEST_DATA)
def test_lowest_salaries(company: tuple[str, dict], limit: None | int, expected: tuple[str]):
    """Checks the correctness of the lowest_salaries function.

    Args:
        company: contains info about one dept.
        limit: numerical limit above which salaries should not be taken.
        expected: expected values of three smallest salaries, and their ratio to all.
    """
    assert calculate_lowest_salaries(company, salary_limit=limit) == expected


@pytest.mark.parametrize('company, limit, expected', TEST_DATA_ARGS)
def test_lowest_salaries_args(company: tuple[str, dict], limit: None | int, expected: tuple[str]):
    """Checks the correctness of the lowest_salaries function with several depts in args.

    Args:
        company: contains info about several depts.
        limit: numerical limit above which salaries should not be taken.
        expected: expected values of three smallest salaries, and their ratio to all.
    """
    assert calculate_lowest_salaries(*company, salary_limit=limit) == expected