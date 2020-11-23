class Array:
    def __init__(self, size: int = 0, data=None):
        if size == 0 and not data:
            raise ValueError('Size of the array must be greater than zero (0)')

        if data is None:
            data = [None for _ in range(size)]

        self._size = size if size > 0 else len(data)
        self._data = data

    def __getitem__(self, key: int):
        if self._size < key:
            raise TypeError('key must be smaller than array size')

        return self._data[key]

    def __setitem__(self, key: int, value):
        if self._size < key:
            raise TypeError('key must be smaller than array size')

        self._data[key] = value

    def size(self):
        return self._size

    def first(self):
        return self.__getitem__(0)

    def last(self):
        return self.__getitem__(self.size() - 1)


class DynamicArray:
    def __init__(self, size: int = 0, data=None):
        self._data = Array(size, data)
        self._capacity = self._data.size()
        index = 0
        while index < self._data.size() and self._data[index]:
            index += 1
        self._last_index = index-1

    def append(self, value):
        if self._last_index+1 == self._capacity:
            temp = Array(size=self._data.size() * 2)
            for i in range(self._capacity):
                temp[i] = self.__getitem__(i)

            self._data = temp
            self._capacity = self._data.size()

        self._data[self._last_index+1] = value
        self._last_index += 1

    def pop(self):
        if (self._last_index <= (self._data.size() // 4)) and (self._data.size() > 2):
            resize = self._data.size() // 2
            temp = Array(size=resize)
            for i in range(resize):
                temp[i] = self.__getitem__(i)
            self._data = temp

        self._data[self._last_index] = None
        self._last_index -= 1
        self._capacity = self._data.size()

    def __getitem__(self, key: int):
        if self._capacity <= key:
            raise TypeError('key must be smaller than array size')

        return self._data[key]

    def __setitem__(self, key: int, value):
        if self._capacity <= key:
            raise TypeError('key must be smaller than array size')

        self._data[key] = value

    def size(self):
        return self._last_index+1

    def last(self):
        return self._data[self._last_index]
