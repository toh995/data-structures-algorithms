class Stack {
    constructor() {
        this._arr = [];
    }

    isEmpty() {
        return this._arr.length ? false : true;
    }

    push(newValue) {
        this._arr.push(newValue);
    }

    pop() {
        if (this.isEmpty()) {
            throw new EmptyStackError();
        }

        return this._arr.pop();
    }

    peek() {
        if (this.isEmpty()) {
            throw new EmptyStackError("dlksfjdlk");
        }

        const lastIndex = this._arr.length - 1;
        return this._arr[lastIndex];
    }

    displayStack() {
        console.log(this._arr);
    }
}

class EmptyStackError extends Error {
    constructor(message="Stack is empty!") {
        super(message);
        this.name = "EmptyStackError";
    }
}

const stack = new Stack();
stack.peek();