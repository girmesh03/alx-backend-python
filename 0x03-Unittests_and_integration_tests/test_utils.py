#!/usr/bin/env python3
""" Parameterize a unit test """

import unittest
from parameterized import parameterized
from utils import access_nested_map  # Import the function you're testing


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing nested map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result) -> None:
        """ Test access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)