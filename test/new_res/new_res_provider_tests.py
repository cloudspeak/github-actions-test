import unittest

from github_actions_test.new_res.new_res_provider import NewResProvider


class NewResProviderProviderTests(unittest.TestCase):
    def test_outputs_are_set(self):
        provider = MockProvider(provider_param1="value1", provider_param2="value2")
        new_res_provider = NewResProvider(provider)

        result = new_res_provider.create({"param1": "123", "param2": "456"})

        self.assertDictEqual(
            result.outs,
            {"param1": "123", "param2": "456", "output_param": "my_output_value"},
        )


class MockProvider:
    def __init__(self, provider_param1, provider_param2):
        self.provider_param1 = provider_param1
        self.provider_param2 = provider_param2