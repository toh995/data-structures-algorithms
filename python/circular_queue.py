class CircularQueue:
    def __init__(self, size):
        self._size = size
        self._queue = [None] * size
        self._head = -1
        self._tail = -1

    def is_empty(self):
        return (self._head == -1) and (self._tail == -1)

    def is_full(self):
        return (self._tail + 1) % self._size == self._head

    def enqueue(self, new_value):
        if self.is_full():
            raise FullCircularQueueError()

        # adjust indexes for head and tail
        if self.is_empty():
            self._head = 0
            self._tail = 0
        
        else:
            self._tail = (self._tail + 1) % self._size
        
        # add the new value to the queue
        self._queue[self._tail] = new_value

    def dequeue(self):
        if self.is_empty():
            raise EmptyCircularQueueError()

        ret = self._queue[self._head]

        # if we are dequeueing the last item from the queue, then put into empty state
        if self._head == self._tail:
            self._head = -1
            self._tail = -1

        # otherwise, adjust the head index normally
        else:
            self._head = (self._head + 1) % self._size

        return ret

    def peek(self):
        if self.is_empty():
            raise EmptyCircularQueueError()

        return self._queue[self._head]

    def display(self):
        display_value = self._get_display_value()
        print(display_value)

    def _get_display_value(self):
        if self.is_empty():
            return []
        
        if self._head <= self._tail:
            start = self._head
            end = self._tail + 1
            return self._queue[start : end]

        else:
            index = self._head
            first_list = self._queue[index:]

            index = self._tail + 1
            second_list = self._queue[:index]

            return first_list + second_list

class EmptyCircularQueueError(Exception):
    def __init__(self, message="Circular Queue is empty!"):
        super().__init__(message)

class FullCircularQueueError(Exception):
    def __init__(self, message="Circular Queue is full!"):
        super().__init__(message)