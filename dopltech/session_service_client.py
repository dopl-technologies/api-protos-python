import logging
import grpc
import os

from dopltech.device_service_client import DeviceServiceClient

from dopltech.protos.session_service_pb2_grpc import SessionServiceStub
from dopltech.protos.session_service_pb2 import (
    CreateSessionRequest,
    GetSessionRequest,
    JoinSessionRequest,
    ListSessionsRequest,
    ListWaitingSessionRequest,
    WaitForSessionRequest,
)

class SessionServiceClient:
    def __init__(self, host, port):
        server_address = "{}:{}".format(host, port)

        print("Connecting to session service @ " + server_address)
        self.__channel = grpc.insecure_channel(server_address)
        self.__stub = SessionServiceStub(self.__channel)
    
    def get(self, session_id):
        logging.info("Getting session {}".format(session_id))
        request = GetSessionRequest(sessionID=session_id)
        response = self.__stub.Get(request)
        return response.session

    def list(self):
        logging.info("Listing sessions")
        responses = self.__stub.List(ListSessionsRequest())

        platform_sessions = []
        for response in responses:
            platform_sessions.append(response.session)
        
        logging.info("Retrieved {} sessions".format(len(platform_sessions)))
        return platform_sessions

    def list_waiting(self):
        logging.info("Getting waiting devices")
        responses = self.__stub.ListWaiting(ListWaitingSessionRequest())

        waitingDevices = []
        for response in responses:
            waitingDevices.append(response.device)

        return waitingDevices

    def create(self, name, deviceIDs):
        req = CreateSessionRequest(name=name, deviceIDs=deviceIDs)
        self.__stub.Create(req)

    def wait_for(self, deviceID):
        logging.info("Waiting for session")
        waitResponses = self.__stub.WaitFor(WaitForSessionRequest(deviceID=deviceID))
        for response in waitResponses:
            logging.info("Session {} created".format(response.sessionID))
            return response.sessionID

    def join_session(self, deviceID, sessionID, session_device_callback, joined_callback=None):
        logging.info("Joining session {}".format(sessionID))
        joinResponses = self.__stub.Join(JoinSessionRequest(deviceID=deviceID, sessionID=sessionID))

        if joined_callback:
            joined_callback(sessionID)

        for response in joinResponses:
            logging.info("Device {} status changed".format(response.sessionDevice.device.id))
            session_device_callback(response.sessionDevice)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.__channel.close()