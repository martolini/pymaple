from twisted.internet import reactor, protocol, task
import random
import struct
from mapleclient import MapleClient

class MapleServerFactory(protocol.Factory):
  def __init__(self, world=-1, channel=-1):
    self.world = world
    self.channel = channel

  def buildProtocol(self, addr):
    return MapleServerHandler(factory=self)


class MapleServerHandler(protocol.Protocol):
  def __init__(self, factory):
    self.factory = factory

  def unpack_header(self, header):
    return struct.unpack('!i', header)

  def dataReceived(self, data):
    header = data[:4]
    # Do nothing with header so far
    body = data[4:]
    parsed_body = list(struct.unpack('!%sB' % len(body), body))
    decoded = self.client.decoder.decode(parsed_body)
    print decoded
    if decoded[0] == 35:
      lc = task.LoopingCall(self.send_heartbeat)
      lc.start(20, now=False)


  def connectionMade(self):
    print 'Made a connection'
    self.client = MapleClient()
    data = struct.pack(
      '<hhhBBBBBBBBBB', 0x0E, 83, 1, 49, *(self.client.decoder.receive + self.client.decoder.send + [8])
    )
    self.transport.write(data)

  def send_heartbeat(self):
    data = self.client.decoder.encode([17, 0])
    print 'Sending ', data
    self.transport.write(struct.pack('<6B', *data))


  def connectionLost(self, reason):
    print 'Lost conn {}'.format(reason)
