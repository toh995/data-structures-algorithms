import pytest
from python.queue import Queue, EmptyQueueError

class TestQueue:
    """Queue"""

    @pytest.fixture()
    def new_queue(self):
        def ret(size):
            queue = Queue()
            for i in range(size):
                queue.enqueue(i)
            return queue
        
        return ret
    
    def test_is_empty_returns_true(self, new_queue):
        """is_empty() should return True if it's empty"""
        queue = new_queue(size=0)
        assert queue.is_empty() == True

    @pytest.mark.parametrize("size", range(1, 11))
    def test_is_empty_returns_false(self, new_queue, size):
        """is_empty() should return False if it's not empty"""
        queue = new_queue(size)
        assert queue.is_empty() == False

    def test_enqueue_increases_size(self, new_queue):
        """should increase in size every time you enqueue"""
        queue = new_queue(size=0)
        for i in range(1, 11):
            queue.enqueue(i)
            assert i == queue.size()

    def test_dequeue_decreases_size(self, new_queue):
        """should decrease in size every time you dequeue"""
        QUEUE_SIZE = 10
        queue = new_queue(QUEUE_SIZE)

        curr_size = queue.size()

        for _ in range(QUEUE_SIZE):
            queue.dequeue()
            curr_size -= 1
            assert curr_size == queue.size()

    def test_dequeue_returns_first_value(self):
        """dequeue() should return the first value in the queue"""
        queue = Queue()

        r = range(10)
        for i in r:
            queue.enqueue(i)

        for i in r:
            assert i == queue.dequeue()

    def test_dequeue_raises_EmptyQueueError_if_empty(self, new_queue):
        """dequeue() should raise an EmptyQueueError if the queue is empty"""
        queue = new_queue(size=0)
        with pytest.raises(EmptyQueueError):
            queue.dequeue()

    def test_peek_returns_first_value(self, new_queue):
        """peek() should return the first value in the queue"""
        queue = Queue()

        r = range(10)
        for i in r:
            queue.enqueue(i)

        assert r[0] == queue.peek()

    @pytest.mark.parametrize("size", range(1, 11))
    def test_peek_does_not_change_size(self, new_queue, size):
        """peek() should not change the queue size"""
        queue = new_queue(size)
        queue.peek()
        assert size == queue.size()

    def test_peek_raises_EmptyQueueError_if_empty(self, new_queue):
        """peek() should raise an EmptyQueueError if the queue is empty"""
        queue = new_queue(size=0)
        with pytest.raises(EmptyQueueError):
            queue.peek()