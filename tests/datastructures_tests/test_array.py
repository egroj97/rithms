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


class DynamicArrayTestSuite(unittest.TestCase):
    def test_dynamic_array_creation(self):
        self.assertTrue(arrays.DynamicArray(10))

    def test_dynamic_array_getting(self):
        arr = arrays.DynamicArray(data=[1, 2, 3, 4])
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)
        self.assertEqual(arr[2], 3)
        self.assertEqual(arr[3], 4)

    def test_dynamic_array_setting(self):
        arr = arrays.DynamicArray(4)

        arr[0] = 1
        arr[1] = 2
        arr[2] = 3
        arr[3] = 4

        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)
        self.assertEqual(arr[2], 3)
        self.assertEqual(arr[3], 4)

    def test_failure_on_null_dynamic_array(self):
        try:
            arrays.DynamicArray(data=[])
        except ValueError:
            self.assertTrue(True)

    def test_failure_on_zero_dynamic_array(self):
        try:
            arrays.DynamicArray(0)
        except ValueError:
            self.assertTrue(True)

    def test_failure_on_negative_sized_dynamic_array(self):
        try:
            arrays.DynamicArray(-10)
        except ValueError:
            self.assertTrue(True)

    def test_append_dynamic_array(self):
        arr = arrays.DynamicArray(data=[1, 2, 3, 4, 5, 6])
        for i in range(100):
            arr.append(i)

        self.assertEqual(arr.last(), 99)
        self.assertEqual(arr.size(), 106)

    def test_pop_dynamic_array(self):
        arr = arrays.DynamicArray(data=[1, 2, 3, 4, 5, 6])
        for i in range(6):
            arr.pop()

        try:
            arr.last()
        except ValueError:
            self.assertTrue(True)
        self.assertEqual(arr.size(), 0)


if __name__ == '__main__':
    unittest.main()
