#Given the head pointers of two linked lists where each linked list represents an integer number (each node is a digit), 
#add them and return the resulting linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

        current = current.next

    return dummy_head.next

# Helper function to create linked lists from arrays
def create_linked_list(arr):
    dummy_head = ListNode(0)
    current = dummy_head

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy_head.next

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
arr1 = [2, 4, 3]  # Linked list representing number 342
arr2 = [5, 6, 4]  # Linked list representing number 465

l1 = create_linked_list(arr1)
l2 = create_linked_list(arr2)

result = add_two_numbers(l1, l2)

print("Resulting Linked List:")
print_linked_list(result)
