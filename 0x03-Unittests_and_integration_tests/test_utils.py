#!/usr/bin/env python3
"""
Parametrize unit tests for various functions.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function with different inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that a KeyError is raised for certain inputs.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test cases for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """
        Test get_json function with different URLs and payloads.
        """
        class Mocked(Mock):
            """
            Mocked class to simulate requests.get response.
            """

            def json(self):
                """
                Return the mocked payload.
                """
                return payload

        with patch("requests.get") as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """
    Test cases for the memoize decorator.
    """

    def test_memoize(self):
        """
        Test memoize decorator.
        """

        class TestClass:
            """
            Test class to apply memoize decorator.
            """

            def a_method(self):
                """
                A method to be memoized.
                """
                return 42

            @memoize
            def a_property(self):
                """
                A memoized property.
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            test_instance = TestClass()
            test_instance.a_property
            test_instance.a_property
            mocked.assert_called_once()
