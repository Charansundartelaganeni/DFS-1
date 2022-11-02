#TC: O(n) 
#SC: O(h)


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.ans = []
        self.dfs(root, 0)
        return self.ans 
        
    def dfs(self,node, i):  

        if not node: return  
        #only the values that are greater than the depth of right, is appended inside ans after right is traversed
        if i >= len(self.ans): #everytime wheni is greater than the ans array, it means we are in the right side
            self.ans.append(node.val) 

        self.dfs(node.right, i+1)  #traverse right path, increase i
        self.dfs(node.left, i+1)  #traverse left path, increase i