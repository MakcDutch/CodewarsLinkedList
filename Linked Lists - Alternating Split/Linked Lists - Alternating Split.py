class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("List must contain at least two nodes.")

    a_head = head
    b_head = head.next

    a = a_head
    b = b_head

    current = head.next.next
    toggle = True

    while current:
        if toggle:
            a.next = current
            a = a.next
        else:
            b.next = current
            b = b.next
        current = current.next
        toggle = not toggle

    a.next = None
    b.next = None

    return Context(a_head, b_head)
