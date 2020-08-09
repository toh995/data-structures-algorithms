class CircularQueue:
    def __init__(self, size):
        self.size = size
        self._queue = [None] * size
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return (self.head == -1) and (self.tail == -1)

    def is_full(self):
        return (self.tail + 1) % self.size == self.head

    def enqueue(self, new_value):
        if self.is_full():
            raise FullCircularQueueError()

        # adjust indexes for head and tail
        if self.is_empty():
            self.head = 0
            self.tail = 0
        
        else:
            self.tail = (self.tail + 1) % self.size
        
        # add the new value to the queue
        self._queue[self.tail] = new_value

    def dequeue(self):
        if self.is_empty():
            raise EmptyCircularQueueError()

        ret = self._queue[self.head]

        # if we are dequeueing the last item from the queue, then put into empty state
        if self.head == self.tail:
            self.head = -1
            self.tail = -1

        # otherwise, adjust the head index normally
        else:
            self.head = (self.head + 1) % self.size

        return ret

    def peek(self):
        if self.is_empty():
            raise EmptyCircularQueueError()

        return self._queue[self.head]

    def display(self):
        display_value = self._get_display_value()
        print(display_value)

    def _get_display_value(self):
        if self.is_empty():
            return []
        
        if self.head <= self.tail:
            start = self.head
            end = self.tail + 1
            return self._queue[start : end]

        else:
            index = self.head
            first_list = self._queue[index:]

            index = self.tail + 1
            second_list = self._queue[:index]

            return first_list + second_list

class EmptyCircularQueueError(Exception):
    def __init__(self, message="Circular Queue is empty!"):
        super().__init__(message)

class FullCircularQueueError(Exception):
    def __init__(self, message="Circular Queue is full!"):
        super().__init__(message)