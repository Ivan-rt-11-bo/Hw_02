class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

# Функция swap_values для обмена k-ого элемента с предпоследним элементом
def swap_values(linked_list, k):
    if k < 0 or k >= linked_list.length - 1:
        return

    if k == 0:
        current_forward = linked_list.head
        for i in range(k):
            current_forward = current_forward.next
        current_forward.data, linked_list.head.data = linked_list.head.data, current_forward.data
        return

    current_forward = linked_list.head
    for i in range(k - 1):
        current_forward = current_forward.next

    current_penultimate = linked_list.head
    for i in range(linked_list.length - 3):
        current_penultimate = current_penultimate.next

    current_forward_next = current_forward.next
    current_penultimate_next = current_penultimate.next

    current_forward.data, current_penultimate_next.data = current_penultimate_next.data, current_forward.data
    current_forward_next.data, current_penultimate.data = current_penultimate.data, current_forward_next.data

# Пример использования:
# l1 = LinkedList(1, 2, 3, 4, 5)
# swap_values(l1, 2)
# print(l1)  # Выводит: (1 -> 3 -> 4 -> 2 -> 5)
