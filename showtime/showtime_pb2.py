# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: showtime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eshowtime.proto\"\x18\n\x08showDate\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\".\n\x0cShowTimeData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x10\n\x08moviesId\x18\x02 \x03(\t\"\x07\n\x05\x45mpty2c\n\x08ShowTime\x12)\n\x0bgetShowTime\x12\t.showDate\x1a\r.ShowTimeData\"\x00\x12,\n\x0fgetListShowTime\x12\x06.Empty\x1a\r.ShowTimeData\"\x00\x30\x01\x62\x06proto3')



_SHOWDATE = DESCRIPTOR.message_types_by_name['showDate']
_SHOWTIMEDATA = DESCRIPTOR.message_types_by_name['ShowTimeData']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
showDate = _reflection.GeneratedProtocolMessageType('showDate', (_message.Message,), {
  'DESCRIPTOR' : _SHOWDATE,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:showDate)
  })
_sym_db.RegisterMessage(showDate)

ShowTimeData = _reflection.GeneratedProtocolMessageType('ShowTimeData', (_message.Message,), {
  'DESCRIPTOR' : _SHOWTIMEDATA,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:ShowTimeData)
  })
_sym_db.RegisterMessage(ShowTimeData)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

_SHOWTIME = DESCRIPTOR.services_by_name['ShowTime']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SHOWDATE._serialized_start=18
  _SHOWDATE._serialized_end=42
  _SHOWTIMEDATA._serialized_start=44
  _SHOWTIMEDATA._serialized_end=90
  _EMPTY._serialized_start=92
  _EMPTY._serialized_end=99
  _SHOWTIME._serialized_start=101
  _SHOWTIME._serialized_end=200
# @@protoc_insertion_point(module_scope)
