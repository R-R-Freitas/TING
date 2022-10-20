# import re


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head_value = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        if self.__length == 0:
            new_value = Node(value)
            new_value.next = self.head_value
            self.head_value = new_value
            self.__length += 1
        else:
            new_value = Node(value)
            current_value = self.head_value
            while current_value.next:
                current_value = current_value.next
            current_value.next = new_value
            self.__length += 1

    def dequeue(self):
        value_to_dequeue = self.head_value
        if value_to_dequeue:
            self.head_value = self.head_value.next
            value_to_dequeue.next = None
            self.__length -= 1
        return value_to_dequeue.value

    def search(self, index):
        if index not in range(self.__length):
            raise IndexError
        returned_value = None
        value_to_return = self.head_value
        if value_to_return:
            while index > 0 and value_to_return.next:
                value_to_return = value_to_return.next
                index -= 1
            if value_to_return:
                returned_value = value_to_return.value
        return returned_value
