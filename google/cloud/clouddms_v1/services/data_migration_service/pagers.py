# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
)

from google.cloud.clouddms_v1.types import (
    clouddms,
    clouddms_resources,
    conversionworkspace_resources,
)


class ListMigrationJobsPager:
    """A pager for iterating through ``list_migration_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.clouddms_v1.types.ListMigrationJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``migration_jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMigrationJobs`` requests and continue to iterate
    through the ``migration_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.clouddms_v1.types.ListMigrationJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., clouddms.ListMigrationJobsResponse],
        request: clouddms.ListMigrationJobsRequest,
        response: clouddms.ListMigrationJobsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.clouddms_v1.types.ListMigrationJobsRequest):
                The initial request object.
            response (google.cloud.clouddms_v1.types.ListMigrationJobsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = clouddms.ListMigrationJobsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[clouddms.ListMigrationJobsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[clouddms_resources.MigrationJob]:
        for page in self.pages:
            yield from page.migration_jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMigrationJobsAsyncPager:
    """A pager for iterating through ``list_migration_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.clouddms_v1.types.ListMigrationJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``migration_jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMigrationJobs`` requests and continue to iterate
    through the ``migration_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.clouddms_v1.types.ListMigrationJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[clouddms.ListMigrationJobsResponse]],
        request: clouddms.ListMigrationJobsRequest,
        response: clouddms.ListMigrationJobsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.clouddms_v1.types.ListMigrationJobsRequest):
                The initial request object.
            response (google.cloud.clouddms_v1.types.ListMigrationJobsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = clouddms.ListMigrationJobsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[clouddms.ListMigrationJobsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[clouddms_resources.MigrationJob]:
        async def async_generator():
            async for page in self.pages:
                for response in page.migration_jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConnectionProfilesPager:
    """A pager for iterating through ``list_connection_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.clouddms_v1.types.ListConnectionProfilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``connection_profiles`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConnectionProfiles`` requests and continue to iterate
    through the ``connection_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.clouddms_v1.types.ListConnectionProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., clouddms.ListConnectionProfilesResponse],
        request: clouddms.ListConnectionProfilesRequest,
        response: clouddms.ListConnectionProfilesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.clouddms_v1.types.ListConnectionProfilesRequest):
                The initial request object.
            response (google.cloud.clouddms_v1.types.ListConnectionProfilesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = clouddms.ListConnectionProfilesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[clouddms.ListConnectionProfilesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[clouddms_resources.ConnectionProfile]:
        for page in self.pages:
            yield from page.connection_profiles

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConnectionProfilesAsyncPager:
    """A pager for iterating through ``list_connection_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.clouddms_v1.types.ListConnectionProfilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``connection_profiles`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConnectionProfiles`` requests and continue to iterate
    through the ``connection_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.clouddms_v1.types.ListConnectionProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[clouddms.ListConnectionProfilesResponse]],
        request: clouddms.ListConnectionProfilesRequest,
        response: clouddms.ListConnectionProfilesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.clouddms_v1.types.ListConnectionProfilesRequest):
                The initial request object.
            response (google.cloud.clouddms_v1.types.ListConnectionProfilesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = clouddms.ListConnectionProfilesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[clouddms.ListConnectionProfilesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[clouddms_resources.ConnectionProfile]:
        async def async_generator():
            async for page in self.pages:
                for response in page.connection_profiles:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPrivateConnectionsPager:
    """A pager for iterating through ``list_private_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.clouddms_v1.types.ListPrivateConnectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``private_connections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPrivateConnections`` requests and continue to iterate
    through the ``private_connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.clouddms_v1.types.ListPrivateConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., clouddms.ListPrivateConnectionsResponse],
        request: clouddms.ListPrivateConnectionsRequest,
        response: clouddms.ListPrivateConnectionsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.clouddms_v1.types.ListPrivateConnectionsRequest):
                The initial request object.
            response (google.cloud.clouddms_v1.types.ListPrivateConnectionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = clouddms.ListPrivateConnectionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[clouddms.ListPrivateConnectionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[clouddms_resources.PrivateConnection]:
        for page in self.pages:
            yield from page.private_connections

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPrivateConnectionsAsyncPager:
    """A pager for iterating through ``list_private_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.clouddms_v1.types.ListPrivateConnectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``private_connections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPrivateConnections`` requests and continue to iterate
    through the ``private_connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.clouddms_v1.types.ListPrivateConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[clouddms.ListPrivateConnectionsResponse]],
        request: clouddms.ListPrivateConnectionsRequest,
        response: clouddms.ListPrivateConnectionsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.clouddms_v1.types.ListPrivateConnectionsRequest):
                The initial request object.
            response (google.cloud.clouddms_v1.types.ListPrivateConnectionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = clouddms.ListPrivateConnectionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[clouddms.ListPrivateConnectionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[clouddms_resources.PrivateConnection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.private_connections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConversionWorkspacesPager:
    """A pager for iterating through ``list_conversion_workspaces`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.clouddms_v1.types.ListConversionWorkspacesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``conversion_workspaces`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConversionWorkspaces`` requests and continue to iterate
    through the ``conversion_workspaces`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.clouddms_v1.types.ListConversionWorkspacesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., clouddms.ListConversionWorkspacesResponse],
        request: clouddms.ListConversionWorkspacesRequest,
        response: clouddms.ListConversionWorkspacesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.clouddms_v1.types.ListConversionWorkspacesRequest):
                The initial request object.
            response (google.cloud.clouddms_v1.types.ListConversionWorkspacesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = clouddms.ListConversionWorkspacesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[clouddms.ListConversionWorkspacesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[conversionworkspace_resources.ConversionWorkspace]:
        for page in self.pages:
            yield from page.conversion_workspaces

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConversionWorkspacesAsyncPager:
    """A pager for iterating through ``list_conversion_workspaces`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.clouddms_v1.types.ListConversionWorkspacesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``conversion_workspaces`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConversionWorkspaces`` requests and continue to iterate
    through the ``conversion_workspaces`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.clouddms_v1.types.ListConversionWorkspacesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[clouddms.ListConversionWorkspacesResponse]],
        request: clouddms.ListConversionWorkspacesRequest,
        response: clouddms.ListConversionWorkspacesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.clouddms_v1.types.ListConversionWorkspacesRequest):
                The initial request object.
            response (google.cloud.clouddms_v1.types.ListConversionWorkspacesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = clouddms.ListConversionWorkspacesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[clouddms.ListConversionWorkspacesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(
        self,
    ) -> AsyncIterator[conversionworkspace_resources.ConversionWorkspace]:
        async def async_generator():
            async for page in self.pages:
                for response in page.conversion_workspaces:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class DescribeDatabaseEntitiesPager:
    """A pager for iterating through ``describe_database_entities`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.clouddms_v1.types.DescribeDatabaseEntitiesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``database_entities`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``DescribeDatabaseEntities`` requests and continue to iterate
    through the ``database_entities`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.clouddms_v1.types.DescribeDatabaseEntitiesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., clouddms.DescribeDatabaseEntitiesResponse],
        request: clouddms.DescribeDatabaseEntitiesRequest,
        response: clouddms.DescribeDatabaseEntitiesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.clouddms_v1.types.DescribeDatabaseEntitiesRequest):
                The initial request object.
            response (google.cloud.clouddms_v1.types.DescribeDatabaseEntitiesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = clouddms.DescribeDatabaseEntitiesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[clouddms.DescribeDatabaseEntitiesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[conversionworkspace_resources.DatabaseEntity]:
        for page in self.pages:
            yield from page.database_entities

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class DescribeDatabaseEntitiesAsyncPager:
    """A pager for iterating through ``describe_database_entities`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.clouddms_v1.types.DescribeDatabaseEntitiesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``database_entities`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``DescribeDatabaseEntities`` requests and continue to iterate
    through the ``database_entities`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.clouddms_v1.types.DescribeDatabaseEntitiesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[clouddms.DescribeDatabaseEntitiesResponse]],
        request: clouddms.DescribeDatabaseEntitiesRequest,
        response: clouddms.DescribeDatabaseEntitiesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.clouddms_v1.types.DescribeDatabaseEntitiesRequest):
                The initial request object.
            response (google.cloud.clouddms_v1.types.DescribeDatabaseEntitiesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = clouddms.DescribeDatabaseEntitiesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[clouddms.DescribeDatabaseEntitiesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[conversionworkspace_resources.DatabaseEntity]:
        async def async_generator():
            async for page in self.pages:
                for response in page.database_entities:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchStaticIpsPager:
    """A pager for iterating through ``fetch_static_ips`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.clouddms_v1.types.FetchStaticIpsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``static_ips`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchStaticIps`` requests and continue to iterate
    through the ``static_ips`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.clouddms_v1.types.FetchStaticIpsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., clouddms.FetchStaticIpsResponse],
        request: clouddms.FetchStaticIpsRequest,
        response: clouddms.FetchStaticIpsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.clouddms_v1.types.FetchStaticIpsRequest):
                The initial request object.
            response (google.cloud.clouddms_v1.types.FetchStaticIpsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = clouddms.FetchStaticIpsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[clouddms.FetchStaticIpsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[str]:
        for page in self.pages:
            yield from page.static_ips

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchStaticIpsAsyncPager:
    """A pager for iterating through ``fetch_static_ips`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.clouddms_v1.types.FetchStaticIpsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``static_ips`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchStaticIps`` requests and continue to iterate
    through the ``static_ips`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.clouddms_v1.types.FetchStaticIpsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[clouddms.FetchStaticIpsResponse]],
        request: clouddms.FetchStaticIpsRequest,
        response: clouddms.FetchStaticIpsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.clouddms_v1.types.FetchStaticIpsRequest):
                The initial request object.
            response (google.cloud.clouddms_v1.types.FetchStaticIpsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = clouddms.FetchStaticIpsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[clouddms.FetchStaticIpsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[str]:
        async def async_generator():
            async for page in self.pages:
                for response in page.static_ips:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
