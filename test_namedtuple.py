import pytest
import datetime
from collections import namedtuple
from namedtuple import intersect_namedtuple, creat_timelines_for_check


def test_intersect_namedtuple_1():
    "There should be no intersection"
    PromoPeriod = namedtuple('PromoPeriod', ['start', 'finish'])
    assert intersect_namedtuple(
        PromoPeriod(start='5/3/2020', finish='9/3/2020'),
        PromoPeriod(start='10/3/2020', finish='10/3/2020')
        ) == None


def test_intersect_namedtuple_2():
    "There should be intersection"
    PromoPeriod = namedtuple('PromoPeriod', ['start', 'finish'])
    assert intersect_namedtuple(
        PromoPeriod(start='5/3/2020', finish='9/3/2020'),
        PromoPeriod(start='7/3/2020', finish='10/3/2020')
        ) == PromoPeriod(
            start=datetime.datetime(2020, 3, 7, 0, 0),
            finish=datetime.datetime(2020, 3, 9, 0, 0)
        )


def test_intersect_namedtuple_3():
    "There should be intersection"
    PromoPeriod = namedtuple('PromoPeriod', ['start', 'finish'])
    assert intersect_namedtuple(
        PromoPeriod(start='5/3/2020', finish='7/3/2020'),
        PromoPeriod(start='7/3/2020', finish='10/3/2020')
        ) == PromoPeriod(
            start=datetime.datetime(2020, 3, 7, 0, 0),
            finish=datetime.datetime(2020, 3, 7, 0, 0)
        )


def test_intersect_namedtuple_4():
    "There should be no intersection"
    PromoPeriod = namedtuple('PromoPeriod', ['start', 'finish'])
    assert intersect_namedtuple(
        PromoPeriod(start='55/3/2020', finish='7/3/2020'),
        PromoPeriod(start='7/3/2020', finish='10/3/2020')
        ) == None


def test_creat_timelines_for_check():
    "There should be TypeError"
    timelines = []
    with pytest.raises(TypeError):
        creat_timelines_for_check(
            ('05/03/2020', ),
            timelines
        )
