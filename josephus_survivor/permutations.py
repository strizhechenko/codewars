# coding=utf-8

from unittest import TestCase

"""
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
[1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
[1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
[1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
[1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
[4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
[] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]
"""


def josephus(people, k):
    index, killed = 0, []
    while people:
        index = (index + k - 1) % len(people)
        killed.append(people.pop(index))
    return killed


class JosephusTest(TestCase):
    def test_josephus1(self):
        self.assertEquals(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_josephus2(self):
        self.assertEquals(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [2, 4, 6, 8, 10, 3, 7, 1, 9, 5])

    def test_josephus3(self):
        self.assertEquals(josephus(["C", "o", "d", "e", "W", "a", "r", "s"], 4),
                          ['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])

    def test_josephus4(self):
        self.assertEquals(josephus([1, 2, 3, 4, 5, 6, 7], 3), [3, 6, 2, 7, 5, 1, 4])

    def test_josephus5(self):
        self.assertEquals(josephus([], 3), [])


if __name__ == '__main__':
    print(josephus([True, False, True, False, True, False, True, False, True], 9))
    print("should be")
    print([True, True, True, False, False, True, False, True, False])
