import pytest
import datetime
from main import intersect


def test_intersect_1():
    assert intersect(
        ('05/03/2020', '09/03/2020'),
        ('10/03/2020', '10/03/2020')
    ) == None


def test_intersect_2():
    assert intersect(
        ('05/03/2020', '09/03/2020'),
        ('07/03/2020', '10/03/2020')
    ) == (
        datetime.datetime(2020, 3, 7, 0, 0),
        datetime.datetime(2020, 3, 9, 0, 0)
    )


def test_intersect_3():
    assert intersect(
        ('05/03/2020', '07/03/2020'),
        ('07/03/2020', '10/03/2020')
    ) == (
        datetime.datetime(2020, 3, 7, 0, 0),
        datetime.datetime(2020, 3, 7, 0, 0)
    )


def test_intersect_4():
    assert intersect(
        ('55/03/2020', '07/03/2020'),
        ('07/03/2020', '10/03/2020')
    ) == None
