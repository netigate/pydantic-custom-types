from unittest import TestCase
from pydantic_custom_types.ip import Ipv4Address


class TestIpv4Address(TestCase):
    def setUp(self) -> None:
        self.v4 = Ipv4Address

    def test_fail(self):
        cases = ["10.10.10.300", "09.10.10.10", "190.80.500.1"]

        for c in cases:
            with self.assertRaises(OSError):
                self.v4.validate(c)

    def test_pass(self):
        cases = ["192.168.0.2", "10.0.0.1", "80.34.2.1"]

        for c in cases:
            self.v4.validate(c)