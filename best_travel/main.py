# coding=utf-8

from itertools import combinations
from unittest import TestCase


def choose_best_sum(max_distance, elements, distances):
    return max((sum(group) for group in combinations(distances, elements) if sum(group) <= max_distance), default=None)


class BestSumTest(TestCase):
    def test_sum(self):
        xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
        self.assertEquals(choose_best_sum(230, 4, xs), 230)
        self.assertEquals(choose_best_sum(430, 5, xs), 430)
        self.assertEquals(choose_best_sum(430, 8, xs), None)


if __name__ == '__main__':
    print(choose_best_sum(230, 4, [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]))
