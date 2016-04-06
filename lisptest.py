import unittest
from lispPythonCompiler import evaluator

class TestLispNormalForms(unittest.TestCase):


	def test_addTwoNumbers(self):
		self.assertEqual(evaluator("(+12)"), 3)

	def test_addMultipleNumbers(self):
		self.assertEqual(evaluator("(+123456"), 21)

if __name__ == '__main__':
	unittest.main()
