class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, node=None):
        self.head = Node(node) if node else None
        self.tail = self.head

    def add_to_head(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        else:
            new_node = Node(value)
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        if self.tail is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next_node = new_node
            self.tail = new_node

    def contains(self, target_node):
        current_node = self.head

        if current_node is None:
            return False
        elif current_node.value is target_node:
            return True
        else:
            while current_node.next_node is not None:
                if current_node.next_node.value is target_node:
                    return True
                current_node = current_node.next_node
            return False

    def get_max(self):
        if self.head is None:
            return None
        else:
            current_max = self.head.value
            current_node = self.head
            while current_node != None:
                if current_node.value > current_max:
                    current_max = current_node.value
                current_node = current_node.next_node
            return current_max

    def remove_head(self):
        if self.head is None:
            return
        elif self.head.next_node is None:
            return_val = self.head.value
            self.head = None
            self.tail = None
            return return_val
        else:
            return_val = self.head.value
            self.head = self.head.next_node
            return return_val
