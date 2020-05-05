import pytest
import datetime
from main import intersect


def test_intersect_1():
    "There should be no intersection"
    assert intersect(
        ('05/03/2020', '09/03/2020'),
        ('10/03/2020', '10/03/2020')
    ) == None


def test_intersect_2():
    "There should be intersection"
    assert intersect(
        ('05/03/2020', '09/03/2020'),
        ('07/03/2020', '10/03/2020')
    ) == (
        datetime.datetime(2020, 3, 7, 0, 0),
        datetime.datetime(2020, 3, 9, 0, 0)
    )


def test_intersect_3():
    "There should be intersection"
    assert intersect(
        ('05/03/2020', '07/03/2020'),
        ('07/03/2020', '10/03/2020')
    ) == (
        datetime.datetime(2020, 3, 7, 0, 0),
        datetime.datetime(2020, 3, 7, 0, 0)
    )


def test_intersect_4():
    "There should be no intersection"
    assert intersect(
        ('55/03/2020', '07/03/2020'),
        ('07/03/2020', '10/03/2020')
    ) == None


def test_intersect_5():
    "There should be IndexError"
    with pytest.raises(IndexError):
        intersect(
            ('05/03/2020', ),
            ('07/03/2020', '10/03/2020')
        )
