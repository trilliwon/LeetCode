class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        if n/3 == n//3:
            return self.isPowerOfThree(n//3)
        else:
            return False
