import datetime
import locale


def parse_appointment_date(possible_date_raw_string):
    """
    Parses the raw date string of a found appointment into a datetime date.

    :param possible_date_raw_string: e.g. 'Sonntag 12.12.2021 um 15:30 Uhr'
    :return: datetime.date
    """
    locale.setlocale(locale.LC_ALL, 'de_DE')
    appointment_datetime = datetime.datetime.strptime(possible_date_raw_string, '%A %x um %H:%M Uhr')
    return appointment_datetime.date()


def parse_latest_possible_date(latest_date_raw_string):
    """
    Parses the raw date string provided by the user as an argument into a datetime date.

    :param latest_date_raw_string: e.g. '2021-12-12'
    :return: datetime.date
    """
    latest_possible_datetime = datetime.datetime.strptime(latest_date_raw_string, '%Y-%m-%d')
    return latest_possible_datetime.date()


def is_appointment_until(possible_date_raw_string, latest_date_raw_string):
    """
    Checks if the found appointment is before or on the latest possible date
    :param possible_date_raw_string:
    :param latest_date_raw_string:
    :return:
    """
    return parse_appointment_date(possible_date_raw_string) <= parse_latest_possible_date(latest_date_raw_string)