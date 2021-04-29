import unittest
from utils import duration_en_min, convert_time, date_to_week, accumulate_km


class TestCase(unittest.TestCase):
    """ tests for 'script.py'"""

    def test_duration_en_min(self):
        """ """
        duree = duration_en_min(78.64985)
        self.assertEqual(duree, 1.18)

    def test_convert_time(self):
        """ """
        time = convert_time(1619542281)
        self.assertEqual(time, [2021, 4, 27])

    def test_date_to_week(self):
        week = date_to_week([2021, 4, 27])
        self.assertEqual(week, "17")

    # def test_accumulate_km(self):
    #     acc = accumulate_km()


if __name__ == '__main__':
    unittest.main()
