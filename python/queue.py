class Queue:
    def __init__(self):
        self._queue = []

    def is_empty(self):
        return True if len(self._queue) == 0 else False

    def enqueue(self, new_value):
        self._queue.append(new_value)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError()

        return self._queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError()

        return self._queue[0]

    def size(self):
        return len(self._queue)

    def display_queue(self):
        print(self._queue)

class EmptyQueueError(Exception):
    def __init__(self, message="Queue is empty!"):
        super().__init__(message)