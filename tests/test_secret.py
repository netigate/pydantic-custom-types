from random import choice
from string import ascii_lowercase
from unittest import TestCase
from pydantic import BaseModel
from pydantic.error_wrappers import ValidationError
from pydantic_custom_types.kubernetes import SecretName


class TestSecretName(TestCase):
    def setUp(self) -> None:
        self.sn = SecretName

    def test_with_pydantic_object_pass(self):
        class Case(BaseModel):
            name: SecretName

        self.assertTrue(
            Case(name="my-secret")
        )

    def test_with_pydantic_object_fail(self):
        class Case(BaseModel):
            name: SecretName

        with self.assertRaises(ValidationError):
            Case(name="my_secret")

    def test_has_to_many_characters_fail(self):
        case = "".join(choice(ascii_lowercase) for i in range(254))
        with self.assertRaises(ValueError):
            self.sn.has_to_many_characters(case)

    def test_has_to_many_characters_pass(self):
        case = "".join(choice(ascii_lowercase) for i in range(100))
        self.assertTrue(
            self.sn.has_to_many_characters(case)
        )
