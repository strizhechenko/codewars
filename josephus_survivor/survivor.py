# coding=utf-8

from unittest import TestCase

"""
josephus_survivor(7,3) => means 7 people in a circle;
one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor!
"""


def josephus_survivor(n, k):
    index, people = 0, list(range(1, n + 1))
    while len(people) > 1:
        index = (index + k - 1) % len(people)
        people.pop(index)
    return people[0]


class JosephusTest(TestCase):
    def test_josephus1(self):
        self.assertEquals(josephus_survivor(7, 3), 4)

    def test_josephus2(self):
        self.assertEquals(josephus_survivor(11, 19), 10)

    def test_josephus3(self):
        self.assertEquals(josephus_survivor(1, 300), 1)

    def test_josephus4(self):
        self.assertEquals(josephus_survivor(14, 2), 13)

    def test_josephus5(self):
        self.assertEquals(josephus_survivor(100, 1), 100)


if __name__ == '__main__':
    josephus_survivor(7, 3)
