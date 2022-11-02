# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import app.v1.service.request_pb2 as request__pb2


class userStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.login = channel.unary_unary(
                '/user/login',
                request_serializer=request__pb2.Request.SerializeToString,
                response_deserializer=request__pb2.Response.FromString,
                )
        self.listUser = channel.unary_unary(
                '/user/listUser',
                request_serializer=request__pb2.Request.SerializeToString,
                response_deserializer=request__pb2.Response.FromString,
                )
        self.register = channel.unary_unary(
                '/user/register',
                request_serializer=request__pb2.Request.SerializeToString,
                response_deserializer=request__pb2.Response.FromString,
                )
        self.delete = channel.unary_unary(
                '/user/delete',
                request_serializer=request__pb2.Request.SerializeToString,
                response_deserializer=request__pb2.Response.FromString,
                )
        self.resetPassword = channel.unary_unary(
                '/user/resetPassword',
                request_serializer=request__pb2.Request.SerializeToString,
                response_deserializer=request__pb2.Response.FromString,
                )
        self.update = channel.unary_unary(
                '/user/update',
                request_serializer=request__pb2.Request.SerializeToString,
                response_deserializer=request__pb2.Response.FromString,
                )
        self.generatePassword = channel.unary_unary(
                '/user/generatePassword',
                request_serializer=request__pb2.Request.SerializeToString,
                response_deserializer=request__pb2.Response.FromString,
                )
        self.checkToken = channel.unary_unary(
                '/user/checkToken',
                request_serializer=request__pb2.Request.SerializeToString,
                response_deserializer=request__pb2.Response.FromString,
                )
        self.query = channel.unary_unary(
                '/user/query',
                request_serializer=request__pb2.Request.SerializeToString,
                response_deserializer=request__pb2.Response.FromString,
                )


class userServicer(object):
    """Missing associated documentation comment in .proto file."""

    def login(self, request, context):
        """login
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def resetPassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def generatePassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def checkToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_userServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'login': grpc.unary_unary_rpc_method_handler(
                    servicer.login,
                    request_deserializer=request__pb2.Request.FromString,
                    response_serializer=request__pb2.Response.SerializeToString,
            ),
            'listUser': grpc.unary_unary_rpc_method_handler(
                    servicer.listUser,
                    request_deserializer=request__pb2.Request.FromString,
                    response_serializer=request__pb2.Response.SerializeToString,
            ),
            'register': grpc.unary_unary_rpc_method_handler(
                    servicer.register,
                    request_deserializer=request__pb2.Request.FromString,
                    response_serializer=request__pb2.Response.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=request__pb2.Request.FromString,
                    response_serializer=request__pb2.Response.SerializeToString,
            ),
            'resetPassword': grpc.unary_unary_rpc_method_handler(
                    servicer.resetPassword,
                    request_deserializer=request__pb2.Request.FromString,
                    response_serializer=request__pb2.Response.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=request__pb2.Request.FromString,
                    response_serializer=request__pb2.Response.SerializeToString,
            ),
            'generatePassword': grpc.unary_unary_rpc_method_handler(
                    servicer.generatePassword,
                    request_deserializer=request__pb2.Request.FromString,
                    response_serializer=request__pb2.Response.SerializeToString,
            ),
            'checkToken': grpc.unary_unary_rpc_method_handler(
                    servicer.checkToken,
                    request_deserializer=request__pb2.Request.FromString,
                    response_serializer=request__pb2.Response.SerializeToString,
            ),
            'query': grpc.unary_unary_rpc_method_handler(
                    servicer.query,
                    request_deserializer=request__pb2.Request.FromString,
                    response_serializer=request__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class user(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user/login',
            request__pb2.Request.SerializeToString,
            request__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user/listUser',
            request__pb2.Request.SerializeToString,
            request__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user/register',
            request__pb2.Request.SerializeToString,
            request__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user/delete',
            request__pb2.Request.SerializeToString,
            request__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def resetPassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user/resetPassword',
            request__pb2.Request.SerializeToString,
            request__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user/update',
            request__pb2.Request.SerializeToString,
            request__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def generatePassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user/generatePassword',
            request__pb2.Request.SerializeToString,
            request__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def checkToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user/checkToken',
            request__pb2.Request.SerializeToString,
            request__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user/query',
            request__pb2.Request.SerializeToString,
            request__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
