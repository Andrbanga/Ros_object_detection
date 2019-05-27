# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/eval.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/eval.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_pb=_b('\n\"object_detection/protos/eval.proto\x12\x17object_detection.protos\"\x80\x03\n\nEvalConfig\x12\x1e\n\x12num_visualizations\x18\x01 \x01(\r:\x02\x31\x30\x12\x1a\n\x0cnum_examples\x18\x02 \x01(\r:\x04\x35\x30\x30\x30\x12\x1f\n\x12\x65val_interval_secs\x18\x03 \x01(\r:\x03\x33\x30\x30\x12\x14\n\tmax_evals\x18\x04 \x01(\r:\x01\x30\x12\x19\n\nsave_graph\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\"\n\x18visualization_export_dir\x18\x06 \x01(\t:\x00\x12\x15\n\x0b\x65val_master\x18\x07 \x01(\t:\x00\x12\'\n\x0bmetrics_set\x18\x08 \x01(\t:\x12pascal_voc_metrics\x12\x15\n\x0b\x65xport_path\x18\t \x01(\t:\x00\x12!\n\x12ignore_groundtruth\x18\n \x01(\x08:\x05\x66\x61lse\x12\"\n\x13use_moving_averages\x18\x0b \x01(\x08:\x05\x66\x61lse\x12\"\n\x13\x65val_instance_masks\x18\x0c \x01(\x08:\x05\x66\x61lse')
)




_EVALCONFIG = _descriptor.Descriptor(
  name='EvalConfig',
  full_name='object_detection.protos.EvalConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_visualizations', full_name='object_detection.protos.EvalConfig.num_visualizations', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_examples', full_name='object_detection.protos.EvalConfig.num_examples', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=5000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eval_interval_secs', full_name='object_detection.protos.EvalConfig.eval_interval_secs', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=300,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_evals', full_name='object_detection.protos.EvalConfig.max_evals', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='save_graph', full_name='object_detection.protos.EvalConfig.save_graph', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visualization_export_dir', full_name='object_detection.protos.EvalConfig.visualization_export_dir', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eval_master', full_name='object_detection.protos.EvalConfig.eval_master', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metrics_set', full_name='object_detection.protos.EvalConfig.metrics_set', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("pascal_voc_metrics").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='export_path', full_name='object_detection.protos.EvalConfig.export_path', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignore_groundtruth', full_name='object_detection.protos.EvalConfig.ignore_groundtruth', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_moving_averages', full_name='object_detection.protos.EvalConfig.use_moving_averages', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eval_instance_masks', full_name='object_detection.protos.EvalConfig.eval_instance_masks', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=448,
)

DESCRIPTOR.message_types_by_name['EvalConfig'] = _EVALCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EvalConfig = _reflection.GeneratedProtocolMessageType('EvalConfig', (_message.Message,), dict(
  DESCRIPTOR = _EVALCONFIG,
  __module__ = 'object_detection.protos.eval_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.EvalConfig)
  ))
_sym_db.RegisterMessage(EvalConfig)


# @@protoc_insertion_point(module_scope)
