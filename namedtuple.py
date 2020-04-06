import logging
from collections import namedtuple
from datetime import datetime
from functools import reduce
from input_data import promotion_periods_first_part
from input_data import promotion_periods_second_part

logging.basicConfig(filename='intersections.log', filemode='w')

PromoPeriod = namedtuple('PromoPeriod', ['start', 'finish'])

timelines_for_check = []
intersections = []


def creat_timelines_for_check(periods, timelines):
    one_part = []
    for period in periods:
        promo_period = PromoPeriod(*period)
        one_part.append(promo_period)
    timelines.append(one_part)
    return timelines


def intersect_namedtuple(timeline1, timeline2):
    try:

        intersect_promo = PromoPeriod(
            max(
                datetime.strptime(timeline1.start, '%d/%m/%Y'),
                datetime.strptime(timeline2.start, '%d/%m/%Y')
            ),
            min(
                datetime.strptime(timeline1.finish, '%d/%m/%Y'),
                datetime.strptime(timeline2.finish, '%d/%m/%Y')
            )
        )
        return intersect_promo if intersect_promo.start <= intersect_promo.finish else None
    except ValueError:
        logging.exception('does not match format %d/%m/%Y')


def intersect_two(timelines1, timelines2):
    for timeline1 in timelines1:
        for timeline2 in timelines2:
            intersection = intersect_namedtuple(timeline1, timeline2)
            if intersection:
                yield intersection


def intersect_all(timelines):
    return reduce(intersect_two, timelines)


def get_intersections(timelines):
    for intersection in intersect_all(timelines):
        for_save = (intersection.start.day, intersection.finish.day)
        intersections.append(for_save)
    return intersections


if __name__ == '__main__':
    first_part = creat_timelines_for_check(
        promotion_periods_first_part,
        timelines_for_check
    )
    second_part = creat_timelines_for_check(
        promotion_periods_second_part,
        timelines_for_check
    )
    print(get_intersections(second_part))
