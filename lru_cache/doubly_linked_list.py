class Node:
    def __init__(self, value, key=None, prev=None, next=None):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


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
        node = self.head

        while node.next.value != None:
            node = node.next

        node.prev.next = None

        self.length -= 1

    def get_tail(self):
        node = self.head

        while node.next.value != None:
            node = node.next

        return node

    def move_to_head(self, node):
        if node is self.head:
            return

        node.prev.next = node.next
        self.head.prev = node
        node.next = self.head
        self.head = node

