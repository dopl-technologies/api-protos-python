# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state_manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='state_manager.proto',
  package='dopltechnologies.protos',
  syntax='proto3',
  serialized_options=b'Z3github.com/dopl-technologies/api-protos-go;dtprotos\252\002\027DoplTechnologies.Protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13state_manager.proto\x12\x17\x64opltechnologies.protos\x1a\x0c\x63ommon.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"p\n\x13RecordFramesRequest\x12,\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1e.dopltechnologies.protos.Frame\x12+\n\x07\x63reated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x16\n\x14RecordFramesResponse2\x84\x01\n\x13StateManagerService\x12m\n\x0cRecordFrames\x12,.dopltechnologies.protos.RecordFramesRequest\x1a-.dopltechnologies.protos.RecordFramesResponse(\x01\x42OZ3github.com/dopl-technologies/api-protos-go;dtprotos\xaa\x02\x17\x44oplTechnologies.Protosb\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_RECORDFRAMESREQUEST = _descriptor.Descriptor(
  name='RecordFramesRequest',
  full_name='dopltechnologies.protos.RecordFramesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='dopltechnologies.protos.RecordFramesRequest.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created', full_name='dopltechnologies.protos.RecordFramesRequest.created', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=207,
)


_RECORDFRAMESRESPONSE = _descriptor.Descriptor(
  name='RecordFramesResponse',
  full_name='dopltechnologies.protos.RecordFramesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=231,
)

_RECORDFRAMESREQUEST.fields_by_name['data'].message_type = common__pb2._FRAME
_RECORDFRAMESREQUEST.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['RecordFramesRequest'] = _RECORDFRAMESREQUEST
DESCRIPTOR.message_types_by_name['RecordFramesResponse'] = _RECORDFRAMESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecordFramesRequest = _reflection.GeneratedProtocolMessageType('RecordFramesRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECORDFRAMESREQUEST,
  '__module__' : 'state_manager_pb2'
  # @@protoc_insertion_point(class_scope:dopltechnologies.protos.RecordFramesRequest)
  })
_sym_db.RegisterMessage(RecordFramesRequest)

RecordFramesResponse = _reflection.GeneratedProtocolMessageType('RecordFramesResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECORDFRAMESRESPONSE,
  '__module__' : 'state_manager_pb2'
  # @@protoc_insertion_point(class_scope:dopltechnologies.protos.RecordFramesResponse)
  })
_sym_db.RegisterMessage(RecordFramesResponse)


DESCRIPTOR._options = None

_STATEMANAGERSERVICE = _descriptor.ServiceDescriptor(
  name='StateManagerService',
  full_name='dopltechnologies.protos.StateManagerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=234,
  serialized_end=366,
  methods=[
  _descriptor.MethodDescriptor(
    name='RecordFrames',
    full_name='dopltechnologies.protos.StateManagerService.RecordFrames',
    index=0,
    containing_service=None,
    input_type=_RECORDFRAMESREQUEST,
    output_type=_RECORDFRAMESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATEMANAGERSERVICE)

DESCRIPTOR.services_by_name['StateManagerService'] = _STATEMANAGERSERVICE

# @@protoc_insertion_point(module_scope)
