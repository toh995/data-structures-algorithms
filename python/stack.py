class Stack:
    def __init__(self):
        self._list = []

    def is_empty(self):
        return True if len(self._list) == 0 else False

    def push(self, new_value):
        self._list.append(new_value)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError()

        return self._list.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError()

        return self._list[-1]

    def size(self):
        return len(self._list)

    def display_stack(self):
        print(self._list)

class EmptyStackError(Exception):
    def __init__(self, message="Stack is empty!"):
        super().__init__(message)