from ..constants.serverconstants import *
from .serverhandler import MapleServerFactory
from .world import World
from twisted.internet import reactor

class Server:
  worlds = []

  def run(self):
    for i, world in enumerate(WORLDS):
      self.worlds.append(World(i, **world))
      for channel in range(CHANNELS):
        port = 7575 + channel
        port += i * 100
        reactor.listenTCP(port, MapleServerFactory(i, channel))
    reactor.listenTCP(8484, MapleServerFactory())
    reactor.run()