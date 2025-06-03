class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Append a new node to the end of the linked list
    def append(self, data):
        new_node = Node(data)

        # If the linked list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return

        # If the linked list is not empty, traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next

        # Make the new node the last node in the list
        current.next = new_node

    def display(self):
        elements = []
        current = self.head

        # Traverse the list and append each node's data to the elements list
        while current:
            elements.append(f"{current.data} ({type(current.data).__name__})")
            current = current.next

        # Join the elements with a -> symbol
        print(" -> ".join(elements))

# Example usage with different data types
if __name__ == "__main__":
    # Create a new linked list
    my_list = LinkedList()

    # Add different types of data
    my_list.append(42)               # integer
    my_list.append("Hello")          # string
    my_list.append(3.14)             # float
    my_list.append(True)             # boolean
    my_list.append([1, 2, 3])        # list
    my_list.append({"name": "John"}) # dictionary

    # Display the linked list
    print("Linked List with different data types:")
    my_list.display()
