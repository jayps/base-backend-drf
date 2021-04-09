import os
from unittest import mock

from rest_framework.test import APITestCase

from base_backend.utils.exceptions import EnvironmentVariableNotSetException
from base_backend.utils.utils import get_environment_variable


class GetEnvironmentVariableTestCase(APITestCase):
    @mock.patch.dict(os.environ, {"TEST_VAR": "TEST_VAL"})
    def test_get_environment_variable_success(self):
        val = get_environment_variable("TEST_VAR")
        assert val == "TEST_VAL"

    def test_get_environment_variable_default(self):
        val = get_environment_variable("TEST_VAR", default="DEFAULT_VAL")
        assert val == "DEFAULT_VAL"

    def test_get_environment_variable_exception(self):
        with self.assertRaises(EnvironmentVariableNotSetException):
            val = get_environment_variable("TEST_VAR")
