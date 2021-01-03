"""
    catheter_path_service_client.py
    ~~~~~~~~~~

    Interacts with the catheter path service.

    :copyright: 2019 Pyrus
"""

import logging
import grpc
import threading
import uuid

from google.protobuf.timestamp_pb2 import Timestamp

from dopltech.protos.catheter_path_service_pb2_grpc import CatheterPathServiceStub
from dopltech.protos.catheter_path_service_pb2 import (
    CatheterPath,
    CreateCatheterPathRequest,
)

class CatheterPathServiceClient:
    def __init__(self, host, port):
        server_address = "{}:{}".format(host, port)

        print("Connecting to catheter path service @ " + server_address)
        self.__channel = grpc.insecure_channel(server_address)
        self.__stub = CatheterPathServiceStub(self.__channel)
    
    def create(self, name, start_catheter_data_id, end_catheter_data_id):
        print("Creating catheter path '{}' [{}, {}]".format(name, start_catheter_data_id, end_catheter_data_id))
        created = Timestamp()
        created.GetCurrentTime()
        path = CatheterPath(
            name=name,
            startCatheterDataID=start_catheter_data_id,
            endCatheterDataID=end_catheter_data_id,
            created=created,
        )
        request = CreateCatheterPathRequest(path=path)
        response = self.__stub.Create(request)
        return response.id

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()
    
    def close(self):
        self.__channel.close()