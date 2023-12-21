class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:  # 假設在樹中已經存在相同值的節點不會再插入
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def in_order_traversal(self):
        elements = []
        self._in_order_traversal(self.root, elements)
        return elements

    def _in_order_traversal(self, node, elements):
        if node:
            self._in_order_traversal(node.left, elements)
            elements.append(node.val)
            self._in_order_traversal(node.right, elements)


# 使用範例
bst = BinarySearchTree()
bst.insert(3)
bst.insert(1)
bst.insert(4)
bst.insert(2)

print(bst)

print(bst.in_order_traversal())  # 這會打印 [1, 2, 3, 4]
