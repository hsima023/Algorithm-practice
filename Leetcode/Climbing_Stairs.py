#Climbing Stairs

#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        curr = prev = 1
        for i in range(n-1):
            curr, prev = curr+prev,curr
        
        return curr