class CircularQueue {
    constructor(size) {
        this._size = size;
        this._queue = new Array(size);
        this._head = -1;
        this._tail = -1;
    }

    isEmpty() {
        return (this._head === -1) && (this._tail === -1);
    }

    isFull() {
        return (this._tail + 1) % this._size === this._head;
    }

    enqueue(newValue) {
        if (this.isFull()) {
            throw new FullCircularQueueError();
        }

        // adjust indexes for head and tail
        if (this.isEmpty()) {
            this._head = 0;
            this._tail = 0;
        }

        else {
            this._tail = (this._tail + 1) % this._size;
        }

        // add the new value to the queue
        this._queue[this._tail] = newValue;
    }

    dequeue() {
        if (this.isEmpty()) {
            throw new EmptyCircularQueueError();
        }

        const ret = this._queue[this._head];

        // if we are dequeueing the last item from the queue, then put into empty state
        if (this._head === this._tail) {
            this._head = -1;
            this._tail = -1;
        }

        // otherwise, adjust the head index normally
        else {
            this._head = (this._head + 1) % this._size;
        }

        return ret;
    }

    peek() {
        if (this.isEmpty()) {
            throw new EmptyCircularQueueError();
        }

        return this._queue[this._head];
    }

    display() {
        const displayValue = this._getDisplayValue();
        console.log(displayValue);
    }

    _getDisplayValue() {
        if (this.isEmpty()) {
            return [];
        }

        if (this._head <= this._tail) {
            const start = this._head;
            const end = this._tail;
            return this._queue.slice(start, end);
        }

        else {
            const firstIndex = this._head;
            const firstArr = this._queue.slice(firstIndex);

            const secondIndex = this._tail + 1;
            const secondArr = this._queue.slice(0, secondIndex);

            return firstArr.concat(secondArr);
        }
    }
}

class EmptyCircularQueueError extends Error {
    constructor(message="Circular Queue is empty!") {
        super(message);
        this.name = "EmptyCircularQueueError";
    }
}

class FullCircularQueueError extends Error {
    constructor(message="Circular Queue is full!"){
        super(message);
        this.name = "FullCircularQueueError";
    }
}