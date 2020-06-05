import unittest

from github_actions_test.my_resource.my_resource_provider import MyResourceProvider


class MyResourceProviderProviderTests(unittest.TestCase):
    """
    Unit tests for the MyResourceProvider class
    """
    def test_outputs_are_set(self):
        provider = MockProvider(provider_param1="value1", provider_param2="value2")
        my_resource_provider = MyResourceProvider(provider)

        result = my_resource_provider.create({"param1": "123", "param2": "456"})

        self.assertDictEqual(
            result.outs,
            {"param1": "123", "param2": "456", "output_param": "my_output_value"},
        )


class MockProvider:
    """
    Mock for Provider class
    """
    def __init__(self, provider_param1, provider_param2):
        self.provider_param1 = provider_param1
        self.provider_param2 = provider_param2
