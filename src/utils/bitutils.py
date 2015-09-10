class BitUtils:
  @staticmethod
  def roll_left(inn, count):
    tmp = inn & 0xFF
    tmp = tmp << (count % 8)
    return ((tmp & 0xFF) | (tmp >> 8))

  @staticmethod
  def roll_right(inn, count):
    tmp = inn & 0xFF
    tmp = (tmp << 8) >> (count % 8)
    return (tmp & 0xFF) | (tmp >> 8)

  @staticmethod
  def unsigned_right_shift(num, arg):
    return (num % 0x100000000) >> arg
