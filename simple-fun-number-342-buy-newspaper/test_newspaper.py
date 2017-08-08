# coding=utf-8

from unittest import TestCase
from newspaper import buy_newspaper


class NewspaperTest(TestCase):
    def test_buy1(self):
        self.assertEqual(buy_newspaper("abc", "bcac"), 2)

    def test_buy2(self):
        self.assertEqual(buy_newspaper("abc", "xyz"), -1)

    def test_buy3(self):
        self.assertEqual(buy_newspaper("abc", "abcabc"), 2)

    def test_buy4(self):
        self.assertEqual(buy_newspaper("abc", "abccba"), 4)

    def test_buy5(self):
        self.assertEqual(buy_newspaper("abc", "aaaaaa"), 6)
