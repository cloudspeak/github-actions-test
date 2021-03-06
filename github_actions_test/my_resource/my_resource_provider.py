from typing import Any

import pulumi
from pulumi.dynamic import CreateResult, UpdateResult

from ..base_dynamic_provider import BaseDynamicProvider


class MyResourceProvider(BaseDynamicProvider):
    """
    The provider for a MyResource resource.

    TODO: USE THIS TEMPLATE TO CREATE RESOURCE PROVIDERS FOR YOUR DYNAMIC PROVIDER.

    You should implement the `create`, `diff`, `update` and `delete` methods as
    necessary.  The `Provider` instance which is passed through the constructor should
    define the configuration used to communicate with the backend service.  It is made
    available by the base class through the
    `provider_params` attribute.

    See https://www.pulumi.com/docs/intro/concepts/programming-model/#dynamicproviders
    for more information.
    """

    def create(self, props: Any) -> CreateResult:

        pulumi.info(
            (
                f"Creating MyResource resource "
                f" (param1={props.get('param1')},param2={props.get('param2')})..."
            )
        )
        pulumi.info(
            (
                f"Using provider parameters ({self.provider_params.provider_param1},"
                f"{self.provider_params.provider_param2})"
            )
        )

        return CreateResult(
            id_="resource_id_12345", outs={**props, "output_param": "my_output_value"}
        )

    def update(self, _id: str, _olds: Any, _news: Any) -> UpdateResult:

        pulumi.info(
            (
                f"Updating MyResource[{_id}] to "
                f" (param1={_news.get('param1')},param2={_news.get('param2')})..."
            )
        )
        pulumi.info(
            (
                f"Using provider parameters ({self.provider_params.provider_param1},"
                f"{self.provider_params.provider_param2})"
            )
        )

        return UpdateResult(outs={**_news, "output_param": "my_output_value"})

    def delete(self, _id: str, _props: Any) -> None:
        pulumi.info(f"Deleting MyResource[{_id}]")
        pulumi.info(
            (
                f"Using provider parameters ({self.provider_params.provider_param1},"
                f"{self.provider_params.provider_param2})"
            )
        )
