class Node:
    def __init__(self, value, key=None, prev=None, next=None):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.length = 0

    def add_to_head(self, value, key=None):
        node = Node(value, key)

        self.head.prev = node
        node.next = self.head
        self.head = node

        self.length += 1

    def remove_from_tail(self):
        if self.head == None or self.head.value == None:
            return
        node = self.head

        while node.next:
            node = node.next

        if self.length > 1:
            node.prev.next = None

        self.length -= 1

        if self.length <= 0:
            self.head = None

    def get_tail(self):
        if not self.head:
            return None
        if self.head.next == None:
            return self.head
        if self.length == 1:
            return self.head
        node = self.head

        while node.next:
            node = node.next

        return node

    def move_to_head(self, node):
        if node is self.head:
            return

        node.prev.next = node.next
        self.head.prev = node
        node.next = self.head
        self.head = node

    # working methods

    def remove_from_head(self):
        head_value = self.head.value

        self.head = self.head.next
        self.head.prev = None

        self.length -= 1

        return head_value

    def add_to_tail(self, value):
        if self.length == 0:
            self.add_to_head(value)
            return

        tail = self.get_tail()
        node = Node(value)

        tail.next = node
        node.prev = tail

        self.length += 1

