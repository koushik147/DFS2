class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adj = defaultdict(list) # creating the adj list
        self.createdict(root, adj) # calling the create function
        #print(adj)
        
        res = [] # craeting the result
        self.dfs(target.val, 0, k, res, adj, set()) # calling the dfs function
        return res # returning res
        
    def createdict(self, cur, adj): # 
        if cur.left:    # traverse through left of root node
            adj[cur.val].append(cur.left.val) # appending the root value as key with its adjacent left value
            adj[cur.left.val].append(cur.val) # appending the left value as key with root value
            self.createdict(cur.left, adj) # recursion calling
        if cur.right:    # traverse through right of root node
            adj[cur.val].append(cur.right.val) # appending the root value as key with its adjacent right value
            adj[cur.right.val].append(cur.val) # appending the right value as key with root value
            self.createdict(cur.right, adj) # recursion calling
        return
    
    def dfs(self, cur, cur_step, last_step, res, adj, visited): # craeting the dfs function
        if cur_step == last_step:    # appending in result when hit k
            res.append(cur)    # appending in result
            return
        visited.add(cur) # adding in visited
        for nxt in adj[cur]:    # iterating in the adj of cur
            if nxt not in visited: # if value not in visited
                visited.add(nxt) # adding in visited set
                self.dfs(nxt, cur_step+1, last_step, res, adj, visited) # recursion calling
        return