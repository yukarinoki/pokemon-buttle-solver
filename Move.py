
class Move:
  def __init__(self, name, move_type, power):
    self.name = name
    self.move_type = move_type
    self.power = power
  
  def raw_power(self):
    return self.power
  
  def calc_power(self, pokemon_types):
    same = False
    if self.move_type in pokemon_types:
      return self.power * 1.5
    else :
      return self.power
  def move_print(self):
    print(self.name)
    print(self.move_type)
    print(self.power)
  