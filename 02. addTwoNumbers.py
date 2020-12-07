'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        temp = self.head
        repr = ""
        while temp is not None:
            repr += "{} -> ".format(temp.val)
            temp = temp.next
        return repr[0:-3]


def addTwoNumbers(l1, l2):
    head = ListNode((l1.val + l2.val) % 10)
    carry = int((l1.val + l2.val) / 10)
    p = l1
    q = l2
    temp = head

    while p.next is not None or q.next is not None or carry != 0:
        x = p.next.val if p.next is not None else 0
        y = q.next.val if q.next is not None else 0

        temp.next = ListNode((x + y + carry) % 10)
        carry = (int)((x + y + carry) / 10)

        temp = temp.next
        if p.next is not None:
            p = p.next
        if q.next is not None:
            q = q.next

    return head


node1 = ListNode(3)
node1.next = ListNode(2)
node1.next.next = ListNode(8)
node2 = ListNode(4)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

l1 = LinkedList(addTwoNumbers(node1, node2))

print(l1)


