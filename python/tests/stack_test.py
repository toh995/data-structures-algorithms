import pytest
from python.stack import Stack, EmptyStackError

class TestStack:
    """Stack"""

    @pytest.fixture()
    def new_stack(self):
        def ret(size):
            stack = Stack()
            for i in range(size):
                stack.push(i)
            return stack
        
        return ret
    
    def test_is_empty_returns_true(self, new_stack):
        """is_empty() should return True if it's empty"""
        stack = new_stack(size=0)
        assert stack.is_empty() == True

    @pytest.mark.parametrize("size", range(1, 11))
    def test_is_empty_returns_false(self, new_stack, size):
        """is_empty() should return False if it's not empty"""
        stack = new_stack(size)
        assert stack.is_empty() == False

    def test_push_increases_size(self, new_stack):
        """should increase in size every time you push to the stack"""
        stack = new_stack(size=0)
        for i in range(1, 11):
            stack.push(i)
            assert i == stack.size()

    def test_pop_decreases_size(self, new_stack):
        """should decrease in size every time you pop from the stack"""
        STACK_SIZE = 10
        stack = new_stack(STACK_SIZE)

        curr_size = stack.size()

        for _ in range(STACK_SIZE):
            stack.pop()
            curr_size -= 1
            assert curr_size == stack.size()

    def test_pop_returns_last_value(self):
        """pop() should return the last value in the stack"""
        stack = Stack()

        r = range(10)
        for i in r:
            stack.push(i)

        curr_index = -1

        for _ in r:
            assert r[curr_index] == stack.pop()
            curr_index -= 1

    def test_pop_raises_EmptyStackError_if_empty(self, new_stack):
        """pop() should raise an EmptyStackError if the stack is empty"""
        stack = new_stack(size=0)
        with pytest.raises(EmptyStackError):
            stack.pop()

    @pytest.mark.parametrize("size", range(1, 11))
    def test_peek_returns_last_value(self, new_stack, size):
        """peek() should return the last value in the stack"""
        stack = new_stack(size)
        VALUE = "abcdef"
        stack.push(VALUE)
        assert VALUE == stack.peek()

    @pytest.mark.parametrize("size", range(1, 11))
    def test_peek_does_not_change_size(self, new_stack, size):
        """peek() should not change the stack size"""
        stack = new_stack(size)
        stack.peek()
        assert size == stack.size()

    def test_peek_raises_EmptyStackError_if_empty(self, new_stack):
        """peek() should raise an EmptyStackError if the stack is empty"""
        stack = new_stack(size=0)
        with pytest.raises(EmptyStackError):
            stack.pop()