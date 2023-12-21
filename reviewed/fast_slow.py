class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def findMiddle(head):
    slow = head  # 慢指標，每次移動一個節點
    fast = head  # 快指標，每次移動兩個節點

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 當快指標到達尾端或超出尾端時，慢指標會在中間節點
    return slow.val

node1 = ListNode(1)
node2 = ListNode(2) 
node3 = ListNode(3)
node4 = ListNode(4)  
node1.next = node2
node2.next = node3
node3.next = node4

print(findMiddle(node1))