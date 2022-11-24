from unittest import TestCase
from pydantic_custom_types.kubernetes import SecretName

from tests.util import randomword


class TestNamespaceName(TestCase):
    def setUp(self) -> None:
        self.nn = SecretName

    def test_has_to_many_characters(self):
        case = randomword(300)

        with self.assertRaises(ValueError):
            self.nn.has_to_many_characters(case)

    def test_class(self):
        case = randomword(200)
        self.assertTrue(case)