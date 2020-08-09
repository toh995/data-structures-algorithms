import pytest
import math
from python.circular_queue import CircularQueue, EmptyCircularQueueError, FullCircularQueueError

class TestCircularQueue:
    """CircularQueue"""

    @pytest.fixture(params=range(1, 11))
    def size(self, request):
        return request.param

    def test_is_empty_returns_true_upon_initialization(self, size):
        """is_empty() should return True upon initialization"""
        circular_queue = CircularQueue(size)
        assert circular_queue.is_empty() == True

    def test_is_empty_returns_true_after_dequeueing(self, size):
        """is_empty() should return True after filling the queue and dequeueing it"""
        circular_queue = CircularQueue(size)

        for i in range(size):
            circular_queue.enqueue(i)

        for i in range(size):
            circular_queue.dequeue()

        assert circular_queue.is_empty() == True

    def test_is_empty_returns_false(self, size):
        """is_empty() should return False if it's not empty"""
        circular_queue = CircularQueue(size)
        for i in range(size):
            circular_queue.enqueue(i)

        for _ in range(size):
            assert circular_queue.is_empty() == False
            circular_queue.dequeue()

    def test_is_full_returns_true(self, size):
        """is_full() should return True if it's full"""
        circular_queue = CircularQueue(size)
        
        for i in range(size):
            circular_queue.enqueue(i)

        assert circular_queue.is_full() == True

    def test_is_full_returns_false(self, size):
        """is_full() should return False if it's not full"""
        circular_queue = CircularQueue(size)
        for i in range(size):
            assert circular_queue.is_full() == False
            circular_queue.enqueue(i)

    def test_enqueue_raises_FullCircularQueueError_if_full(self, size):
        """enqueue() should raise a FullCircularQueueError if the circular queue is full"""
        circular_queue = CircularQueue(size)
        
        for i in range(size):
            circular_queue.enqueue(i)
        
        with pytest.raises(FullCircularQueueError):
            circular_queue.enqueue("abc")

    def test_dequeue_returns_first_value(self, size):
        """dequeue() should return the first value in the queue"""
        circular_queue = CircularQueue(size)

        list1 = [i for i in range(size)]
        list2 = [str(i) for i in list1]

        half_index = len(list1) / 2
        half_index = math.floor(half_index)

        # enqueue list1
        for i in list1:
            circular_queue.enqueue(i)

        # dequeue the first half of list1
        for i in list1[:half_index]:
            assert i == circular_queue.dequeue()

        # enqueue the first half of list2
        for i in list2[:half_index]:
            circular_queue.enqueue(i)

        # dequeue the second half of list1
        for i in list1[half_index:]:
            assert i == circular_queue.dequeue()

        # dequeue the first half of list2
        for i in list2[:half_index]:
            assert i == circular_queue.dequeue()

    def test_dequeue_raises_EmptyCircularQueueError_if_not_enqueued(self, size):
        """dequeue() should raise an EmptyCircularQueueError if nothing has been enqueued yet"""
        circular_queue = CircularQueue(size)
        with pytest.raises(EmptyCircularQueueError):
            circular_queue.dequeue()

    def test_dequeue_raises_EmptyCircularQueueError_after_complete_dequeue(self, size):
        """dequeue() should raise an EmptyCircularQueueError if the circular queue has been completely dequeued"""
        circular_queue = CircularQueue(size)
        
        for i in range(size):
            circular_queue.enqueue(i)

        for i in range(size):
            circular_queue.dequeue()

        with pytest.raises(EmptyCircularQueueError):
            circular_queue.dequeue()

    def test_peek_returns_first_value(self, size):
        """peek() should return the first value in the queue"""
        circular_queue = CircularQueue(size)

        list1 = [i for i in range(size)]
        list2 = [str(i) for i in list1]

        half_index = len(list1) / 2
        half_index = math.floor(half_index)

        # enqueue list1
        for i in list1:
            circular_queue.enqueue(i)

        # dequeue the first half of list1
        for i in list1[:half_index]:
            assert i == circular_queue.peek()
            circular_queue.dequeue()

        # enqueue the first half of list2
        for i in list2[:half_index]:
            circular_queue.enqueue(i)

        # dequeue the second half of list1
        for i in list1[half_index:]:
            assert i == circular_queue.peek()
            circular_queue.dequeue()

        # dequeue the first half of list2
        for i in list2[:half_index]:
            assert i == circular_queue.peek()
            circular_queue.dequeue()


    def test_peek_raises_EmptyCircularQueueError_if_not_enqueued(self, size):
        """peek() should raise an EmptyCircularQueueError if nothing has been enqueued yet"""
        circular_queue = CircularQueue(size)
        with pytest.raises(EmptyCircularQueueError):
            circular_queue.peek()

    def test_peek_raises_EmptyCircularQueueError_after_complete_dequeue(self, size):
        """peek() should raise an EmptyCircularQueueError if the circular queue has been completely dequeued"""
        circular_queue = CircularQueue(size)
        
        for i in range(size):
            circular_queue.enqueue(i)

        for i in range(size):
            circular_queue.dequeue()

        with pytest.raises(EmptyCircularQueueError):
            circular_queue.peek()
