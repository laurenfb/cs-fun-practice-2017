# Traversing trees
[trees 4 lyfe](http://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/)

## Pre-order traversal
Root, left, right

Pre-order is used to create a copy of the tree.

## In-order traversal
Left, root, right

In-order is used to return the values of the tree in order.

Time complexity -- expected O(n)

Space complexity -- expected O(log(n))

## Post-order traversal
Left, right, root

Post-order is used to delete the binary tree.

Time complexity -- expected O(n)

Space complexity -- expected O(log(n))

# Insertion order matters
When you take an array and use it to make a tree, the order is important. If the array is already sorted, then the tree ends up super unbalanced.
