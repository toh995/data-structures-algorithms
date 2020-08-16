class Deque {
    constructor() {
        this._deque = [];
    }

    isEmpty() {
        return this._deque.length === 0 ? true : false;
    }

    addFront(newValue) {
        this._deque.unshift(newValue);
    }

    addRear(newValue) {
        this._deque.push(newValue);
    }

    removeFront() {
        if (this.isEmpty()) {
            throw new EmptyQueueError();
        }

        return this._deque.shift();
    }

    removeRear() {
        if (this.isEmpty()) {
            throw new EmptyDequeError();
        }

        return this._deque.pop();
    }

    peekFront() {
        if (this.isEmpty()) {
            throw new EmptyDequeError();
        }

        return this._deque[0];
    }

    peekRear() {
        if (this.isEmpty()) {
            throw new EmptyDequeError();
        }

        const lastIndex = this._deque.length - 1;
        return this._deque[lastIndex];
    }

    size() {
        return this._deque.length;
    }

    displayDeque() {
        console.log(this._deque);
    }
}

class EmptyDequeError extends Error {
    constructor(message="Deque is empty!") {
        super(message);
        this.name = "EmptyDequeError";
    }
}