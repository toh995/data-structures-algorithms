class Queue {
    constructor() {
        this._queue = [];
    }

    isEmpty() {
        return this._queue.length ? false : true;
    }

    enqueue(newValue) {
        this._queue.push(newValue);
    }

    dequeue() {
        if (this.isEmpty()) {
            throw new EmptyQueueError();
        }

        return this._queue.shift();
    }

    peek() {
        if (this.isEmpty()) {
            throw new EmptyQueueError();
        }

        return this._queue[0];
    }

    displayQueue() {
        console.log(this._queue);
    }
}

class EmptyQueueError extends Error {
    constructor(message="Queue is empty!") {
        super(message);
        this.name = "EmptyQueueError";
    }
}