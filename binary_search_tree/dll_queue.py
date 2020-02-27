from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        head_value = None
        if self.storage.head and self.storage.head.value != None:
            head_value = self.storage.head.value
            self.storage.remove_from_head()

        return head_value

    def len(self):
        return self.storage.length
