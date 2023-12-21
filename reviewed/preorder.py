class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def dfs_preorder(node):
    if node:
        print(node.val, end=' ')  # 訪問根節點
        dfs_preorder(node.left)   # 遞迴遍歷左子樹
        dfs_preorder(node.right)  # 遞迴遍歷右子樹

# 建立樹狀結構
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

# 執行DFS Preorder遍歷
dfs_preorder(root)