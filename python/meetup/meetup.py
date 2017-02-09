from datetime import date, timedelta


weekdays = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6,
}

orders = {
    '2nd': 1,
    '3rd': 2,
    '4th': 3,
    '5th': 4,
}


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, weekday, order):
    weekday = weekdays[weekday]
    direction = 1

    if order == 'last':
        day = date(year, month + 1, 1) if month < 12 \
              else date(year + 1, 1, 1)
        day += timedelta(days=-1)
        direction = -1
    elif order == 'teenth':
        day = date(year, month, 10)
    else:
        day = date(year, month, 1)

    if day.weekday() != weekday:
        if direction > 0:
            day += timedelta(days=(weekday - day.weekday()) % 7)
        else:
            day -= timedelta(days=(day.weekday() - weekday) % 7)

    if order in orders:
        day += direction * timedelta(days=7 * orders[order])

    if day.year != year or day.month != month:
        raise MeetupDayException

    return day
