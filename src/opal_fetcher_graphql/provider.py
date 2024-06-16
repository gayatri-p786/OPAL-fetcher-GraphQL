from typing import List, Optional

import graphql
from pydantic import BaseModel, Field

from opal_common.fetcher.fetch_provider import BaseFetchProvider
from opal_common.fetcher.events import FetcherConfig, FetchEvent
from opal_common.logger import logger


class GraphQLFetcherConfig(FetcherConfig):
    """
    Config for GraphQLFetchProvider, inherits from `FetcherConfig`.
    """
    fetcher: str = "GraphQLFetchProvider"
    graphql_endpoint: str = Field(..., description="The URL of the GraphQL endpoint")
    query: str = Field(..., description="The GraphQL query to fetch the data")
    variables: Optional[dict] = Field({}, description="Variables to be passed with the GraphQL query")


class GraphQLFetchEvent(FetchEvent):
    """
    A FetchEvent shape for the GraphQL Fetch Provider.
    """
    fetcher: str = "GraphQLFetchProvider"
    config: GraphQLFetcherConfig = None


class GraphQLFetchProvider(BaseFetchProvider):
    """
    An OPAL fetch provider for GraphQL.
    """

    def __init__(self, event: GraphQLFetchEvent) -> None:
        super().__init__(event)

    def parse_event(self, event: FetchEvent) -> GraphQLFetchEvent:
        return GraphQLFetchEvent(**event.dict(exclude={"config"}), config=event.config)

    async def _fetch_(self):
        """
        Fetches data from the GraphQL endpoint.
        """
        self._event: GraphQLFetchEvent

        try:
            # Create a GraphQL client
            client = graphql.client.Client()

            # Send the GraphQL query to the endpoint
            result = await client.execute(
                self._event.config.graphql_endpoint,
                self._event.config.query,
                variables=self._event.config.variables
            )

            return result
        except Exception as e:
            logger.error(f"Error fetching data from GraphQL API: {str(e)}")
            return None

    async def _process_(self, data):
        """
        Process the fetched data.
        """
        return data
