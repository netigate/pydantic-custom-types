from random import choice
from string import ascii_lowercase
from unittest import TestCase
from pydantic import BaseModel
from pydantic.error_wrappers import ValidationError

from pydantic_custom_types.kubernetes import NamespaceName


class TestNamespaceName(TestCase):
    def setUp(self) -> None:
        self.nn = NamespaceName

    def test_with_pydantic_object_pass(self):
        class Case(BaseModel):
            name: NamespaceName

        self.assertTrue(
            Case(name="my-secret")
        )

    def test_with_pydantic_object_fail(self):
        class Case(BaseModel):
            name: NamespaceName

        with self.assertRaises(ValidationError):
            Case(name="my_secret")

    def test_has_to_many_characters_fail(self):
        case = "".join(choice(ascii_lowercase) for i in range(64))
        with self.assertRaises(ValueError):
            self.nn.has_to_many_characters(case)

    def test_has_to_many_characters_pass(self):
        case = "".join(choice(ascii_lowercase) for i in range(40))
        self.assertTrue(
            self.nn.has_to_many_characters(case)
        )
