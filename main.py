
## main.py
```python
"""
HW04 — Forest Watchtower (Balanced Tree Check)

Implement TreeNode and is_balanced(root) to check if a binary tree is height-balanced.
"""


class TreeNode:
    """
    Simple binary tree node: value, left, right.
    """

    def __init__(self, value, left=None, right=None):
        # TODO: store the given fields on the instance
        # Example:
        # self.value = value
        # self.left = left
        # self.right = right
        pass


def is_balanced(root):
    """
    Return True if the binary tree rooted at `root` is height-balanced.

    Empty tree (root is None) is considered balanced.
    """
    # TODO (8 Steps of Coding, minimal prompts):
    # - Design a helper that checks balance and height in one traversal.
    # - Implement the recursive logic.
    # - Test on small examples (empty tree, single node, skewed tree).
    raise NotImplementedError("Implement is_balanced in main.py")


if __name__ == "__main__":
    # Optional: quick manual tree
    #   1
    #  / \
    # 2   3
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left, right)
    print(is_balanced(root))
