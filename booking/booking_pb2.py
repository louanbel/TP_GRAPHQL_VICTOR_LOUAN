# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\"-\n\x0bJsonBooking\x12\x1e\n\x08\x62ookings\x18\x01 \x03(\x0b\x32\x0c.BookingData\"*\n\x0fResponseMessage\x12\x17\n\x0fresponseMessage\x18\x01 \x01(\t\"\x18\n\x06UserId\x12\x0e\n\x06userid\x18\x01 \x01(\t\"9\n\x0b\x42ookingData\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x1a\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\x0b.DateBooked\"*\n\nDateBooked\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\";\n\nSingleBook\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0f\n\x07movieid\x18\x03 \x01(\t\"\x08\n\x06\x45mpty42\x91\x01\n\x07\x42ooking\x12\"\n\x07GetJson\x12\x07.Empty4\x1a\x0c.JsonBooking\"\x00\x12,\n\x11GetBookingForUser\x12\x07.UserId\x1a\x0c.BookingData\"\x00\x12\x34\n\x11\x41\x64\x64\x42ookingForUser\x12\x0b.SingleBook\x1a\x10.ResponseMessage\"\x00\x62\x06proto3')



_JSONBOOKING = DESCRIPTOR.message_types_by_name['JsonBooking']
_RESPONSEMESSAGE = DESCRIPTOR.message_types_by_name['ResponseMessage']
_USERID = DESCRIPTOR.message_types_by_name['UserId']
_BOOKINGDATA = DESCRIPTOR.message_types_by_name['BookingData']
_DATEBOOKED = DESCRIPTOR.message_types_by_name['DateBooked']
_SINGLEBOOK = DESCRIPTOR.message_types_by_name['SingleBook']
_EMPTY4 = DESCRIPTOR.message_types_by_name['Empty4']
JsonBooking = _reflection.GeneratedProtocolMessageType('JsonBooking', (_message.Message,), {
  'DESCRIPTOR' : _JSONBOOKING,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:JsonBooking)
  })
_sym_db.RegisterMessage(JsonBooking)

ResponseMessage = _reflection.GeneratedProtocolMessageType('ResponseMessage', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEMESSAGE,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:ResponseMessage)
  })
_sym_db.RegisterMessage(ResponseMessage)

UserId = _reflection.GeneratedProtocolMessageType('UserId', (_message.Message,), {
  'DESCRIPTOR' : _USERID,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:UserId)
  })
_sym_db.RegisterMessage(UserId)

BookingData = _reflection.GeneratedProtocolMessageType('BookingData', (_message.Message,), {
  'DESCRIPTOR' : _BOOKINGDATA,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:BookingData)
  })
_sym_db.RegisterMessage(BookingData)

DateBooked = _reflection.GeneratedProtocolMessageType('DateBooked', (_message.Message,), {
  'DESCRIPTOR' : _DATEBOOKED,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:DateBooked)
  })
_sym_db.RegisterMessage(DateBooked)

SingleBook = _reflection.GeneratedProtocolMessageType('SingleBook', (_message.Message,), {
  'DESCRIPTOR' : _SINGLEBOOK,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:SingleBook)
  })
_sym_db.RegisterMessage(SingleBook)

Empty4 = _reflection.GeneratedProtocolMessageType('Empty4', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY4,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:Empty4)
  })
_sym_db.RegisterMessage(Empty4)

_BOOKING = DESCRIPTOR.services_by_name['Booking']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _JSONBOOKING._serialized_start=17
  _JSONBOOKING._serialized_end=62
  _RESPONSEMESSAGE._serialized_start=64
  _RESPONSEMESSAGE._serialized_end=106
  _USERID._serialized_start=108
  _USERID._serialized_end=132
  _BOOKINGDATA._serialized_start=134
  _BOOKINGDATA._serialized_end=191
  _DATEBOOKED._serialized_start=193
  _DATEBOOKED._serialized_end=235
  _SINGLEBOOK._serialized_start=237
  _SINGLEBOOK._serialized_end=296
  _EMPTY4._serialized_start=298
  _EMPTY4._serialized_end=306
  _BOOKING._serialized_start=309
  _BOOKING._serialized_end=454
# @@protoc_insertion_point(module_scope)
