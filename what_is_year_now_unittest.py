import unittest

from what_is_year_now import what_is_year_now


class TestCurrentYear(unittest.TestCase):
    def test_online_year(self):
        self.assertEqual(what_is_year_now(), 2022)


if __name__ == '__main__':
    unittest.main()
