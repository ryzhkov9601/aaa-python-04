import unittest

from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):

    def test_one_category(self):
        categories = [0, 0]
        expected = [(0, [1]), (0, [1])]
        self.assertEqual(fit_transform(categories), expected, msg=categories)

    def test_first_item_in(self):
        categories = ['A', 'B', 'C', 'B', 'A']
        expected_item = ('A', [0, 0, 1])
        self.assertIn(expected_item, fit_transform(categories), msg=categories)

    def test_zero_not_in(self):
        self.assertNotIn([0], fit_transform('123')[0], msg="'123'")

    def test_args(self):
        expected = [
            ('A', [0, 1]),
            ('B', [1, 0]),
        ]
        self.assertEqual(fit_transform('A', 'B'), expected, msg="'A', 'B'")

    def test_wrong_input(self):
        self.assertRaises(TypeError, fit_transform)


if __name__ == '__main__':
    print(1455)
    unittest.main()
