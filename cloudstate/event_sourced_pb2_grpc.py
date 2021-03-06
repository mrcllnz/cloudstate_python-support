# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from cloudstate import event_sourced_pb2 as cloudstate_dot_event__sourced__pb2


class EventSourcedStub(object):
  """The Entity service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.handle = channel.stream_stream(
        '/cloudstate.eventsourced.EventSourced/handle',
        request_serializer=cloudstate_dot_event__sourced__pb2.EventSourcedStreamIn.SerializeToString,
        response_deserializer=cloudstate_dot_event__sourced__pb2.EventSourcedStreamOut.FromString,
        )


class EventSourcedServicer(object):
  """The Entity service
  """

  def handle(self, request_iterator, context):
    """The stream. One stream will be established per active entity.
    Once established, the first message sent will be Init, which contains the entity ID, and,
    if the entity has previously persisted a snapshot, it will contain that snapshot. It will
    then send zero to many event messages, one for each event previously persisted. The entity
    is expected to apply these to its state in a deterministic fashion. Once all the events
    are sent, one to many commands are sent, with new commands being sent as new requests for
    the entity come in. The entity is expected to reply to each command with exactly one reply
    message. The entity should reply in order, and any events that the entity requests to be
    persisted the entity should handle itself, applying them to its own state, as if they had
    arrived as events when the event stream was being replayed on load.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EventSourcedServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'handle': grpc.stream_stream_rpc_method_handler(
          servicer.handle,
          request_deserializer=cloudstate_dot_event__sourced__pb2.EventSourcedStreamIn.FromString,
          response_serializer=cloudstate_dot_event__sourced__pb2.EventSourcedStreamOut.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cloudstate.eventsourced.EventSourced', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
