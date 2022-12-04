import unittest
from unittest.mock import MagicMock, patch

from what_is_year_now import what_is_year_now
from urllib.error import HTTPError


class TestCurrentYear(unittest.TestCase):
    def cm_urlopen(self, response):
        """
        Возвращает MagicMock-объект context manager
        с желаемым response.
        """
        cm = MagicMock()
        cm.read.return_value = response
        cm.__enter__.return_value = cm
        return cm

    def test_online_year(self):
        try:
            year = what_is_year_now()
        except HTTPError as err:
            # иногда сервис недоступен, поэтому проверяем код ошибки 503
            self.assertEqual(err.code, 503, msg='Unavailable')
        else:
            # если сервис доступен, проверяем год
            self.assertEqual(year, 2022)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_format_with_dashes(self, mock_urlopen):
        response = '{"currentDateTime": "2022-10-01"}'
        mock_urlopen.return_value = self.cm_urlopen(response)
        self.assertEqual(what_is_year_now(), 2022)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_format_with_dots(self, mock_urlopen):
        response = '{"currentDateTime": "01.10.2022"}'
        mock_urlopen.return_value = self.cm_urlopen(response)
        self.assertEqual(what_is_year_now(), 2022)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_invalid_format(self, mock_urlopen):
        response = '{"currentDateTime": "01/10/2022"}'
        mock_urlopen.return_value = self.cm_urlopen(response)
        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == '__main__':
    unittest.main()
