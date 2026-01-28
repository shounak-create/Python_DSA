class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_list(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display_list(self):
        if self.head is None:
            return "no elements in the list"

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def Count_list(self):
        count = 0
        if self.head is None:
            return count

        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print(count)


l1 = LinkedList()
l1.add_list(23)
l1.add_list(24)
l1.add_list(25)
l1.Count_list()
l1.display_list()
