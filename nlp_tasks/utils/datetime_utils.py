# -*- coding: utf-8 -*-


import datetime


def parse_dates(start_time, end_time, datetime_format='%Y%m%d%H%M%S'):
    """

    :param start_time: str，（），20190129000008
    :param end_time: str，（），20190131000008
    :param datetime_format: str，，
    :return:
    """
    result = []
    start_time = datetime.datetime.strptime(start_time, datetime_format)
    end_time = datetime.datetime.strptime(end_time, datetime_format)
    while start_time <= end_time:
        result.append(start_time.strftime('%Y%m%d'))
        start_time = start_time + datetime.timedelta(days=1)
    return result


def now(date_format_str='%Y%m%d%H%M%S'):
    """

    :param date_format_str: str,
    :return:
    """
    return datetime.datetime.now().strftime(date_format_str)


def day_ago(day_num, date_format_str='%Y%m%d%H%M%S'):
    """

    :param day_num:
    :param date_format_str:
    :return:
    """
    now = datetime.datetime.now()
    ago = now - datetime.timedelta(days=day_num)
    return ago.strftime(date_format_str)


def second_diff(start_time_str, end_time_str, date_format_str='%Y%m%d%H%M%S'):
    """

    :param start_time_str:
    :param end_time_str:
    :param date_format_str:
    :return:
    """
    start_time = datetime.datetime.strptime(start_time_str, date_format_str)
    end_time = datetime.datetime.strptime(end_time_str, date_format_str)
    diff = end_time - start_time
    total_seconds = diff.total_seconds()
    return total_seconds


def day_diff(start_time_str, end_time_str, date_format_str='%Y%m%d'):
    """

    :param start_time_str:
    :param end_time_str:
    :param date_format_str:
    :return:
    """
    start_time = datetime.datetime.strptime(start_time_str, date_format_str)
    end_time = datetime.datetime.strptime(end_time_str, date_format_str)
    diff = end_time - start_time
    days = diff.days
    return abs(days)


if __name__ == '__main__':
    start_time = '20190308'
    end_time = '20190306'
    print(day_diff(start_time, end_time))
