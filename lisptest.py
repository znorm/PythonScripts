import unittest
from lispPythonInterp import evaluator

class TestLispNormalForms(unittest.TestCase):


	def test_addTwoNumbers(self):
		self.assertEqual(evaluator("(+12)"), 3)

if __name__ == '__main__':
	unittest.main()
