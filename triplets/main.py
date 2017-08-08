# coding=utf-8

from unittest import TestCase, skip
from operator import add
from functools import reduce
from itertools import combinations
from copy import deepcopy

SOLUTION = [
    [['t', 'u', 'p'],
     ['w', 'h', 'i'],
     ['t', 's', 'u'],
     ['a', 't', 's'],
     ['h', 'a', 'p'],
     ['t', 'i', 's'],
     ['w', 'h', 's']],

    # 1 - w
    [['t', 'u', 'p'],
     ['h', 'i'],
     ['t', 's', 'u'],
     ['a', 't', 's'],
     ['h', 'a', 'p'],
     ['t', 'i', 's'],
     ['h', 's']],

    # 2 - wh
    [['t', 'u', 'p'],
     ['i'],
     ['t', 's', 'u'],
     ['a', 't', 's'],
     ['a', 'p'],
     ['t', 'i', 's'],
     ['s']],

    # 3 - wha
    [['t', 'u', 'p'],
     ['i'],
     ['t', 's', 'u'],
     ['t', 's'],
     ['p'],
     ['t', 'i', 's'],
     ['s']],

    # 4 - what
    [['u', 'p'],
     ['i'],
     ['s', 'u'],
     ['p'],
     ['i', 's'],
     ['s']],

    # 5 - whati
    [['u', 'p'],
     ['s', 'u'],
     ['p'],
     ['s']],

    # 6 - whatis
    [['u', 'p'],
     ['u'],
     ['p']],

    # 7 - whatisu
    [['p']],

    # 8 - whatisup
]


def debug(f=None, n=None, t=None):
    print("--------------")
    if f:
        print("first row symbols:", f)
    if n:
        print("next row symbols:", n)
    if t:
        for triplet in t:
            print(triplet)


def next_symbol(triplets):
    first_row = set([a[0] for a in triplets])
    next_rows = [a[1:] for a in triplets if len(a) > 1]
    if not next_rows:
        return list(first_row)[0]
    next_symbols = set(reduce(add, next_rows))
    # debug(first_row, next_symbols, triplets)
    return list(first_row - next_symbols)[0]


def cleanup(triplets, symbol):
    for triplet in triplets:
        if symbol in triplet:
            triplet.remove(symbol)
        combines = list(combinations(triplets, 2))
        matches = [l == r for l, r in combines if triplet in (l, r)]
        while any(matches):
            triplets.remove(triplet)
            combines = list(combinations(triplets, 2))
            matches = [l == r for l, r in combines if triplet in (l, r)]
    return [triplet for triplet in triplets if triplet]


def recoverSecret(triplets):
    """ triplets is a list of triplets from the secrent string. Return the string. """
    secret = ""
    attempt = 0
    test = TestCase()
    while triplets:
        symbol = next_symbol(triplets)
        secret += symbol
        test.assertEquals(triplets, SOLUTION[attempt])
        data_before = ("cleanup", deepcopy(triplets), symbol)
        triplets = cleanup(triplets, symbol)
        data_after = ("cleanup", deepcopy(triplets), symbol)
        attempt += 1

        try:
            test.assertEquals(triplets, SOLUTION[attempt])
        except AssertionError as err:
            debug(t=triplets)
            print(secret, attempt)
            print("data_before", data_before)
            print("data_after", data_after)
            raise err
    return secret


class TripletsTests(TestCase):
    @skip
    def test_cleanup1(self):
        expected = [['u', 'p'], ['u'], ['p']]
        input_data = [['u', 'p'], ['s', 'u'], ['s'], ['p'], ['s'], ['s']]
        output = cleanup(input_data, 's')
        self.assertEquals(output, expected)

    def test_cleanup2(self):
        expected = [['p']]
        input_data = [['u', 'p'], ['u'], ['p']]
        output = cleanup(input_data, 'u')
        self.assertEquals(output, expected)

    @skip
    def test_whatisup(self):
        secret = "whatisup"
        triplets = [
            ['t', 'u', 'p'],
            ['w', 'h', 'i'],
            ['t', 's', 'u'],
            ['a', 't', 's'],
            ['h', 'a', 'p'],
            ['t', 'i', 's'],
            ['w', 'h', 's']
        ]
        print(recoverSecret(triplets))
        # self.assertEquals(recoverSecret(triplets), secret)


if __name__ == '__main__':
    TripletsTests().test_whatisup()
