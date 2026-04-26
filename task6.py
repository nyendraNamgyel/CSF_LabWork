class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        result = ""

        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next

        result += "None"
        return result


class AdvancedLinkedList(LinkedList):

    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None

    def reverse_list(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


# Demo
al = AdvancedLinkedList()
al.insert_at_end(10)
al.insert_at_end(20)
al.insert_at_end(30)
al.insert_at_end(40)

print("Linked List:", al.display())
print("Number of nodes:", al.count_nodes())
print("Middle element:", al.find_middle())

al.reverse_list()
print("Reversed list:", al.display())