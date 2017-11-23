import unittest

from full import determine_turkeys 

class Tests(unittest.TestCase):
  def test_example(self):
    self.assertEqual( determine_turkeys(3, 6, 3), 2 )
  
  def test_all_any(self):
    self.assertEqual( determine_turkeys(0, 0, 20), 3 )

  def test_all_white(self):
    self.assertEqual( determine_turkeys(20, 0, 0), 5 )
  
  def test_all_dark(self):
    self.assertEqual( determine_turkeys(0, 20, 0), 7 )

  def test_perfect(self):
    self.assertEqual( determine_turkeys(4, 3, 0), 1 )

  def test_alone(self):
    self.assertEqual( determine_turkeys(0, 0, 0), 0 )

  def test_big(self):
    self.assertEqual( determine_turkeys(20, 20, 20), 9 )

  def test_fractional(self):
    self.assertEqual( determine_turkeys(3, 2, 1), 1 )

  def test_fractional2(self):
    self.assertEqual( determine_turkeys(5, 4, 10), 3 )

if __name__ == '__main__':
  unittest.main()
