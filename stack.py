__all__ = 'Stack',


class Node:
    def __init__(self, value, below):
        assert value is not None, '/value/ cannot be None'
        assert isinstance(below, (type(None), Node))
        self.value = value
        self.below = below
        if below is None:
            self.min = value
        else:
            self.min = min(value, below.min)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


class Stack:
    def __init__(self):
        """
        Creates an empty stack
        """
        self._top = None

    def push(self, item):
        """
        Insert item on top of stack
        :param item: The value that will be stacked
        """
        if item is None:
            raise ValueError('None item not allowed in Stack')
        self._top = Node(item, self._top)

    def pop(self):
        """
        Removes item from the top of stack and returns it. Raises IndexError when the stack is empty
        :return: Item popped from stack
        """
        if self._top is None:
            raise IndexError('pop() from empty stack')
        value, self._top = self._top.value, self._top.below
        return value

    def __len__(self):
        if self._top is None:
            return 0
        return sum(1 for _ in self)

    def __iter__(self):
        current = self._top
        while current is not None:
            yield current.value
            current = current.below

    def peek(self):
        """
        Returns the value on top of the stack or None when the stack is empty
        :return: Topmost value of the stack
        """
        if self._top is None:
            return None
        return self._top.value

    @property
    def min(self):
        """
        Returns the minimum value on the stack in constant time, a.k.a. O(1)
        :return: The minimum value
        """
        if self._top is None:
            return float('nan')
        return self._top.min

    def __str__(self):
        return '[' + ','.join([str(x) for x in self]) + ']'

    def __repr__(self):
        return str(self)
