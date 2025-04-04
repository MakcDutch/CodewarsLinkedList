from preloaded import Node

def swap_pairs(head):
    fake = Node(0)
    fake.next = head
    prev = fake

    while head and head.next:
        first = head
        second = head.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        head = first.next

    return fake.next
