import logging
from datetime import datetime
from input_data import PROMOTION_PERIOD_FIRST_PART
from input_data import PROMOTION_PERIOD_SECOND_PART

logging.basicConfig(filename='intersections.log', filemode='w')

intersections = []


def intersect(timeline1, timeline2):
    try:
        intersect_promo = (
            max(
                datetime.strptime(timeline1[0], '%d/%m/%Y'),
                datetime.strptime(timeline2[0], '%d/%m/%Y')
            ),
            min(
                datetime.strptime(timeline1[1], '%d/%m/%Y'),
                datetime.strptime(timeline2[1], '%d/%m/%Y')
            )
        )
        return intersect_promo if intersect_promo[0] <= intersect_promo[1] else None
    except ValueError:
        logging.exception('does not match format %d/%m/%Y')


def intersect_two(timelines1, timelines2):
    for timeline1 in timelines1:
        for timeline2 in timelines2:
            intersection = intersect(timeline1, timeline2)
            if intersection:
                yield intersection


def get_intersections(timelines1, timelines2):
    for intersection in intersect_two(timelines1, timelines2):
        for_save = (intersection[0].day, intersection[1].day)
        intersections.append(for_save)
    return intersections


if __name__ == '__main__':
    print(get_intersections(
        PROMOTION_PERIOD_FIRST_PART,
        PROMOTION_PERIOD_SECOND_PART
        )
    )
