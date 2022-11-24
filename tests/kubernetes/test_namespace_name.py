from unittest import TestCase
from pydantic_custom_types.kubernetes import NamespaceName
from .util import randomword


class TestNamespaceName(TestCase):
    def setUp(self) -> None:
        self.nn = NamespaceName

    def test_has_to_many_characters(self):
        case = randomword(70)

        with self.assertRaises(ValueError):
            self.nn.has_to_many_characters(case)

    def test_has_dot(self):
        case = "asd.asd"

        with self.assertRaises(ValueError):
            self.nn.has_dot(case)
