class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0

        p1 = 0
        p2 = 0

        for p1 in range(len(haystack)- len(needle)+1):
            if haystack[p1:p1 + len(needle)] == needle:
                return p1

            
        return -1

            
# Time complexity: Loop O(n+m-1) * Substring slicing O(m) => O(n*m)
        