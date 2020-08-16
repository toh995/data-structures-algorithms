import pytest
from python.deque import Deque, EmptyDequeError

class TestDeque:
    """Deque"""

    @pytest.fixture()
    def new_deque(self):
        def ret(size):
            deque = Deque()
            for i in range(size):
                deque.add_rear(i)
            return deque
        
        return ret
    
    def test_is_empty_returns_true(self, new_deque):
        """is_empty() should return True if it's empty"""
        deque = new_deque(size=0)
        assert deque.is_empty() == True

    @pytest.mark.parametrize("size", range(1, 11))
    def test_is_empty_returns_false(self, new_deque, size):
        """is_empty() should return False if it's not empty"""
        deque = new_deque(size)
        assert deque.is_empty() == False

    def test_add_front_increases_size(self, new_deque):
        """should increase in size every time you add to the front"""
        deque = new_deque(size=0)
        for i in range(1, 11):
            deque.add_front(i)
            assert i == deque.size()

    def test_add_rear_increases_size(self, new_deque):
        """should increase in size every time you add to the rear"""
        deque = new_deque(size=0)
        for i in range(1, 11):
            deque.add_rear(i)
            assert i == deque.size()

    def test_remove_front_decreases_size(self, new_deque):
        """should decrease in size every time you remove from the front"""
        DEQUE_SIZE = 10
        deque = new_deque(DEQUE_SIZE)

        curr_size = deque.size()

        for _ in range(DEQUE_SIZE):
            deque.remove_front()
            curr_size -= 1
            assert curr_size == deque.size()

    def test_remove_rear_decreases_size(self, new_deque):
        """should decrease in size every time you remove from the rear"""
        DEQUE_SIZE = 10
        deque = new_deque(DEQUE_SIZE)

        curr_size = deque.size()

        for _ in range(DEQUE_SIZE):
            deque.remove_rear()
            curr_size -= 1
            assert curr_size == deque.size()

    def test_remove_front_returns_front_value_after_add_front(self):
        """remove_front() should return the front value in the deque after adding to the front"""
        DEQUE_SIZE = 10
        deque = Deque()

        r = range(DEQUE_SIZE)
        for i in r:
            deque.add_front(i)

        for i in reversed(r):
            assert i == deque.remove_front()

    def test_remove_front_returns_front_value_after_add_rear(self):
        """remove_front() should return the front value in the deque after adding to the rear"""
        DEQUE_SIZE = 10
        deque = Deque()

        r = range(DEQUE_SIZE)
        for i in r:
            deque.add_rear(i)

        for i in r:
            assert i == deque.remove_front()

    def test_remove_rear_returns_rear_value_after_add_front(self):
        """remove_rear() should return the rear value in the deque after adding to the front"""
        deque = Deque()

        r = range(10)
        for i in r:
            deque.add_front(i)

        for i in r:
            assert i == deque.remove_rear()

    def test_remove_rear_returns_rear_value_after_add_rear(self):
        """remove_rear() should return the rear value in the deque after adding to the rear"""
        deque = Deque()

        r = range(10)
        for i in r:
            deque.add_rear(i)

        for i in reversed(r):
            assert i == deque.remove_rear()

    def test_remove_front_raises_EmptyDequeError_if_empty(self, new_deque):
        """remove_front() should raise an EmptyDequeError if the deque is empty"""
        deque = new_deque(size=0)
        with pytest.raises(EmptyDequeError):
            deque.remove_front()

    def test_remove_rear_raises_EmptyDequeError_if_empty(self, new_deque):
        """remove_rear() should raise an EmptyDequeError if the deque is empty"""
        deque = new_deque(size=0)
        with pytest.raises(EmptyDequeError):
            deque.remove_rear()

    def test_peek_front_returns_front_value_after_add_front(self, new_deque):
        """peek_front() should return the front value in the deque after adding to the front"""
        DEQUE_SIZE = 10
        deque = Deque()

        r = range(DEQUE_SIZE)
        for i in r:
            deque.add_front(i)

        assert r[-1] == deque.peek_front()

    def test_peek_front_returns_front_value_after_add_rear(self, new_deque):
        """peek_front() should return the front value in the deque after adding to the rear"""
        DEQUE_SIZE = 10
        deque = Deque()

        r = range(DEQUE_SIZE)
        for i in r:
            deque.add_rear(i)

        assert r[0] == deque.peek_front()

    def test_peek_rear_returns_rear_value_after_add_front(self, new_deque):
        """peek_rear() should return the rear value in the deque after adding to the front"""
        DEQUE_SIZE = 10
        deque = Deque()

        r = range(DEQUE_SIZE)
        for i in r:
            deque.add_front(i)

        assert r[0] == deque.peek_rear()

    def test_peek_rear_returns_rear_value_after_add_rear(self, new_deque):
        """peek_rear() should return the rear value in the deque after adding to the rear"""
        DEQUE_SIZE = 10
        deque = Deque()

        r = range(DEQUE_SIZE)
        for i in r:
            deque.add_rear(i)

        assert r[-1] == deque.peek_rear()

    @pytest.mark.parametrize("size", range(1, 11))
    def test_peek_front_does_not_change_size(self, new_deque, size):
        """peek_front() should not change the deque size"""
        deque = new_deque(size)
        deque.peek_front()
        assert size == deque.size()

    @pytest.mark.parametrize("size", range(1, 11))
    def test_peek_rear_does_not_change_size(self, new_deque, size):
        """peek_rear() should not change the deque size"""
        deque = new_deque(size)
        deque.peek_rear()
        assert size == deque.size()

    def test_peek_front_raises_EmptyDequeError_if_empty(self, new_deque):
        """peek_front() should raise an EmptyDequeError if the deque is empty"""
        deque = new_deque(size=0)
        with pytest.raises(EmptyDequeError):
            deque.peek_front()

    def test_peek_rear_raises_EmptyDequeError_if_empty(self, new_deque):
        """peek_rear() should raise an EmptyDequeError if the deque is empty"""
        deque = new_deque(size=0)
        with pytest.raises(EmptyDequeError):
            deque.peek_rear()

    def test_size_returns_zero_if_empty_deque(self, new_deque):
        """size() should return 0 if the deque is empty"""
        deque = new_deque(size=0)
        assert 0 == deque.size()