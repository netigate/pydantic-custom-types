import os
from unittest import TestCase
from pydantic_custom_types.active_directory import RealAdGroup


class TestRealAdGroup(TestCase):
    def setUp(self) -> None:
        os.environ["GROUPS_FILE"] = "files/groups.json"
        self.rg = RealAdGroup

    def test_validate(self):
        self.assertTrue(self.rg.validate("othergroup"))
        with self.assertRaises(ValueError):
            self.rg.validate("mygroup")
