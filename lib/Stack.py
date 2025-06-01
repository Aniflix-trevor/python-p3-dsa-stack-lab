class Stack:
    def __init__(self, items=None, limit=100):
        self._items = list(items) if items else []
        self.limit = limit

    @property
    def items(self):
        return self._items

    def is_empty(self):
        return len(self._items) == 0

    def isEmpty(self):
        return self.is_empty()

    def push(self, item):
        if self.full():
            raise OverflowError("Stack is full")
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        else:
            # Instead of raising, just return None
            return None

    def peek(self):
        if not self.is_empty():
            return self._items[-1]
        return None

    def size(self):
        return len(self._items)

    def full(self):
        return len(self._items) >= self.limit

    def search(self, target):
        try:
            index_from_top = self._items[::-1].index(target)
            return index_from_top + 1
        except ValueError:
            return -1
