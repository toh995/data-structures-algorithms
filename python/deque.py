class Deque:
    def __init__(self):
        self._deque = []

    def is_empty(self):
        return True if len(self._deque) == 0 else False

    def add_front(self, new_value):
        self._deque.insert(0, new_value)

    def add_rear(self, new_value):
        self._deque.append(new_value)

    def remove_front(self):
        if self.is_empty():
            raise EmptyDequeError()
        
        return self._deque.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise EmptyDequeError()

        return self._deque.pop()

    def peek_front(self):
        if self.is_empty():
            raise EmptyDequeError()

        return self._deque[0]

    def peek_rear(self):
        if self.is_empty():
            raise EmptyDequeError()

        return self._deque[-1]

    def size(self):
        return len(self._deque)

    def display_deque(self):
        print(self._deque)

class EmptyDequeError(Exception):
    def __init__(self, message="Deque is empty!"):
        super().__init__(message)