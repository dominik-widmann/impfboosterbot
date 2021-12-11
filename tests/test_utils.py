import datetime
from unittest import TestCase

from src.utils import parse_appointment_date, parse_latest_possible_date, is_appointment_until


class Test(TestCase):
    def test_parse_appointment_date(self):
        input_date = 'Sonntag 13.12.2021 um 15:30 Uhr'
        appointment_date = parse_appointment_date(input_date)
        self.assertEqual(appointment_date, datetime.date(2021, 12, 13))

    def test_parse_latest_possible_date(self):
        latest_date = parse_latest_possible_date('2021-12-15')
        self.assertEqual(latest_date, datetime.date(2021,12,15))

    def test_is_appointment_until(self):
        self.assertTrue(is_appointment_until('Sonntag 12.12.2021 um 15:30 Uhr', '2021-12-13'))
        self.assertTrue(is_appointment_until('Sonntag 13.12.2021 um 15:30 Uhr', '2021-12-13'))
        self.assertTrue(is_appointment_until('Sonntag 13.12.2021 um 15:30 Uhr', '2022-01-05'))
        self.assertFalse(is_appointment_until('Sonntag 16.12.2021 um 15:30 Uhr', '2021-12-15'))
        self.assertFalse(is_appointment_until('Sonntag 01.06.2022 um 15:30 Uhr', '2022-01-05'))
