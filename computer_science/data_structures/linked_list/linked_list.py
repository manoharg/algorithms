class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        current_node = self.head
        count = 0

        while current_node:
            count += 1
            current_node = current_node.next

        return count

    def search(self, item):
        current_node = self.head

        while current_node and not current_node.data == item:
            current_node = current_node.next

        return current_node != None and current_node.data == item

    def remove(self, item):
        if self.head == None:
            print('List is empty')
            return

        found = False
        current_node = self.head
        previous_node = None

        while not found and current_node:
            if current_node.data == item:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next

        if previous_node == None:
            self.head = current_node.next
        else:
            previous_node.next = current_node.next
