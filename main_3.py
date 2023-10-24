class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.length = 0
        for item in args:
            self.add_back(item)
    pass

    def add_back(self, el):
        new_node = Node(el)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    pass

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "(" + " -> ".join(elements) + ")"
    pass

    def __repr__(self):
        elements = []
        current = self.head
        while current:
            elements.append(repr(current.data))
            current = current.next
        return f"LinkedList({', '.join(elements)})"
    pass

def alternating_split(link_list):
    if not link_list.head:
        return LinkedList(), LinkedList()

    current = link_list.head
    even_list = LinkedList()
    odd_list = LinkedList()
    even_current = even_list
    odd_current = odd_list
    is_even = True

    while current:
        if is_even:
            even_current.add_back(current.data)
        else:
            odd_current.add_back(current.data)

        current = current.next
        is_even = not is_even

    return even_list, odd_list
pass
