import unittest
from unittest.mock import MagicMock, patch

from what_is_year_now import what_is_year_now
from urllib.error import HTTPError


class TestCurrentYear(unittest.TestCase):
    def test_online_year(self):
        try:
            year = what_is_year_now()
        except HTTPError as err:
            self.assertEqual(err.code, 503, msg='Unavailable')
        else:
            self.assertEqual(year, 2022)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_format_with_dashes(self, mock_urlopen):
        cm = MagicMock()
        cm.getcode.return_value = 200
        cm.read.return_value = """{"currentDateTime": "2022-10-01"}"""
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm

        self.assertEqual(what_is_year_now(), 2022)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_format_with_dots(self, mock_urlopen):
        cm = MagicMock()
        cm.getcode.return_value = 200
        cm.read.return_value = """{"currentDateTime": "01.10.2022"}"""
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm

        self.assertEqual(what_is_year_now(), 2022)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_invalid_format(self, mock_urlopen):
        cm = MagicMock()
        cm.getcode.return_value = 200
        cm.read.return_value = """{"currentDateTime": "01/10/2022"}"""
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm
        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == '__main__':
    unittest.main()
