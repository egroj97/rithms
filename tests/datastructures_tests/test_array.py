import unittest

from tests.context import arrays


class ArrayTestSuite(unittest.TestCase):
    def test_array_creation(self):
        self.assertTrue(arrays.Array(10))

    def test_array_getting(self):
        arr = arrays.Array(data=[1, 2, 3, 4])
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)
        self.assertEqual(arr[2], 3)
        self.assertEqual(arr[3], 4)

    def test_array_setting(self):
        arr = arrays.Array(4)

        arr[0] = 1
        arr[1] = 2
        arr[2] = 3
        arr[3] = 4

        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)
        self.assertEqual(arr[2], 3)
        self.assertEqual(arr[3], 4)

    def test_failure_on_null_array(self):
        try:
            arrays.Array(data=[])
        except ValueError:
            self.assertTrue(True)

    def test_failure_on_zero_array(self):
        try:
            arrays.Array(0)
        except ValueError:
            self.assertTrue(True)

    def test_failure_on_negative_sized_array(self):
        try:
            arrays.Array(-10)
        except ValueError:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
