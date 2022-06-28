# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import holoViveCom_pb2 as holoViveCom__pb2


class BackendStub(object):
    """package unary;

    package unary;
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LighthouseReport = channel.stream_unary(
                '/Backend/LighthouseReport',
                request_serializer=holoViveCom__pb2.LighthouseState.SerializeToString,
                response_deserializer=holoViveCom__pb2.Empty.FromString,
                )
        self.ProvideLighthouseState = channel.unary_stream(
                '/Backend/ProvideLighthouseState',
                request_serializer=holoViveCom__pb2.InformationRequest.SerializeToString,
                response_deserializer=holoViveCom__pb2.LighthouseState.FromString,
                )
        self.ProvideTrackerState = channel.unary_stream(
                '/Backend/ProvideTrackerState',
                request_serializer=holoViveCom__pb2.InformationRequest.SerializeToString,
                response_deserializer=holoViveCom__pb2.LighthouseState.FromString,
                )
        self.ChangeStatus = channel.unary_unary(
                '/Backend/ChangeStatus',
                request_serializer=holoViveCom__pb2.Status.SerializeToString,
                response_deserializer=holoViveCom__pb2.Empty.FromString,
                )
        self.UpdateCalibrationInfo = channel.unary_unary(
                '/Backend/UpdateCalibrationInfo',
                request_serializer=holoViveCom__pb2.CalibrationInfo.SerializeToString,
                response_deserializer=holoViveCom__pb2.Empty.FromString,
                )
        self.GetCalibrationInfo = channel.unary_unary(
                '/Backend/GetCalibrationInfo',
                request_serializer=holoViveCom__pb2.Empty.SerializeToString,
                response_deserializer=holoViveCom__pb2.CalibrationInfo.FromString,
                )
        self.PlaceWayPoint = channel.unary_unary(
                '/Backend/PlaceWayPoint',
                request_serializer=holoViveCom__pb2.LighthouseState.SerializeToString,
                response_deserializer=holoViveCom__pb2.Empty.FromString,
                )


class BackendServicer(object):
    """package unary;

    package unary;
    """

    def LighthouseReport(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProvideLighthouseState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProvideTrackerState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCalibrationInfo(self, request, context):
        """Following function are used to manage the calribation information
        One RPC to send and one to receive
        GetCalibration is used from services on startup to get the calibrationinfo
        UpdateCalibration is called when a new calibration becomes available or is set
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCalibrationInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlaceWayPoint(self, request, context):
        """special rpc which will be used to signal that a waypoint via the controller method shall be placed
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BackendServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LighthouseReport': grpc.stream_unary_rpc_method_handler(
                    servicer.LighthouseReport,
                    request_deserializer=holoViveCom__pb2.LighthouseState.FromString,
                    response_serializer=holoViveCom__pb2.Empty.SerializeToString,
            ),
            'ProvideLighthouseState': grpc.unary_stream_rpc_method_handler(
                    servicer.ProvideLighthouseState,
                    request_deserializer=holoViveCom__pb2.InformationRequest.FromString,
                    response_serializer=holoViveCom__pb2.LighthouseState.SerializeToString,
            ),
            'ProvideTrackerState': grpc.unary_stream_rpc_method_handler(
                    servicer.ProvideTrackerState,
                    request_deserializer=holoViveCom__pb2.InformationRequest.FromString,
                    response_serializer=holoViveCom__pb2.LighthouseState.SerializeToString,
            ),
            'ChangeStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeStatus,
                    request_deserializer=holoViveCom__pb2.Status.FromString,
                    response_serializer=holoViveCom__pb2.Empty.SerializeToString,
            ),
            'UpdateCalibrationInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCalibrationInfo,
                    request_deserializer=holoViveCom__pb2.CalibrationInfo.FromString,
                    response_serializer=holoViveCom__pb2.Empty.SerializeToString,
            ),
            'GetCalibrationInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCalibrationInfo,
                    request_deserializer=holoViveCom__pb2.Empty.FromString,
                    response_serializer=holoViveCom__pb2.CalibrationInfo.SerializeToString,
            ),
            'PlaceWayPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.PlaceWayPoint,
                    request_deserializer=holoViveCom__pb2.LighthouseState.FromString,
                    response_serializer=holoViveCom__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Backend', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Backend(object):
    """package unary;

    package unary;
    """

    @staticmethod
    def LighthouseReport(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/Backend/LighthouseReport',
            holoViveCom__pb2.LighthouseState.SerializeToString,
            holoViveCom__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProvideLighthouseState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Backend/ProvideLighthouseState',
            holoViveCom__pb2.InformationRequest.SerializeToString,
            holoViveCom__pb2.LighthouseState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProvideTrackerState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Backend/ProvideTrackerState',
            holoViveCom__pb2.InformationRequest.SerializeToString,
            holoViveCom__pb2.LighthouseState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Backend/ChangeStatus',
            holoViveCom__pb2.Status.SerializeToString,
            holoViveCom__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCalibrationInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Backend/UpdateCalibrationInfo',
            holoViveCom__pb2.CalibrationInfo.SerializeToString,
            holoViveCom__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCalibrationInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Backend/GetCalibrationInfo',
            holoViveCom__pb2.Empty.SerializeToString,
            holoViveCom__pb2.CalibrationInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlaceWayPoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Backend/PlaceWayPoint',
            holoViveCom__pb2.LighthouseState.SerializeToString,
            holoViveCom__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)