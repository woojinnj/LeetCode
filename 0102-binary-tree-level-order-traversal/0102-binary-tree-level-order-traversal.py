from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]

        q=deque()
        if root:
            q.append(root)

        while q:
            q_len=len(q)
            temp=[]
            for _ in range(q_len):
                current=q.popleft()
                if current:
                    temp.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            res.append(temp)
        return res
                
