# coding=utf-8

from unittest import TestCase


def director(steps):
    prev = 'up'
    for step_count in steps:
        prev = {
            'up': 'right',
            'down': 'left',
            'left': 'up',
            'right': 'down'
        }.get(prev)
        yield prev, step_count


def step_counter(array_len):
    for steps in range(array_len, 0, -1):
        if steps != array_len:
            yield steps
        yield steps


def next_coord(direction, x, y):
    return {
        'left': (x - 1, y),
        'right': (x + 1, y),
        'up': (x, y - 1),
        'down': (x, y + 1),
    }.get(direction)


def snail(array):
    x, y = -1, 0
    result = []
    for direction, steps in director(step_counter(len(array))):
        for _ in range(steps):
            x, y = next_coord(direction, x, y)
            result.append(array[y][x])
    return result


class SnailTest(TestCase):
    def test_next_coord(self):
        self.assertEquals(next_coord('left', 1, 1), (0, 1))
        self.assertEquals(next_coord('right', 1, 1), (2, 1))
        self.assertEquals(next_coord('up', 1, 1), (1, 0))
        self.assertEquals(next_coord('down', 1, 1), (1, 2))

    def test_simple(self):
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        # 3 2 2 1 1

        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEquals(snail(array), expected)

    def test_one_more(self):
        array = [[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEquals(snail(array), expected)

    def test_quad(self):
        array = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
        # 4 3 3 2 2 1 1
        expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEquals(snail(array), expected)


if __name__ == '__main__':
    SnailTest().test_simple()
