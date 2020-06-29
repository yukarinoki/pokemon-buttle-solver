import Move
import unittest

class TestMove(unittest.TestCase):

  def test_raw_power(self):
    move = Move.Move("Waza1", "fire", 100)
    self.assertEqual(100, move.raw_power())
  def test_power(self):
    move = Move.Move("Waza1", "fire", 100)
    self.assertEqual(100, move.power)
  def test_calc_power(self):
    move = Move.Move("Waza1", "fire", 100) 
    self.assertEqual(150, move.calc_power(["fire", "ice"]))
  def test_calc_power(self):
    move = Move.Move("Waza1", "fire", 100) 
    self.assertEqual(100, move.calc_power(["leaf", "ice"]))
  
if __name__ == '__main__':
  unittest.main()