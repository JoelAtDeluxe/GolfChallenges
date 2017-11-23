import unittest

from golfed import uncollapse

class Tests(unittest.TestCase):
  def test_ex1(self):
    self.assertEqual( uncollapse('three'),  'three')
  
  def test_ex2(self):
    self.assertEqual( uncollapse('eightsix'),  'eight six')
  
  def test_ex3(self):
    self.assertEqual( uncollapse('fivefourseven'),  'five four seven')
  
  def test_ex4(self):
    self.assertEqual( uncollapse('ninethreesixthree'),  'nine three six three')
  
  def test_ex5(self):
    self.assertEqual( uncollapse('foursixeighttwofive'),  'four six eight two five')
  
  def test_ex6(self):
    self.assertEqual( uncollapse('fivethreefivesixthreenineonesevenoneeight'),  'five three five six three nine one seven one eight')
  
  def test_ex7(self):
    self.assertEqual( uncollapse('threesevensevensixninenineninefiveeighttwofiveeightsixthreeeight'),  'three seven seven six nine nine nine five eight two five eight six three eight')

  def test_ex8(self):
    self.assertEqual( uncollapse('zeroonetwothreefourfivesixseveneightnine'),  'zero one two three four five six seven eight nine')


if __name__ == '__main__':
  unittest.main()









