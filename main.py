class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    length = 0
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.length = 0
        for item in args:
            self.add_back(item)
            self.length += 1  # Увеличивайте length при добавлении элементов

    def add_forward(self, el):
        new_node = Node(el)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def add_back(self, el):
        new_node = Node(el)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        #self.length += 1

    def pop(self, index=0):
        if index < 0 or index >= self.length:
            raise IndexError("pop index out of range")

        if index == 0:
            removed_data = self.head.data
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return removed_data

        current = self.head
        for i in range(index - 1):
            current = current.next

        removed_data = current.next.data
        current.next = current.next.next
        if index == self.length - 1:
            self.tail = current
        self.length -= 1
        return removed_data

    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError("can only concatenate LinkedList (not {}) to LinkedList".format(type(other).__name))

        new_list = LinkedList()
        current = self.head
        while current:
            new_list.add_back(current.data)
            current = current.next

        current = other.head
        while current:
            new_list.add_back(current.data)
            current = current.next

        return new_list

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("list index out of range")

        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError("list index out of range")

        current = self.head
        for i in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "(" + " -> ".join(elements) + ")"

    def __repr__(self):
        return "LinkedList(" + ", ".join(map(repr, self)) + ")"
    def __len__(self):
        return self.length  # Возвращайте значение атрибута length
