class World:
  def __init__(self, world, flag, eventmsg, exprate, droprate, mesorate, bossdroprate):
    self.world = world
    self.flag = flag
    self.eventmsg = eventmsg
    self.exprate = exprate
    self.droprate = droprate
    self.mesorate = mesorate
    self.bossdroprate = bossdroprate
    self.channels = []