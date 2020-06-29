import Pokemon
import unittest

class TestPokemon(unittest.TestCase):

  def test_addmove(self):
    poke = Pokemon.Pokemon("pikachu", ["electric"], 100,100,100,100,100,100)
    poke.add_move("waza1", "electric", 100)
    self.assertEqual(1, len(poke.moves))
    poke.add_move("waza2", "fire", 100)
    self.assertEqual(2, len(poke.moves))
  def test_power(self):
    poke = Pokemon.Pokemon("pikachu", "electric", 100,100,100,100,100,100)
    poke.add_move("waza1", "electric", 100)
    poke.add_move("waza2", "fire", 100)
    self.assertEqual(150, poke.power(0))
    self.assertEqual(100, poke.power(1))
  
if __name__ == '__main__':
  unittest.main()