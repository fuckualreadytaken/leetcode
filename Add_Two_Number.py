#! /usr/bin/env python
# -*-coding:utf-8-*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    n1 = ""
    while l1 is not None:
        n1 += str(l1.val)
        l1 = l1.next
    n1 = int(n1[::-1])
    n2 = ""
    while l2 is not None:
        n2 += str(l2.val)
        l2 = l2.next

    n2 = int(n2[::-1])
    n3 = n1 + n2
    n3 = list(str(n3))
    lp = ListNode(n3.pop())
    res = lp
    while len(n3) != 0:
        lp.next = ListNode(n3.pop())
        lp = lp.next

    return res


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    res = addTwoNumbers(l1, l2)
    while res is not None:
        print(res.val)
        res = res.next
