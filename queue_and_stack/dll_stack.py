from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):

        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        tail = self.storage.get_tail().value
        self.storage.remove_from_tail()

        return tail

    def len(self):
        return self.storage.length
