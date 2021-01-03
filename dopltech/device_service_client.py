import logging
import grpc
import os

from dopltech.protos.device_service_pb2_grpc import DeviceServiceStub
from dopltech.protos.common_pb2 import (
    DeviceInfo,
)
from dopltech.protos.device_service_pb2 import (
    CreateDeviceRequest,
    DeleteDeviceRequest,
    UpdateDeviceRequest,
)

class DeviceServiceClient:
    def __init__(self, host, port):
        server_address = "{}:{}".format(host, port)

        print("Connecting to device service @ " + server_address)
        self.__channel = grpc.insecure_channel(server_address)
        self.__stub = DeviceServiceStub(self.__channel)
    
    def create(self, name, type, ip, port):
        response = self.__stub.Create(CreateDeviceRequest(
            info=DeviceInfo(
                name=name,
                type=type,
                ip=ip,
                port=port,
            )
        ))

        return response.device.id
    
    def update(self, deviceID, ipv4_address, port):
        response = self.__stub.Update(UpdateDeviceRequest(
            deviceID=deviceID,
            info=DeviceInfo(
                ip=ipv4_address,
                port=port,
            ),
        ))
        return response.device

    def delete(self, deviceID):
        response = self.__stub.Delete(DeleteDeviceRequest(deviceID=deviceID))

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()
    
    def close(self):
        self.__channel.close()