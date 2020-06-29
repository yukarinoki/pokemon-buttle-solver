import Move

class Pokemon:
  def __init__(self, name, types, hp,atk, defe, spa,spd,spe, moves = []) :
    self.name = name
    self.types = types
    self.hp = hp
    self.atk = atk
    self.spa = spa
    self.spd = spd
    self.spe = spe
    self.moves = moves
  
  def add_move(self, move_name, move_type, move_power):
    self.moves.append(Move.Move(move_name, move_type, move_power))
  def power(self, move_id):
    return self.moves[move_id].calc_power(self.types)
  def print_pokemon(self):
    print(self.name)
    print(self.types)
    print("Status:")
    print(self.hp)
    print(self.atk)
    print(self.spa)
    print(self.spd)
    print(self.spe)
    print(self.moves)

