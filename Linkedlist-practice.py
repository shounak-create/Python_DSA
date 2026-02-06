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

    def insertion_at_start(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

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

    def reverse_list(self):
        temp = self.head
        new = self.head.next
        new2 = self.head.next.next

        while new2.next is not None:
            new.next = temp
            temp = new
            new = new2
            new2.next = new2.next
        self.head = new2


l1 = LinkedList()
l1.add_list(23)
l1.add_list(24)
l1.add_list(25)
l1.add_list(26)
l1.add_list(27)
print("Counting")
l1.Count_list()
print("1st display")
l1.display_list()
l1.insertion_at_start(1)
print("2nd Display")
l1.display_list()
print("reversing")
l1.reverse_list()
l1.display_list()