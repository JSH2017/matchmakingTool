# coding: utf-8

"""
    Matchmaking tool

    Documentacion de llamadas para la generacion del api del matchmaking tool del proyecto jalisco sin hambre.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from empleos.api_client import ApiClient


class EmpleoApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_job(self, body, **kwargs):  # noqa: E501
        """Agregar nueva oferta de empleo al sistema  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_job(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Empleo body: Oferta de empleo a añadir (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_job_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_job_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_job_with_http_info(self, body, **kwargs):  # noqa: E501
        """Agregar nueva oferta de empleo al sistema  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_job_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Empleo body: Oferta de empleo a añadir (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/empleo', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_empleo(self, empleo_id, **kwargs):  # noqa: E501
        """Borra una oferta de trabajo  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_empleo(empleo_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int empleo_id: id del empleo a borrar (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_empleo_with_http_info(empleo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_empleo_with_http_info(empleo_id, **kwargs)  # noqa: E501
            return data

    def delete_empleo_with_http_info(self, empleo_id, **kwargs):  # noqa: E501
        """Borra una oferta de trabajo  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_empleo_with_http_info(empleo_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int empleo_id: id del empleo a borrar (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['empleo_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_empleo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'empleo_id' is set
        if ('empleo_id' not in params or
                params['empleo_id'] is None):
            raise ValueError("Missing the required parameter `empleo_id` when calling `delete_empleo`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'empleo_id' in params:
            query_params.append(('empleoId', params['empleo_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/empleo', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_jobs_by_centro_comunitario(self, centro_comunitario_id, **kwargs):  # noqa: E501
        """Encontrar empleo cerca del centro comunitario  # noqa: E501

        Multiple status values can be provided with comma separated strings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_jobs_by_centro_comunitario(centro_comunitario_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int centro_comunitario_id: Status values that need to be considered for filter (required)
        :return: list[Empleo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.find_jobs_by_centro_comunitario_with_http_info(centro_comunitario_id, **kwargs)  # noqa: E501
        else:
            (data) = self.find_jobs_by_centro_comunitario_with_http_info(centro_comunitario_id, **kwargs)  # noqa: E501
            return data

    def find_jobs_by_centro_comunitario_with_http_info(self, centro_comunitario_id, **kwargs):  # noqa: E501
        """Encontrar empleo cerca del centro comunitario  # noqa: E501

        Multiple status values can be provided with comma separated strings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_jobs_by_centro_comunitario_with_http_info(centro_comunitario_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int centro_comunitario_id: Status values that need to be considered for filter (required)
        :return: list[Empleo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['centro_comunitario_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_jobs_by_centro_comunitario" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'centro_comunitario_id' is set
        if ('centro_comunitario_id' not in params or
                params['centro_comunitario_id'] is None):
            raise ValueError("Missing the required parameter `centro_comunitario_id` when calling `find_jobs_by_centro_comunitario`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'centro_comunitario_id' in params:
            query_params.append(('CentroComunitarioId', params['centro_comunitario_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/empleo/findByCentroComunitario', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Empleo]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_jobs_by_status(self, status, **kwargs):  # noqa: E501
        """Encontrar empleo por estatus  # noqa: E501

        Multiple status values can be provided with comma separated strings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_jobs_by_status(status, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] status: Status values that need to be considered for filter (required)
        :return: list[Empleo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.find_jobs_by_status_with_http_info(status, **kwargs)  # noqa: E501
        else:
            (data) = self.find_jobs_by_status_with_http_info(status, **kwargs)  # noqa: E501
            return data

    def find_jobs_by_status_with_http_info(self, status, **kwargs):  # noqa: E501
        """Encontrar empleo por estatus  # noqa: E501

        Multiple status values can be provided with comma separated strings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_jobs_by_status_with_http_info(status, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] status: Status values that need to be considered for filter (required)
        :return: list[Empleo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_jobs_by_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status' is set
        if ('status' not in params or
                params['status'] is None):
            raise ValueError("Missing the required parameter `status` when calling `find_jobs_by_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
            collection_formats['status'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/empleo/findByStatus', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Empleo]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_job(self, body, **kwargs):  # noqa: E501
        """Actualizar una oferta de empleo existente  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_job(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Empleo body: Oferta de trabajo a modificar (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_job_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_job_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_job_with_http_info(self, body, **kwargs):  # noqa: E501
        """Actualizar una oferta de empleo existente  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_job_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Empleo body: Oferta de trabajo a modificar (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['petstore_auth']  # noqa: E501

        return self.api_client.call_api(
            '/empleo', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
