from unittest.mock import patch
from unittest import TestCase

# import unittest
from howdoi import howdoi




# howdoi._get_result = MagicMock(return_value='-------response for test_answers')

# print(howdoi._get_result("url"))

@patch('howdoi._get_result', return_value="predefined return value")
def test(self, _get_result):
    # mock1.return_value = "predefined return value"

    print(howdoi.howdoi("declare a function"))

query = "declare a function in javascript"
output = howdoi.howdoi(query)

print(output)