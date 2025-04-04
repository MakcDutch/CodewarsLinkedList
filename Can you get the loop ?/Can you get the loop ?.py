def loop_size(node):
    slow = node
    fast = node
#використав алгоритм Флойда
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    loop_count = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        loop_count += 1

    return loop_count
