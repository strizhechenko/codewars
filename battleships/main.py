# coding=utf-8

from unittest import TestCase
from collections import Counter
from functools import reduce
from operator import add


def print_board(board, label):
    print()
    print("# ", label)
    for row in board:
        print(row)
    for k, v in Counter(reduce(add, board)).items():
        print("{0}: {1}".format(k, v))


def damaged_or_sunk(board, attacks):
    result = {
        "sunk": 0,
        "damaged": 0,
        "not_touched": 0,
        "points": 0,
    }
    print_board(board, "before")
    for x, row in attacks:
        if board[row - 1][x - 1] != 0:
            board[row - 1][x - 1] = 'd'
        else:
            result['not_touched'] += 1
    print_board(board, "after")
    return result


class BattleShipTest(TestCase):
    def test_simple(self):
        board = [[0, 0, 1, 0],
                 [0, 0, 1, 0],
                 [0, 0, 1, 0]]

        attacks = [[3, 1], [3, 2], [3, 3]]
        result = damaged_or_sunk(board, attacks)
        print("Game 1 result expected: { 'sunk': 1, 'damaged': 0 , 'not_touched': 0, 'points': 1}")
        print("Game 1 result occured: ", result)
        # self.assertEquals(result['sunk'], 1)
        # self.assertEquals(result['damaged'], 0)
        # self.assertEquals(result['not_touched'], 0)
        # self.assertEquals(result['points'], 1)

    def test_hard(self):
        board = [[3, 0, 1],
                 [3, 0, 1],
                 [0, 2, 1],
                 [0, 2, 0]]
        attacks = [[2, 1], [2, 2], [3, 2], [3, 3]]
        result = damaged_or_sunk(board, attacks)
        print("Game 2 result: { 'sunk': 1, 'damaged': 1 , 'not_touched': 1, 'points': 0.5}")
        self.assertEquals(result['sunk'], 1)
        self.assertEquals(result['damaged'], 1)
        self.assertEquals(result['not_touched'], 1)
        self.assertEquals(result['points'], 0.5)


if __name__ == '__main__':
    BattleShipTest().test_simple()
