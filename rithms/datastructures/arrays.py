class Array:
    def __init__(self, size: int = 0, data=None):
        if size == 0 and not data:
            raise ValueError('Size of the array must be greater than zero (0)')

        if data is None:
            data = [0 for _ in range(size)]

        self.size = size if size > 0 else len(data)
        self._data = data

    def __getitem__(self, key: int):
        if self.size <= key:
            raise TypeError('key must be smaller than array size')

        return self._data[key]

    def __setitem__(self, key: int, value):
        if self.size <= key:
            raise TypeError('key must be smaller than array size')

        self._data[key] = value
