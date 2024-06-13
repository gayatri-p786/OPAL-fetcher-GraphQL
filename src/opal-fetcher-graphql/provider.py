from pydantic import BaseModel, Field

from opal_common.fetcher.fetch_provider import BaseFetchProvider
from opal_common.fetcher.events import FetcherConfig, FetchEvent


class GraphQLFetcherConfig(FetcherConfig):
    """
    Config for GraphQLFetchProvider, inherits from `FetcherConfig`.
    * In your own class, you must set the value of the `fetcher` key to be your custom provider class name.
    """
    fetcher: str = "GraphQLFetchProvider"


class GraphQLFetchEvent(FetchEvent):
    """
    When writing a custom provider, you must create a custom FetchEvent subclass, just like this class.
    In your own class, you must:
    * set the value of the `fetcher` key to be your custom provider class name.
    * set the type of the `config` key to be your custom config class (the one just above).
    """
    fetcher: str = "GraphQLFetchProvider"
    config: GraphQLFetcherConfig = None


class GraphQLFetchProvider(BaseFetchProvider):
    """
    The fetch-provider logic, must inherit from `BaseFetchProvider`.
    """
    ...
