class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def postorderTraversal(root):
    if root:
        # 首先遍歷左子樹
        postorderTraversal(root.left)
        # 然後遍歷右子樹
        postorderTraversal(root.right)
        # 最後訪問節點本身
        print(root.val),

# 創建上面示例中的樹
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')

# 執行後序遍歷
postorderTraversal(root)