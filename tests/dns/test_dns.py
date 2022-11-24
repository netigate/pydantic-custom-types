from unittest import TestCase
from pydantic_custom_types.dns import Hostname


class TestHostname(TestCase):
    def setUp(self) -> None:
        self.hn = Hostname

    def test_has_to_many_characters(self):
        case = "jsdklfjhsdkjlfhasjkldfhlkjhasdflkjhasdflkjhasdhdsfjklkjlhssdfhjkl"

        with self.assertRaises(ValueError):
            self.hn.has_to_many_characters(case)

    def test_start_end_with_dot(self):
        fail = [".asd", "asd."]

        for f in fail:
            with self.assertRaises(ValueError):
                self.hn.start_end_with_dot(f)

    def test_start_end_with_dash(self):
        fail = ["-asd", "asd-"]

        for f in fail:
            with self.assertRaises(ValueError):
                self.hn.start_end_with_dash(f)

    def test_validator(self):
        cases = ["myname", "name-space", "sup_as"]

        for c in cases:
            self.assertTrue(self.hn.validate(c))
