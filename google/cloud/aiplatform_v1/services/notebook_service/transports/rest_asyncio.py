# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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

import google.auth

try:
    import aiohttp  # type: ignore
    from google.auth.aio.transport.sessions import AsyncAuthorizedSession  # type: ignore
    from google.api_core import rest_streaming_async  # type: ignore
    from google.api_core.operations_v1 import AsyncOperationsRestClient  # type: ignore
except ImportError as e:  # pragma: NO COVER
    raise ImportError(
        "`rest_asyncio` transport requires the library to be installed with the `async_rest` extra. Install the library with the `async_rest` extra using `pip install google-cloud-aiplatform[async_rest]`"
    ) from e

from google.auth.aio import credentials as ga_credentials_async  # type: ignore

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import operations_v1
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.api_core import retry_async as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming_async  # type: ignore
import google.protobuf

from google.protobuf import json_format
from google.api_core import operations_v1
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore

import json  # type: ignore
import dataclasses
from typing import Any, Dict, List, Callable, Tuple, Optional, Sequence, Union


from google.cloud.aiplatform_v1.types import notebook_execution_job
from google.cloud.aiplatform_v1.types import notebook_runtime
from google.cloud.aiplatform_v1.types import notebook_service
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseNotebookServiceRestTransport

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


import logging

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"google-auth@{google.auth.__version__}",
)

if hasattr(DEFAULT_CLIENT_INFO, "protobuf_runtime_version"):  # pragma: NO COVER
    DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class AsyncNotebookServiceRestInterceptor:
    """Asynchronous Interceptor for NotebookService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AsyncNotebookServiceRestTransport.

    .. code-block:: python
        class MyCustomNotebookServiceInterceptor(NotebookServiceRestInterceptor):
            async def pre_assign_notebook_runtime(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_assign_notebook_runtime(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_create_notebook_execution_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_create_notebook_execution_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_create_notebook_runtime_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_create_notebook_runtime_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_delete_notebook_execution_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_delete_notebook_execution_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_delete_notebook_runtime(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_delete_notebook_runtime(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_delete_notebook_runtime_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_delete_notebook_runtime_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_get_notebook_execution_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_get_notebook_execution_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_get_notebook_runtime(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_get_notebook_runtime(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_get_notebook_runtime_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_get_notebook_runtime_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_list_notebook_execution_jobs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_list_notebook_execution_jobs(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_list_notebook_runtimes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_list_notebook_runtimes(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_list_notebook_runtime_templates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_list_notebook_runtime_templates(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_start_notebook_runtime(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_start_notebook_runtime(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_stop_notebook_runtime(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_stop_notebook_runtime(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_update_notebook_runtime_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_update_notebook_runtime_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_upgrade_notebook_runtime(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_upgrade_notebook_runtime(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AsyncNotebookServiceRestTransport(interceptor=MyCustomNotebookServiceInterceptor())
        client = async NotebookServiceClient(transport=transport)


    """

    async def pre_assign_notebook_runtime(
        self,
        request: notebook_service.AssignNotebookRuntimeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.AssignNotebookRuntimeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for assign_notebook_runtime

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_assign_notebook_runtime(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for assign_notebook_runtime

        DEPRECATED. Please use the `post_assign_notebook_runtime_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_assign_notebook_runtime` interceptor runs
        before the `post_assign_notebook_runtime_with_metadata` interceptor.
        """
        return response

    async def post_assign_notebook_runtime_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for assign_notebook_runtime

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_assign_notebook_runtime_with_metadata`
        interceptor in new development instead of the `post_assign_notebook_runtime` interceptor.
        When both interceptors are used, this `post_assign_notebook_runtime_with_metadata` interceptor runs after the
        `post_assign_notebook_runtime` interceptor. The (possibly modified) response returned by
        `post_assign_notebook_runtime` will be passed to
        `post_assign_notebook_runtime_with_metadata`.
        """
        return response, metadata

    async def pre_create_notebook_execution_job(
        self,
        request: notebook_service.CreateNotebookExecutionJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.CreateNotebookExecutionJobRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_notebook_execution_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_create_notebook_execution_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_notebook_execution_job

        DEPRECATED. Please use the `post_create_notebook_execution_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_create_notebook_execution_job` interceptor runs
        before the `post_create_notebook_execution_job_with_metadata` interceptor.
        """
        return response

    async def post_create_notebook_execution_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_notebook_execution_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_create_notebook_execution_job_with_metadata`
        interceptor in new development instead of the `post_create_notebook_execution_job` interceptor.
        When both interceptors are used, this `post_create_notebook_execution_job_with_metadata` interceptor runs after the
        `post_create_notebook_execution_job` interceptor. The (possibly modified) response returned by
        `post_create_notebook_execution_job` will be passed to
        `post_create_notebook_execution_job_with_metadata`.
        """
        return response, metadata

    async def pre_create_notebook_runtime_template(
        self,
        request: notebook_service.CreateNotebookRuntimeTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.CreateNotebookRuntimeTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_notebook_runtime_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_create_notebook_runtime_template(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_notebook_runtime_template

        DEPRECATED. Please use the `post_create_notebook_runtime_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_create_notebook_runtime_template` interceptor runs
        before the `post_create_notebook_runtime_template_with_metadata` interceptor.
        """
        return response

    async def post_create_notebook_runtime_template_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_notebook_runtime_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_create_notebook_runtime_template_with_metadata`
        interceptor in new development instead of the `post_create_notebook_runtime_template` interceptor.
        When both interceptors are used, this `post_create_notebook_runtime_template_with_metadata` interceptor runs after the
        `post_create_notebook_runtime_template` interceptor. The (possibly modified) response returned by
        `post_create_notebook_runtime_template` will be passed to
        `post_create_notebook_runtime_template_with_metadata`.
        """
        return response, metadata

    async def pre_delete_notebook_execution_job(
        self,
        request: notebook_service.DeleteNotebookExecutionJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.DeleteNotebookExecutionJobRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_notebook_execution_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_delete_notebook_execution_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_notebook_execution_job

        DEPRECATED. Please use the `post_delete_notebook_execution_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_delete_notebook_execution_job` interceptor runs
        before the `post_delete_notebook_execution_job_with_metadata` interceptor.
        """
        return response

    async def post_delete_notebook_execution_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_notebook_execution_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_delete_notebook_execution_job_with_metadata`
        interceptor in new development instead of the `post_delete_notebook_execution_job` interceptor.
        When both interceptors are used, this `post_delete_notebook_execution_job_with_metadata` interceptor runs after the
        `post_delete_notebook_execution_job` interceptor. The (possibly modified) response returned by
        `post_delete_notebook_execution_job` will be passed to
        `post_delete_notebook_execution_job_with_metadata`.
        """
        return response, metadata

    async def pre_delete_notebook_runtime(
        self,
        request: notebook_service.DeleteNotebookRuntimeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.DeleteNotebookRuntimeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_notebook_runtime

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_delete_notebook_runtime(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_notebook_runtime

        DEPRECATED. Please use the `post_delete_notebook_runtime_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_delete_notebook_runtime` interceptor runs
        before the `post_delete_notebook_runtime_with_metadata` interceptor.
        """
        return response

    async def post_delete_notebook_runtime_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_notebook_runtime

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_delete_notebook_runtime_with_metadata`
        interceptor in new development instead of the `post_delete_notebook_runtime` interceptor.
        When both interceptors are used, this `post_delete_notebook_runtime_with_metadata` interceptor runs after the
        `post_delete_notebook_runtime` interceptor. The (possibly modified) response returned by
        `post_delete_notebook_runtime` will be passed to
        `post_delete_notebook_runtime_with_metadata`.
        """
        return response, metadata

    async def pre_delete_notebook_runtime_template(
        self,
        request: notebook_service.DeleteNotebookRuntimeTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.DeleteNotebookRuntimeTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_notebook_runtime_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_delete_notebook_runtime_template(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_notebook_runtime_template

        DEPRECATED. Please use the `post_delete_notebook_runtime_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_delete_notebook_runtime_template` interceptor runs
        before the `post_delete_notebook_runtime_template_with_metadata` interceptor.
        """
        return response

    async def post_delete_notebook_runtime_template_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_notebook_runtime_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_delete_notebook_runtime_template_with_metadata`
        interceptor in new development instead of the `post_delete_notebook_runtime_template` interceptor.
        When both interceptors are used, this `post_delete_notebook_runtime_template_with_metadata` interceptor runs after the
        `post_delete_notebook_runtime_template` interceptor. The (possibly modified) response returned by
        `post_delete_notebook_runtime_template` will be passed to
        `post_delete_notebook_runtime_template_with_metadata`.
        """
        return response, metadata

    async def pre_get_notebook_execution_job(
        self,
        request: notebook_service.GetNotebookExecutionJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.GetNotebookExecutionJobRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_notebook_execution_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_get_notebook_execution_job(
        self, response: notebook_execution_job.NotebookExecutionJob
    ) -> notebook_execution_job.NotebookExecutionJob:
        """Post-rpc interceptor for get_notebook_execution_job

        DEPRECATED. Please use the `post_get_notebook_execution_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_get_notebook_execution_job` interceptor runs
        before the `post_get_notebook_execution_job_with_metadata` interceptor.
        """
        return response

    async def post_get_notebook_execution_job_with_metadata(
        self,
        response: notebook_execution_job.NotebookExecutionJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_execution_job.NotebookExecutionJob,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_notebook_execution_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_get_notebook_execution_job_with_metadata`
        interceptor in new development instead of the `post_get_notebook_execution_job` interceptor.
        When both interceptors are used, this `post_get_notebook_execution_job_with_metadata` interceptor runs after the
        `post_get_notebook_execution_job` interceptor. The (possibly modified) response returned by
        `post_get_notebook_execution_job` will be passed to
        `post_get_notebook_execution_job_with_metadata`.
        """
        return response, metadata

    async def pre_get_notebook_runtime(
        self,
        request: notebook_service.GetNotebookRuntimeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.GetNotebookRuntimeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_notebook_runtime

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_get_notebook_runtime(
        self, response: notebook_runtime.NotebookRuntime
    ) -> notebook_runtime.NotebookRuntime:
        """Post-rpc interceptor for get_notebook_runtime

        DEPRECATED. Please use the `post_get_notebook_runtime_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_get_notebook_runtime` interceptor runs
        before the `post_get_notebook_runtime_with_metadata` interceptor.
        """
        return response

    async def post_get_notebook_runtime_with_metadata(
        self,
        response: notebook_runtime.NotebookRuntime,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_runtime.NotebookRuntime, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_notebook_runtime

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_get_notebook_runtime_with_metadata`
        interceptor in new development instead of the `post_get_notebook_runtime` interceptor.
        When both interceptors are used, this `post_get_notebook_runtime_with_metadata` interceptor runs after the
        `post_get_notebook_runtime` interceptor. The (possibly modified) response returned by
        `post_get_notebook_runtime` will be passed to
        `post_get_notebook_runtime_with_metadata`.
        """
        return response, metadata

    async def pre_get_notebook_runtime_template(
        self,
        request: notebook_service.GetNotebookRuntimeTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.GetNotebookRuntimeTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_notebook_runtime_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_get_notebook_runtime_template(
        self, response: notebook_runtime.NotebookRuntimeTemplate
    ) -> notebook_runtime.NotebookRuntimeTemplate:
        """Post-rpc interceptor for get_notebook_runtime_template

        DEPRECATED. Please use the `post_get_notebook_runtime_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_get_notebook_runtime_template` interceptor runs
        before the `post_get_notebook_runtime_template_with_metadata` interceptor.
        """
        return response

    async def post_get_notebook_runtime_template_with_metadata(
        self,
        response: notebook_runtime.NotebookRuntimeTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_runtime.NotebookRuntimeTemplate,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_notebook_runtime_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_get_notebook_runtime_template_with_metadata`
        interceptor in new development instead of the `post_get_notebook_runtime_template` interceptor.
        When both interceptors are used, this `post_get_notebook_runtime_template_with_metadata` interceptor runs after the
        `post_get_notebook_runtime_template` interceptor. The (possibly modified) response returned by
        `post_get_notebook_runtime_template` will be passed to
        `post_get_notebook_runtime_template_with_metadata`.
        """
        return response, metadata

    async def pre_list_notebook_execution_jobs(
        self,
        request: notebook_service.ListNotebookExecutionJobsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.ListNotebookExecutionJobsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_notebook_execution_jobs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_list_notebook_execution_jobs(
        self, response: notebook_service.ListNotebookExecutionJobsResponse
    ) -> notebook_service.ListNotebookExecutionJobsResponse:
        """Post-rpc interceptor for list_notebook_execution_jobs

        DEPRECATED. Please use the `post_list_notebook_execution_jobs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_list_notebook_execution_jobs` interceptor runs
        before the `post_list_notebook_execution_jobs_with_metadata` interceptor.
        """
        return response

    async def post_list_notebook_execution_jobs_with_metadata(
        self,
        response: notebook_service.ListNotebookExecutionJobsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.ListNotebookExecutionJobsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_notebook_execution_jobs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_list_notebook_execution_jobs_with_metadata`
        interceptor in new development instead of the `post_list_notebook_execution_jobs` interceptor.
        When both interceptors are used, this `post_list_notebook_execution_jobs_with_metadata` interceptor runs after the
        `post_list_notebook_execution_jobs` interceptor. The (possibly modified) response returned by
        `post_list_notebook_execution_jobs` will be passed to
        `post_list_notebook_execution_jobs_with_metadata`.
        """
        return response, metadata

    async def pre_list_notebook_runtimes(
        self,
        request: notebook_service.ListNotebookRuntimesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.ListNotebookRuntimesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_notebook_runtimes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_list_notebook_runtimes(
        self, response: notebook_service.ListNotebookRuntimesResponse
    ) -> notebook_service.ListNotebookRuntimesResponse:
        """Post-rpc interceptor for list_notebook_runtimes

        DEPRECATED. Please use the `post_list_notebook_runtimes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_list_notebook_runtimes` interceptor runs
        before the `post_list_notebook_runtimes_with_metadata` interceptor.
        """
        return response

    async def post_list_notebook_runtimes_with_metadata(
        self,
        response: notebook_service.ListNotebookRuntimesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.ListNotebookRuntimesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_notebook_runtimes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_list_notebook_runtimes_with_metadata`
        interceptor in new development instead of the `post_list_notebook_runtimes` interceptor.
        When both interceptors are used, this `post_list_notebook_runtimes_with_metadata` interceptor runs after the
        `post_list_notebook_runtimes` interceptor. The (possibly modified) response returned by
        `post_list_notebook_runtimes` will be passed to
        `post_list_notebook_runtimes_with_metadata`.
        """
        return response, metadata

    async def pre_list_notebook_runtime_templates(
        self,
        request: notebook_service.ListNotebookRuntimeTemplatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.ListNotebookRuntimeTemplatesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_notebook_runtime_templates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_list_notebook_runtime_templates(
        self, response: notebook_service.ListNotebookRuntimeTemplatesResponse
    ) -> notebook_service.ListNotebookRuntimeTemplatesResponse:
        """Post-rpc interceptor for list_notebook_runtime_templates

        DEPRECATED. Please use the `post_list_notebook_runtime_templates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_list_notebook_runtime_templates` interceptor runs
        before the `post_list_notebook_runtime_templates_with_metadata` interceptor.
        """
        return response

    async def post_list_notebook_runtime_templates_with_metadata(
        self,
        response: notebook_service.ListNotebookRuntimeTemplatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.ListNotebookRuntimeTemplatesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_notebook_runtime_templates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_list_notebook_runtime_templates_with_metadata`
        interceptor in new development instead of the `post_list_notebook_runtime_templates` interceptor.
        When both interceptors are used, this `post_list_notebook_runtime_templates_with_metadata` interceptor runs after the
        `post_list_notebook_runtime_templates` interceptor. The (possibly modified) response returned by
        `post_list_notebook_runtime_templates` will be passed to
        `post_list_notebook_runtime_templates_with_metadata`.
        """
        return response, metadata

    async def pre_start_notebook_runtime(
        self,
        request: notebook_service.StartNotebookRuntimeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.StartNotebookRuntimeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for start_notebook_runtime

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_start_notebook_runtime(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for start_notebook_runtime

        DEPRECATED. Please use the `post_start_notebook_runtime_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_start_notebook_runtime` interceptor runs
        before the `post_start_notebook_runtime_with_metadata` interceptor.
        """
        return response

    async def post_start_notebook_runtime_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_notebook_runtime

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_start_notebook_runtime_with_metadata`
        interceptor in new development instead of the `post_start_notebook_runtime` interceptor.
        When both interceptors are used, this `post_start_notebook_runtime_with_metadata` interceptor runs after the
        `post_start_notebook_runtime` interceptor. The (possibly modified) response returned by
        `post_start_notebook_runtime` will be passed to
        `post_start_notebook_runtime_with_metadata`.
        """
        return response, metadata

    async def pre_stop_notebook_runtime(
        self,
        request: notebook_service.StopNotebookRuntimeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.StopNotebookRuntimeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for stop_notebook_runtime

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_stop_notebook_runtime(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for stop_notebook_runtime

        DEPRECATED. Please use the `post_stop_notebook_runtime_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_stop_notebook_runtime` interceptor runs
        before the `post_stop_notebook_runtime_with_metadata` interceptor.
        """
        return response

    async def post_stop_notebook_runtime_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stop_notebook_runtime

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_stop_notebook_runtime_with_metadata`
        interceptor in new development instead of the `post_stop_notebook_runtime` interceptor.
        When both interceptors are used, this `post_stop_notebook_runtime_with_metadata` interceptor runs after the
        `post_stop_notebook_runtime` interceptor. The (possibly modified) response returned by
        `post_stop_notebook_runtime` will be passed to
        `post_stop_notebook_runtime_with_metadata`.
        """
        return response, metadata

    async def pre_update_notebook_runtime_template(
        self,
        request: notebook_service.UpdateNotebookRuntimeTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.UpdateNotebookRuntimeTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_notebook_runtime_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_update_notebook_runtime_template(
        self, response: notebook_runtime.NotebookRuntimeTemplate
    ) -> notebook_runtime.NotebookRuntimeTemplate:
        """Post-rpc interceptor for update_notebook_runtime_template

        DEPRECATED. Please use the `post_update_notebook_runtime_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_update_notebook_runtime_template` interceptor runs
        before the `post_update_notebook_runtime_template_with_metadata` interceptor.
        """
        return response

    async def post_update_notebook_runtime_template_with_metadata(
        self,
        response: notebook_runtime.NotebookRuntimeTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_runtime.NotebookRuntimeTemplate,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_notebook_runtime_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_update_notebook_runtime_template_with_metadata`
        interceptor in new development instead of the `post_update_notebook_runtime_template` interceptor.
        When both interceptors are used, this `post_update_notebook_runtime_template_with_metadata` interceptor runs after the
        `post_update_notebook_runtime_template` interceptor. The (possibly modified) response returned by
        `post_update_notebook_runtime_template` will be passed to
        `post_update_notebook_runtime_template_with_metadata`.
        """
        return response, metadata

    async def pre_upgrade_notebook_runtime(
        self,
        request: notebook_service.UpgradeNotebookRuntimeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        notebook_service.UpgradeNotebookRuntimeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for upgrade_notebook_runtime

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_upgrade_notebook_runtime(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for upgrade_notebook_runtime

        DEPRECATED. Please use the `post_upgrade_notebook_runtime_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code. This `post_upgrade_notebook_runtime` interceptor runs
        before the `post_upgrade_notebook_runtime_with_metadata` interceptor.
        """
        return response

    async def post_upgrade_notebook_runtime_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for upgrade_notebook_runtime

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NotebookService server but before it is returned to user code.

        We recommend only using this `post_upgrade_notebook_runtime_with_metadata`
        interceptor in new development instead of the `post_upgrade_notebook_runtime` interceptor.
        When both interceptors are used, this `post_upgrade_notebook_runtime_with_metadata` interceptor runs after the
        `post_upgrade_notebook_runtime` interceptor. The (possibly modified) response returned by
        `post_upgrade_notebook_runtime` will be passed to
        `post_upgrade_notebook_runtime_with_metadata`.
        """
        return response, metadata

    async def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code.
        """
        return response

    async def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code.
        """
        return response

    async def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_get_iam_policy(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code.
        """
        return response

    async def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_set_iam_policy(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code.
        """
        return response

    async def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code.
        """
        return response

    async def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code.
        """
        return response

    async def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code.
        """
        return response

    async def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code.
        """
        return response

    async def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code.
        """
        return response

    async def pre_wait_operation(
        self,
        request: operations_pb2.WaitOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.WaitOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for wait_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NotebookService server.
        """
        return request, metadata

    async def post_wait_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for wait_operation

        Override in a subclass to manipulate the response
        after it is returned by the NotebookService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AsyncNotebookServiceRestStub:
    _session: AsyncAuthorizedSession
    _host: str
    _interceptor: AsyncNotebookServiceRestInterceptor


class AsyncNotebookServiceRestTransport(_BaseNotebookServiceRestTransport):
    """Asynchronous REST backend transport for NotebookService.

    The interface for Vertex Notebook service (a.k.a. Colab on
    Workbench).

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "aiplatform.googleapis.com",
        credentials: Optional[ga_credentials_async.Credentials] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        url_scheme: str = "https",
        interceptor: Optional[AsyncNotebookServiceRestInterceptor] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'aiplatform.googleapis.com').
            credentials (Optional[google.auth.aio.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            url_scheme (str): the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=False,
            url_scheme=url_scheme,
            api_audience=None,
        )
        self._session = AsyncAuthorizedSession(self._credentials)  # type: ignore
        self._interceptor = interceptor or AsyncNotebookServiceRestInterceptor()
        self._wrap_with_kind = True
        self._prep_wrapped_messages(client_info)
        self._operations_client: Optional[
            operations_v1.AsyncOperationsRestClient
        ] = None

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.create_notebook_runtime_template: self._wrap_method(
                self.create_notebook_runtime_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_notebook_runtime_template: self._wrap_method(
                self.get_notebook_runtime_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_notebook_runtime_templates: self._wrap_method(
                self.list_notebook_runtime_templates,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_notebook_runtime_template: self._wrap_method(
                self.delete_notebook_runtime_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_notebook_runtime_template: self._wrap_method(
                self.update_notebook_runtime_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.assign_notebook_runtime: self._wrap_method(
                self.assign_notebook_runtime,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_notebook_runtime: self._wrap_method(
                self.get_notebook_runtime,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_notebook_runtimes: self._wrap_method(
                self.list_notebook_runtimes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_notebook_runtime: self._wrap_method(
                self.delete_notebook_runtime,
                default_timeout=None,
                client_info=client_info,
            ),
            self.upgrade_notebook_runtime: self._wrap_method(
                self.upgrade_notebook_runtime,
                default_timeout=None,
                client_info=client_info,
            ),
            self.start_notebook_runtime: self._wrap_method(
                self.start_notebook_runtime,
                default_timeout=None,
                client_info=client_info,
            ),
            self.stop_notebook_runtime: self._wrap_method(
                self.stop_notebook_runtime,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_notebook_execution_job: self._wrap_method(
                self.create_notebook_execution_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_notebook_execution_job: self._wrap_method(
                self.get_notebook_execution_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_notebook_execution_jobs: self._wrap_method(
                self.list_notebook_execution_jobs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_notebook_execution_job: self._wrap_method(
                self.delete_notebook_execution_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: self._wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: self._wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: self._wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: self._wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.wait_operation: self._wrap_method(
                self.wait_operation,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def _wrap_method(self, func, *args, **kwargs):
        if self._wrap_with_kind:  # pragma: NO COVER
            kwargs["kind"] = self.kind
        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    class _AssignNotebookRuntime(
        _BaseNotebookServiceRestTransport._BaseAssignNotebookRuntime,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.AssignNotebookRuntime")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        async def __call__(
            self,
            request: notebook_service.AssignNotebookRuntimeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the assign notebook runtime method over HTTP.

            Args:
                request (~.notebook_service.AssignNotebookRuntimeRequest):
                    The request object. Request message for
                [NotebookService.AssignNotebookRuntime][google.cloud.aiplatform.v1.NotebookService.AssignNotebookRuntime].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseAssignNotebookRuntime._get_http_options()
            )

            request, metadata = await self._interceptor.pre_assign_notebook_runtime(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseAssignNotebookRuntime._get_transcoded_request(
                http_options, request
            )

            body = _BaseNotebookServiceRestTransport._BaseAssignNotebookRuntime._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseAssignNotebookRuntime._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.AssignNotebookRuntime",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "AssignNotebookRuntime",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._AssignNotebookRuntime._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_assign_notebook_runtime(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            (
                resp,
                _,
            ) = await self._interceptor.post_assign_notebook_runtime_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.assign_notebook_runtime",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "AssignNotebookRuntime",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _CreateNotebookExecutionJob(
        _BaseNotebookServiceRestTransport._BaseCreateNotebookExecutionJob,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.CreateNotebookExecutionJob")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        async def __call__(
            self,
            request: notebook_service.CreateNotebookExecutionJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create notebook execution
            job method over HTTP.

                Args:
                    request (~.notebook_service.CreateNotebookExecutionJobRequest):
                        The request object. Request message for
                    [NotebookService.CreateNotebookExecutionJob]
                    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseCreateNotebookExecutionJob._get_http_options()
            )

            (
                request,
                metadata,
            ) = await self._interceptor.pre_create_notebook_execution_job(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseCreateNotebookExecutionJob._get_transcoded_request(
                http_options, request
            )

            body = _BaseNotebookServiceRestTransport._BaseCreateNotebookExecutionJob._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseCreateNotebookExecutionJob._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.CreateNotebookExecutionJob",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "CreateNotebookExecutionJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._CreateNotebookExecutionJob._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_create_notebook_execution_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            (
                resp,
                _,
            ) = await self._interceptor.post_create_notebook_execution_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.create_notebook_execution_job",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "CreateNotebookExecutionJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _CreateNotebookRuntimeTemplate(
        _BaseNotebookServiceRestTransport._BaseCreateNotebookRuntimeTemplate,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AsyncNotebookServiceRestTransport.CreateNotebookRuntimeTemplate"
            )

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        async def __call__(
            self,
            request: notebook_service.CreateNotebookRuntimeTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create notebook runtime
            template method over HTTP.

                Args:
                    request (~.notebook_service.CreateNotebookRuntimeTemplateRequest):
                        The request object. Request message for
                    [NotebookService.CreateNotebookRuntimeTemplate][google.cloud.aiplatform.v1.NotebookService.CreateNotebookRuntimeTemplate].
                    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseCreateNotebookRuntimeTemplate._get_http_options()
            )

            (
                request,
                metadata,
            ) = await self._interceptor.pre_create_notebook_runtime_template(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseCreateNotebookRuntimeTemplate._get_transcoded_request(
                http_options, request
            )

            body = _BaseNotebookServiceRestTransport._BaseCreateNotebookRuntimeTemplate._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseCreateNotebookRuntimeTemplate._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.CreateNotebookRuntimeTemplate",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "CreateNotebookRuntimeTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._CreateNotebookRuntimeTemplate._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_create_notebook_runtime_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            (
                resp,
                _,
            ) = await self._interceptor.post_create_notebook_runtime_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.create_notebook_runtime_template",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "CreateNotebookRuntimeTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _DeleteNotebookExecutionJob(
        _BaseNotebookServiceRestTransport._BaseDeleteNotebookExecutionJob,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.DeleteNotebookExecutionJob")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: notebook_service.DeleteNotebookExecutionJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete notebook execution
            job method over HTTP.

                Args:
                    request (~.notebook_service.DeleteNotebookExecutionJobRequest):
                        The request object. Request message for
                    [NotebookService.DeleteNotebookExecutionJob]
                    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseDeleteNotebookExecutionJob._get_http_options()
            )

            (
                request,
                metadata,
            ) = await self._interceptor.pre_delete_notebook_execution_job(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseDeleteNotebookExecutionJob._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseDeleteNotebookExecutionJob._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.DeleteNotebookExecutionJob",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "DeleteNotebookExecutionJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._DeleteNotebookExecutionJob._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_delete_notebook_execution_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            (
                resp,
                _,
            ) = await self._interceptor.post_delete_notebook_execution_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.delete_notebook_execution_job",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "DeleteNotebookExecutionJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _DeleteNotebookRuntime(
        _BaseNotebookServiceRestTransport._BaseDeleteNotebookRuntime,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.DeleteNotebookRuntime")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: notebook_service.DeleteNotebookRuntimeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete notebook runtime method over HTTP.

            Args:
                request (~.notebook_service.DeleteNotebookRuntimeRequest):
                    The request object. Request message for
                [NotebookService.DeleteNotebookRuntime][google.cloud.aiplatform.v1.NotebookService.DeleteNotebookRuntime].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseDeleteNotebookRuntime._get_http_options()
            )

            request, metadata = await self._interceptor.pre_delete_notebook_runtime(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseDeleteNotebookRuntime._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseDeleteNotebookRuntime._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.DeleteNotebookRuntime",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "DeleteNotebookRuntime",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._DeleteNotebookRuntime._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_delete_notebook_runtime(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            (
                resp,
                _,
            ) = await self._interceptor.post_delete_notebook_runtime_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.delete_notebook_runtime",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "DeleteNotebookRuntime",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _DeleteNotebookRuntimeTemplate(
        _BaseNotebookServiceRestTransport._BaseDeleteNotebookRuntimeTemplate,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AsyncNotebookServiceRestTransport.DeleteNotebookRuntimeTemplate"
            )

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: notebook_service.DeleteNotebookRuntimeTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete notebook runtime
            template method over HTTP.

                Args:
                    request (~.notebook_service.DeleteNotebookRuntimeTemplateRequest):
                        The request object. Request message for
                    [NotebookService.DeleteNotebookRuntimeTemplate][google.cloud.aiplatform.v1.NotebookService.DeleteNotebookRuntimeTemplate].
                    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseDeleteNotebookRuntimeTemplate._get_http_options()
            )

            (
                request,
                metadata,
            ) = await self._interceptor.pre_delete_notebook_runtime_template(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseDeleteNotebookRuntimeTemplate._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseDeleteNotebookRuntimeTemplate._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.DeleteNotebookRuntimeTemplate",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "DeleteNotebookRuntimeTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._DeleteNotebookRuntimeTemplate._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_delete_notebook_runtime_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            (
                resp,
                _,
            ) = await self._interceptor.post_delete_notebook_runtime_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.delete_notebook_runtime_template",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "DeleteNotebookRuntimeTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _GetNotebookExecutionJob(
        _BaseNotebookServiceRestTransport._BaseGetNotebookExecutionJob,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.GetNotebookExecutionJob")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: notebook_service.GetNotebookExecutionJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> notebook_execution_job.NotebookExecutionJob:
            r"""Call the get notebook execution
            job method over HTTP.

                Args:
                    request (~.notebook_service.GetNotebookExecutionJobRequest):
                        The request object. Request message for
                    [NotebookService.GetNotebookExecutionJob]
                    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.notebook_execution_job.NotebookExecutionJob:
                        NotebookExecutionJob represents an
                    instance of a notebook execution.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseGetNotebookExecutionJob._get_http_options()
            )

            request, metadata = await self._interceptor.pre_get_notebook_execution_job(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseGetNotebookExecutionJob._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseGetNotebookExecutionJob._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.GetNotebookExecutionJob",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "GetNotebookExecutionJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._GetNotebookExecutionJob._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = notebook_execution_job.NotebookExecutionJob()
            pb_resp = notebook_execution_job.NotebookExecutionJob.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_get_notebook_execution_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            (
                resp,
                _,
            ) = await self._interceptor.post_get_notebook_execution_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        notebook_execution_job.NotebookExecutionJob.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.get_notebook_execution_job",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "GetNotebookExecutionJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _GetNotebookRuntime(
        _BaseNotebookServiceRestTransport._BaseGetNotebookRuntime,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.GetNotebookRuntime")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: notebook_service.GetNotebookRuntimeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> notebook_runtime.NotebookRuntime:
            r"""Call the get notebook runtime method over HTTP.

            Args:
                request (~.notebook_service.GetNotebookRuntimeRequest):
                    The request object. Request message for
                [NotebookService.GetNotebookRuntime][google.cloud.aiplatform.v1.NotebookService.GetNotebookRuntime]
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.notebook_runtime.NotebookRuntime:
                    A runtime is a virtual machine
                allocated to a particular user for a
                particular Notebook file on temporary
                basis with lifetime. Default runtimes
                have a lifetime of 18 hours, while
                custom runtimes last for 6 months from
                their creation or last upgrade.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseGetNotebookRuntime._get_http_options()
            )

            request, metadata = await self._interceptor.pre_get_notebook_runtime(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseGetNotebookRuntime._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseGetNotebookRuntime._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.GetNotebookRuntime",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "GetNotebookRuntime",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._GetNotebookRuntime._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = notebook_runtime.NotebookRuntime()
            pb_resp = notebook_runtime.NotebookRuntime.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_get_notebook_runtime(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_get_notebook_runtime_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = notebook_runtime.NotebookRuntime.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.get_notebook_runtime",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "GetNotebookRuntime",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _GetNotebookRuntimeTemplate(
        _BaseNotebookServiceRestTransport._BaseGetNotebookRuntimeTemplate,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.GetNotebookRuntimeTemplate")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: notebook_service.GetNotebookRuntimeTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> notebook_runtime.NotebookRuntimeTemplate:
            r"""Call the get notebook runtime
            template method over HTTP.

                Args:
                    request (~.notebook_service.GetNotebookRuntimeTemplateRequest):
                        The request object. Request message for
                    [NotebookService.GetNotebookRuntimeTemplate][google.cloud.aiplatform.v1.NotebookService.GetNotebookRuntimeTemplate]
                    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.notebook_runtime.NotebookRuntimeTemplate:
                        A template that specifies runtime
                    configurations such as machine type,
                    runtime version, network configurations,
                    etc. Multiple runtimes can be created
                    from a runtime template.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseGetNotebookRuntimeTemplate._get_http_options()
            )

            (
                request,
                metadata,
            ) = await self._interceptor.pre_get_notebook_runtime_template(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseGetNotebookRuntimeTemplate._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseGetNotebookRuntimeTemplate._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.GetNotebookRuntimeTemplate",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "GetNotebookRuntimeTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._GetNotebookRuntimeTemplate._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = notebook_runtime.NotebookRuntimeTemplate()
            pb_resp = notebook_runtime.NotebookRuntimeTemplate.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_get_notebook_runtime_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            (
                resp,
                _,
            ) = await self._interceptor.post_get_notebook_runtime_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = notebook_runtime.NotebookRuntimeTemplate.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.get_notebook_runtime_template",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "GetNotebookRuntimeTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _ListNotebookExecutionJobs(
        _BaseNotebookServiceRestTransport._BaseListNotebookExecutionJobs,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.ListNotebookExecutionJobs")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: notebook_service.ListNotebookExecutionJobsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> notebook_service.ListNotebookExecutionJobsResponse:
            r"""Call the list notebook execution
            jobs method over HTTP.

                Args:
                    request (~.notebook_service.ListNotebookExecutionJobsRequest):
                        The request object. Request message for
                    [NotebookService.ListNotebookExecutionJobs]
                    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.notebook_service.ListNotebookExecutionJobsResponse:
                        Response message for
                    [NotebookService.CreateNotebookExecutionJob]

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseListNotebookExecutionJobs._get_http_options()
            )

            (
                request,
                metadata,
            ) = await self._interceptor.pre_list_notebook_execution_jobs(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseListNotebookExecutionJobs._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseListNotebookExecutionJobs._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.ListNotebookExecutionJobs",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "ListNotebookExecutionJobs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._ListNotebookExecutionJobs._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = notebook_service.ListNotebookExecutionJobsResponse()
            pb_resp = notebook_service.ListNotebookExecutionJobsResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_list_notebook_execution_jobs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            (
                resp,
                _,
            ) = await self._interceptor.post_list_notebook_execution_jobs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        notebook_service.ListNotebookExecutionJobsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.list_notebook_execution_jobs",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "ListNotebookExecutionJobs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _ListNotebookRuntimes(
        _BaseNotebookServiceRestTransport._BaseListNotebookRuntimes,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.ListNotebookRuntimes")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: notebook_service.ListNotebookRuntimesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> notebook_service.ListNotebookRuntimesResponse:
            r"""Call the list notebook runtimes method over HTTP.

            Args:
                request (~.notebook_service.ListNotebookRuntimesRequest):
                    The request object. Request message for
                [NotebookService.ListNotebookRuntimes][google.cloud.aiplatform.v1.NotebookService.ListNotebookRuntimes].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.notebook_service.ListNotebookRuntimesResponse:
                    Response message for
                [NotebookService.ListNotebookRuntimes][google.cloud.aiplatform.v1.NotebookService.ListNotebookRuntimes].

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseListNotebookRuntimes._get_http_options()
            )

            request, metadata = await self._interceptor.pre_list_notebook_runtimes(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseListNotebookRuntimes._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseListNotebookRuntimes._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.ListNotebookRuntimes",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "ListNotebookRuntimes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._ListNotebookRuntimes._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = notebook_service.ListNotebookRuntimesResponse()
            pb_resp = notebook_service.ListNotebookRuntimesResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_list_notebook_runtimes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_list_notebook_runtimes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        notebook_service.ListNotebookRuntimesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.list_notebook_runtimes",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "ListNotebookRuntimes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _ListNotebookRuntimeTemplates(
        _BaseNotebookServiceRestTransport._BaseListNotebookRuntimeTemplates,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AsyncNotebookServiceRestTransport.ListNotebookRuntimeTemplates"
            )

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: notebook_service.ListNotebookRuntimeTemplatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> notebook_service.ListNotebookRuntimeTemplatesResponse:
            r"""Call the list notebook runtime
            templates method over HTTP.

                Args:
                    request (~.notebook_service.ListNotebookRuntimeTemplatesRequest):
                        The request object. Request message for
                    [NotebookService.ListNotebookRuntimeTemplates][google.cloud.aiplatform.v1.NotebookService.ListNotebookRuntimeTemplates].
                    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.notebook_service.ListNotebookRuntimeTemplatesResponse:
                        Response message for
                    [NotebookService.ListNotebookRuntimeTemplates][google.cloud.aiplatform.v1.NotebookService.ListNotebookRuntimeTemplates].

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseListNotebookRuntimeTemplates._get_http_options()
            )

            (
                request,
                metadata,
            ) = await self._interceptor.pre_list_notebook_runtime_templates(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseListNotebookRuntimeTemplates._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseListNotebookRuntimeTemplates._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.ListNotebookRuntimeTemplates",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "ListNotebookRuntimeTemplates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._ListNotebookRuntimeTemplates._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = notebook_service.ListNotebookRuntimeTemplatesResponse()
            pb_resp = notebook_service.ListNotebookRuntimeTemplatesResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_list_notebook_runtime_templates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            (
                resp,
                _,
            ) = await self._interceptor.post_list_notebook_runtime_templates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        notebook_service.ListNotebookRuntimeTemplatesResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.list_notebook_runtime_templates",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "ListNotebookRuntimeTemplates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _StartNotebookRuntime(
        _BaseNotebookServiceRestTransport._BaseStartNotebookRuntime,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.StartNotebookRuntime")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        async def __call__(
            self,
            request: notebook_service.StartNotebookRuntimeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the start notebook runtime method over HTTP.

            Args:
                request (~.notebook_service.StartNotebookRuntimeRequest):
                    The request object. Request message for
                [NotebookService.StartNotebookRuntime][google.cloud.aiplatform.v1.NotebookService.StartNotebookRuntime].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseStartNotebookRuntime._get_http_options()
            )

            request, metadata = await self._interceptor.pre_start_notebook_runtime(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseStartNotebookRuntime._get_transcoded_request(
                http_options, request
            )

            body = _BaseNotebookServiceRestTransport._BaseStartNotebookRuntime._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseStartNotebookRuntime._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.StartNotebookRuntime",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "StartNotebookRuntime",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._StartNotebookRuntime._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_start_notebook_runtime(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_start_notebook_runtime_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.start_notebook_runtime",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "StartNotebookRuntime",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _StopNotebookRuntime(
        _BaseNotebookServiceRestTransport._BaseStopNotebookRuntime,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.StopNotebookRuntime")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        async def __call__(
            self,
            request: notebook_service.StopNotebookRuntimeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the stop notebook runtime method over HTTP.

            Args:
                request (~.notebook_service.StopNotebookRuntimeRequest):
                    The request object. Request message for
                [NotebookService.StopNotebookRuntime][google.cloud.aiplatform.v1.NotebookService.StopNotebookRuntime].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseStopNotebookRuntime._get_http_options()
            )

            request, metadata = await self._interceptor.pre_stop_notebook_runtime(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseStopNotebookRuntime._get_transcoded_request(
                http_options, request
            )

            body = _BaseNotebookServiceRestTransport._BaseStopNotebookRuntime._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseStopNotebookRuntime._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.StopNotebookRuntime",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "StopNotebookRuntime",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._StopNotebookRuntime._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_stop_notebook_runtime(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_stop_notebook_runtime_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.stop_notebook_runtime",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "StopNotebookRuntime",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _UpdateNotebookRuntimeTemplate(
        _BaseNotebookServiceRestTransport._BaseUpdateNotebookRuntimeTemplate,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AsyncNotebookServiceRestTransport.UpdateNotebookRuntimeTemplate"
            )

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        async def __call__(
            self,
            request: notebook_service.UpdateNotebookRuntimeTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> notebook_runtime.NotebookRuntimeTemplate:
            r"""Call the update notebook runtime
            template method over HTTP.

                Args:
                    request (~.notebook_service.UpdateNotebookRuntimeTemplateRequest):
                        The request object. Request message for
                    [NotebookService.UpdateNotebookRuntimeTemplate][google.cloud.aiplatform.v1.NotebookService.UpdateNotebookRuntimeTemplate].
                    retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.notebook_runtime.NotebookRuntimeTemplate:
                        A template that specifies runtime
                    configurations such as machine type,
                    runtime version, network configurations,
                    etc. Multiple runtimes can be created
                    from a runtime template.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseUpdateNotebookRuntimeTemplate._get_http_options()
            )

            (
                request,
                metadata,
            ) = await self._interceptor.pre_update_notebook_runtime_template(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseUpdateNotebookRuntimeTemplate._get_transcoded_request(
                http_options, request
            )

            body = _BaseNotebookServiceRestTransport._BaseUpdateNotebookRuntimeTemplate._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseUpdateNotebookRuntimeTemplate._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.UpdateNotebookRuntimeTemplate",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "UpdateNotebookRuntimeTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._UpdateNotebookRuntimeTemplate._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = notebook_runtime.NotebookRuntimeTemplate()
            pb_resp = notebook_runtime.NotebookRuntimeTemplate.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_update_notebook_runtime_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            (
                resp,
                _,
            ) = await self._interceptor.post_update_notebook_runtime_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = notebook_runtime.NotebookRuntimeTemplate.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.update_notebook_runtime_template",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "UpdateNotebookRuntimeTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _UpgradeNotebookRuntime(
        _BaseNotebookServiceRestTransport._BaseUpgradeNotebookRuntime,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.UpgradeNotebookRuntime")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        async def __call__(
            self,
            request: notebook_service.UpgradeNotebookRuntimeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the upgrade notebook runtime method over HTTP.

            Args:
                request (~.notebook_service.UpgradeNotebookRuntimeRequest):
                    The request object. Request message for
                [NotebookService.UpgradeNotebookRuntime][google.cloud.aiplatform.v1.NotebookService.UpgradeNotebookRuntime].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseUpgradeNotebookRuntime._get_http_options()
            )

            request, metadata = await self._interceptor.pre_upgrade_notebook_runtime(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseUpgradeNotebookRuntime._get_transcoded_request(
                http_options, request
            )

            body = _BaseNotebookServiceRestTransport._BaseUpgradeNotebookRuntime._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseUpgradeNotebookRuntime._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.UpgradeNotebookRuntime",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "UpgradeNotebookRuntime",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._UpgradeNotebookRuntime._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_upgrade_notebook_runtime(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            (
                resp,
                _,
            ) = await self._interceptor.post_upgrade_notebook_runtime_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": "OK",  # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.upgrade_notebook_runtime",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "UpgradeNotebookRuntime",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    @property
    def operations_client(self) -> AsyncOperationsRestClient:
        """Create the async client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/agents/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/apps/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/ragEngineConfig/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/endpoints/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/customJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/tuningJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/indexes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/migratableResources/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/models/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/persistentResources/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/ragEngineConfig/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/ragCorpora/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/studies/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/schedules/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/specialistPools/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/agents/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/apps/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*}/operations",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*}/operations",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/ragEngineConfig/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/featureMonitors/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/endpoints/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/customJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/models/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/ragEngineConfig/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/ragCorpora/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/studies/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/schedules/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/agents/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/apps/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDeploymentJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/ragEngineConfig/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/featureMonitors/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/endpoints/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/customJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/tuningJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/models/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/ragEngineConfig/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/ragCorpora/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/studies/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/schedules/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/agents/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/apps/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/models/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/notebookExecutionJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimeTemplates/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/ragEngineConfig}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/featureMonitors/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/dataItems/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/savedQueries/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/deploymentResourcePools/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/endpoints/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/entityTypes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/customJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/dataLabelingJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/hyperparameterTuningJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/tuningJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/indexes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/indexEndpoints/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/artifacts/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/contexts/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/executions/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/migratableResources/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/models/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/models/*/evaluations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/notebookExecutionJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/notebookRuntimes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/notebookRuntimeTemplates/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/reasoningEngines/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/studies/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/studies/*/trials/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/trainingPipelines/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/persistentResources/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/pipelineJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/ragEngineConfig}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/ragCorpora/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/schedules/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/specialistPools/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                    },
                ],
                "google.longrunning.Operations.WaitOperation": [
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/agents/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/apps/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/ragEngineConfig/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/featureMonitors/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/endpoints/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/customJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/indexes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/migratableResources/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/models/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/ragEngineConfig/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/ragCorpora/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/studies/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/persistentResources/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/schedules/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/specialistPools/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                    },
                ],
            }

            rest_transport = operations_v1.AsyncOperationsRestTransport(  # type: ignore
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,  # type: ignore
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = AsyncOperationsRestClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def assign_notebook_runtime(
        self,
    ) -> Callable[
        [notebook_service.AssignNotebookRuntimeRequest], operations_pb2.Operation
    ]:
        return self._AssignNotebookRuntime(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_notebook_execution_job(
        self,
    ) -> Callable[
        [notebook_service.CreateNotebookExecutionJobRequest], operations_pb2.Operation
    ]:
        return self._CreateNotebookExecutionJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_notebook_runtime_template(
        self,
    ) -> Callable[
        [notebook_service.CreateNotebookRuntimeTemplateRequest],
        operations_pb2.Operation,
    ]:
        return self._CreateNotebookRuntimeTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_notebook_execution_job(
        self,
    ) -> Callable[
        [notebook_service.DeleteNotebookExecutionJobRequest], operations_pb2.Operation
    ]:
        return self._DeleteNotebookExecutionJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_notebook_runtime(
        self,
    ) -> Callable[
        [notebook_service.DeleteNotebookRuntimeRequest], operations_pb2.Operation
    ]:
        return self._DeleteNotebookRuntime(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_notebook_runtime_template(
        self,
    ) -> Callable[
        [notebook_service.DeleteNotebookRuntimeTemplateRequest],
        operations_pb2.Operation,
    ]:
        return self._DeleteNotebookRuntimeTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_notebook_execution_job(
        self,
    ) -> Callable[
        [notebook_service.GetNotebookExecutionJobRequest],
        notebook_execution_job.NotebookExecutionJob,
    ]:
        return self._GetNotebookExecutionJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_notebook_runtime(
        self,
    ) -> Callable[
        [notebook_service.GetNotebookRuntimeRequest], notebook_runtime.NotebookRuntime
    ]:
        return self._GetNotebookRuntime(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_notebook_runtime_template(
        self,
    ) -> Callable[
        [notebook_service.GetNotebookRuntimeTemplateRequest],
        notebook_runtime.NotebookRuntimeTemplate,
    ]:
        return self._GetNotebookRuntimeTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_notebook_execution_jobs(
        self,
    ) -> Callable[
        [notebook_service.ListNotebookExecutionJobsRequest],
        notebook_service.ListNotebookExecutionJobsResponse,
    ]:
        return self._ListNotebookExecutionJobs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_notebook_runtimes(
        self,
    ) -> Callable[
        [notebook_service.ListNotebookRuntimesRequest],
        notebook_service.ListNotebookRuntimesResponse,
    ]:
        return self._ListNotebookRuntimes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_notebook_runtime_templates(
        self,
    ) -> Callable[
        [notebook_service.ListNotebookRuntimeTemplatesRequest],
        notebook_service.ListNotebookRuntimeTemplatesResponse,
    ]:
        return self._ListNotebookRuntimeTemplates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_notebook_runtime(
        self,
    ) -> Callable[
        [notebook_service.StartNotebookRuntimeRequest], operations_pb2.Operation
    ]:
        return self._StartNotebookRuntime(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_notebook_runtime(
        self,
    ) -> Callable[
        [notebook_service.StopNotebookRuntimeRequest], operations_pb2.Operation
    ]:
        return self._StopNotebookRuntime(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_notebook_runtime_template(
        self,
    ) -> Callable[
        [notebook_service.UpdateNotebookRuntimeTemplateRequest],
        notebook_runtime.NotebookRuntimeTemplate,
    ]:
        return self._UpdateNotebookRuntimeTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def upgrade_notebook_runtime(
        self,
    ) -> Callable[
        [notebook_service.UpgradeNotebookRuntimeRequest], operations_pb2.Operation
    ]:
        return self._UpgradeNotebookRuntime(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseNotebookServiceRestTransport._BaseGetLocation, AsyncNotebookServiceRestStub
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.GetLocation")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:

            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseGetLocation._get_http_options()
            )

            request, metadata = await self._interceptor.pre_get_location(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseGetLocation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseGetLocation._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                await AsyncNotebookServiceRestTransport._GetLocation._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_get_location(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseNotebookServiceRestTransport._BaseListLocations,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.ListLocations")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:

            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseListLocations._get_http_options()
            )

            request, metadata = await self._interceptor.pre_list_locations(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseListLocations._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseListLocations._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                await AsyncNotebookServiceRestTransport._ListLocations._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_list_locations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseNotebookServiceRestTransport._BaseGetIamPolicy,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.GetIamPolicy")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:

            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseGetIamPolicy._get_http_options()
            )

            request, metadata = await self._interceptor.pre_get_iam_policy(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseGetIamPolicy._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseGetIamPolicy._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                await AsyncNotebookServiceRestTransport._GetIamPolicy._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_get_iam_policy(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(
        _BaseNotebookServiceRestTransport._BaseSetIamPolicy,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.SetIamPolicy")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        async def __call__(
            self,
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:

            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseSetIamPolicy._get_http_options()
            )

            request, metadata = await self._interceptor.pre_set_iam_policy(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseSetIamPolicy._get_transcoded_request(
                http_options, request
            )

            body = _BaseNotebookServiceRestTransport._BaseSetIamPolicy._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseSetIamPolicy._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                await AsyncNotebookServiceRestTransport._SetIamPolicy._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_set_iam_policy(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(
        _BaseNotebookServiceRestTransport._BaseTestIamPermissions,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.TestIamPermissions")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:

            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseTestIamPermissions._get_http_options()
            )

            request, metadata = await self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseTestIamPermissions._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseTestIamPermissions._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncNotebookServiceRestTransport._TestIamPermissions._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_test_iam_permissions(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseNotebookServiceRestTransport._BaseCancelOperation,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.CancelOperation")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:

            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseCancelOperation._get_http_options()
            )

            request, metadata = await self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseCancelOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseCancelOperation._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                await AsyncNotebookServiceRestTransport._CancelOperation._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            return await self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseNotebookServiceRestTransport._BaseDeleteOperation,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.DeleteOperation")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:

            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseDeleteOperation._get_http_options()
            )

            request, metadata = await self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseDeleteOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseDeleteOperation._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                await AsyncNotebookServiceRestTransport._DeleteOperation._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            return await self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseNotebookServiceRestTransport._BaseGetOperation,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.GetOperation")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:

            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseGetOperation._get_http_options()
            )

            request, metadata = await self._interceptor.pre_get_operation(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseGetOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseGetOperation._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                await AsyncNotebookServiceRestTransport._GetOperation._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_get_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseNotebookServiceRestTransport._BaseListOperations,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.ListOperations")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:

            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseListOperations._get_http_options()
            )

            request, metadata = await self._interceptor.pre_list_operations(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseListOperations._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseListOperations._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                await AsyncNotebookServiceRestTransport._ListOperations._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_list_operations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "ListOperations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def wait_operation(self):
        return self._WaitOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _WaitOperation(
        _BaseNotebookServiceRestTransport._BaseWaitOperation,
        AsyncNotebookServiceRestStub,
    ):
        def __hash__(self):
            return hash("AsyncNotebookServiceRestTransport.WaitOperation")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = await getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        async def __call__(
            self,
            request: operations_pb2.WaitOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:

            r"""Call the wait operation method over HTTP.

            Args:
                request (operations_pb2.WaitOperationRequest):
                    The request object for WaitOperation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from WaitOperation method.
            """

            http_options = (
                _BaseNotebookServiceRestTransport._BaseWaitOperation._get_http_options()
            )

            request, metadata = await self._interceptor.pre_wait_operation(
                request, metadata
            )
            transcoded_request = _BaseNotebookServiceRestTransport._BaseWaitOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseNotebookServiceRestTransport._BaseWaitOperation._get_query_params_json(
                transcoded_request
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.aiplatform_v1.NotebookServiceClient.WaitOperation",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "WaitOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                await AsyncNotebookServiceRestTransport._WaitOperation._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode("utf-8"))
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_wait_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.aiplatform_v1.NotebookServiceAsyncClient.WaitOperation",
                    extra={
                        "serviceName": "google.cloud.aiplatform.v1.NotebookService",
                        "rpcName": "WaitOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def kind(self) -> str:
        return "rest_asyncio"

    async def close(self):
        await self._session.close()
