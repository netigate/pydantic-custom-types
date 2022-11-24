import os
from unittest import TestCase
from pydantic_custom_types.active_directory import RealAdUser


class TestRealAdUser(TestCase):
    def setUp(self) -> None:
        os.environ["USERS_FILE"] = "files/users.json"
        self.rd = RealAdUser

    def test_validate(self):
        self.assertTrue(self.rd.validate("john.doe@example.com"))
        with self.assertRaises(ValueError):
            self.rd.validate("doh.john@example.com")
