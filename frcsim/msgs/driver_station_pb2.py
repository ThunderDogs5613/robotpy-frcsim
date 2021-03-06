# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: driver-station.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='driver-station.proto',
  package='gazebo.msgs',
  serialized_pb=_b('\n\x14\x64river-station.proto\x12\x0bgazebo.msgs\"z\n\rDriverStation\x12\x0f\n\x07\x65nabled\x18\x01 \x02(\x08\x12/\n\x05state\x18\x02 \x02(\x0e\x32 .gazebo.msgs.DriverStation.State\"\'\n\x05State\x12\x08\n\x04\x41UTO\x10\x00\x12\n\n\x06TELEOP\x10\x01\x12\x08\n\x04TEST\x10\x02\x42\x11\x42\x0fGzDriverStation')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DRIVERSTATION_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='gazebo.msgs.DriverStation.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TELEOP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=120,
  serialized_end=159,
)
_sym_db.RegisterEnumDescriptor(_DRIVERSTATION_STATE)


_DRIVERSTATION = _descriptor.Descriptor(
  name='DriverStation',
  full_name='gazebo.msgs.DriverStation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='gazebo.msgs.DriverStation.enabled', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='gazebo.msgs.DriverStation.state', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DRIVERSTATION_STATE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=159,
)

_DRIVERSTATION.fields_by_name['state'].enum_type = _DRIVERSTATION_STATE
_DRIVERSTATION_STATE.containing_type = _DRIVERSTATION
DESCRIPTOR.message_types_by_name['DriverStation'] = _DRIVERSTATION

DriverStation = _reflection.GeneratedProtocolMessageType('DriverStation', (_message.Message,), dict(
  DESCRIPTOR = _DRIVERSTATION,
  __module__ = 'driver_station_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.DriverStation)
  ))
_sym_db.RegisterMessage(DriverStation)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\017GzDriverStation'))
# @@protoc_insertion_point(module_scope)
