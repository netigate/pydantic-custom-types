from unittest import TestCase
from pydantic import BaseModel
from pydantic.error_wrappers import ValidationError
from pydantic_custom_types.base_name import BaseName


class TestBaseName(TestCase):
    def setUp(self) -> None:
        self.bn = BaseName

    def test_with_pydantic_object_pass(self):
        class Case(BaseModel):
            name: BaseName

        case = "namespace"
        self.assertTrue(
            Case(name=case)
        )

    def test_pydantic_object_fail(self):
        class Case(BaseModel):
            name: BaseName

        case = "Namespace"
        with self.assertRaises(ValidationError):
            Case(name=case)

    def test_validate_pass(self):
        case = "namespace-99-name"
        self.assertTrue(
            self.bn.base_name_validate(case)
        )

    def test_is_string_pass(self):
        case = "aaskdj"
        self.assertTrue(
            self.bn.is_string(case)
        )

    def test_is_string_fail(self):
        case = 123
        with self.assertRaises(TypeError):
            self.bn.is_string(case)

    def test_is_empty_string_fail(self):
        case = ""
        with self.assertRaises(ValueError):
            self.bn.is_empty_string(case)

    def test_is_empty_string_pass(self):
        case = "asd"
        self.assertTrue(self.bn.is_empty_string(case))

    def test_has_upper_case_fail(self):
        cases = ["NAMESPACE", "Namespace", "namespacE"]
        for c in cases:
            with self.assertRaises(ValueError):
                self.bn.has_upper_case(c)

    def test_has_upper_case_pass(self):
        case = "namespace"
        self.assertTrue(self.bn.has_upper_case(case))

    def test_starts_with_number_fail(self):
        case = "9namespace"
        with self.assertRaises(ValueError):
            self.bn.starts_with_number(case)

    def test_starts_with_number_pass(self):
        case = "namespace"
        self.assertTrue(
            self.bn.starts_with_number(case)
        )

    def test_starts_with_dash_fail(self):
        case = "-namespace"
        with self.assertRaises(ValueError):
            self.bn.starts_with_dash(case)

    def test_starts_with_dash_pass(self):
        case = "namespace"
        self.assertTrue(
            self.bn.starts_with_dash(case)
        )

