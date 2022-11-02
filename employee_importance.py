#TC: O(n) 
#SC: O(h)
class Solution: 
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.importance = 0
        graph = self.makeGraph(employees) #create the graph
        self.dfs(graph, id, set()) #call the recursive function
        return (self.importance) #return the total importance
    
    def dfs(self, graph, node, visited): #passing the graph, current node, visited hashset and importance into the dfs function
        if node in visited: #if node is already there in visited set, unfold the recursion
            return
        visited.add(node) #by default add the node to visited
        for adj_node in graph[node][1]: #first index has the subordinates array, in which we have to traverse
            self.dfs(graph, adj_node, visited) #call the recursion
        visited.remove(node)
        self.importance+=(graph[node][0]) #importance array will have the current importance
        return
    
    def makeGraph(self, employees: List['Employee']) -> Dict: #making the graph
        graph = {} #we can keep graph as a hashmap
        for employee in employees: #traverse through the employee list
            graph[employee.id] = (employee.importance, employee.subordinates) #with employee id as key, save the employee importance and subordinates  
        #print(graph)
        return graph 