#TC: O(n)
#SC: O(h)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: 


        result = [ ]
        self.dfs(root, 0, result) #call the recursive function
        for i in result: #traverse through the result array and if one of the ele is not a palindrome, then return Fals
            if not self.isPalindrome (i): 
                return False 

        return True       
        
    def dfs(self, root, level, result):
        
        if len(result) < level+1: #if result is less than the next level, then assign an empty array for the next level
            result.append([ ])  
        if root:  #if there's a root, append it inside the result
            result[level].append(root.val) 
        else: 
            result[level].append(None)  #else append None 
        if root: #if there's a node, do the DFS recursively
            self.dfs(root.left,  level+1, result)   
            self.dfs(root.right, level+1, result)  

    def isPalindrome(self,li): #is palindrome function
        left = 0
        right = len(li)-1

        while left<=right: #two pointer approach
            if li[left]!=li[right]: #if left ele is not equal to right, then it's not a palindrome
                return False
    
            left+=1
            right-=1

        return True

        