class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head) :
    cur = head
    a =set()
    a.add(cur.val)
    while cur and cur.next:
        if cur.next.val in a:
            cur.next = cur.next.next
        else:
            a.add(cur.val)
        cur = cur.next
    return head
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)

# 連接節點
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

deleteDuplicates(node1)