import unittest

from stack import Stack


class StackTest(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)

        stack.push(-1)
        self.assertEqual(len(stack), 1)

        stack.push(8)
        self.assertEqual(len(stack), 2)

    def test_pop(self):
        stack = Stack()
        stack.push(4)
        popped = stack.pop()
        self.assertEqual(popped, 4)
        self.assertEqual(len(stack), 0)

    def test_min(self):
        import math

        stack = Stack()
        self.assertTrue(math.isnan(stack.min), 'Expected NaN, got ' + str(stack.min))

        stack.push(3)  # [3]
        self.assertEqual(stack.min, 3)

        stack.push(1)  # [1, 3]
        self.assertEqual(stack.min, 1)

        stack.push(10)  # [10, 1, 3]
        self.assertEqual(stack.min, 1)

        stack.push(-4)  # [-4, 10, 1, 3]
        self.assertEqual(stack.min, -4)

        stack.pop()  # [10, 1, 3]
        self.assertEqual(stack.min, 1)

        stack.pop()  # [1, 3]
        self.assertEqual(stack.min, 1)

        stack.pop()  # [3]
        self.assertEqual(stack.min, 3)

        stack.pop()  # []
        self.assertTrue(math.isnan(stack.min), 'Expected NaN, got ' + str(stack.min))

if __name__ == '__main__':
    unittest.main()
