class Solution(object):
    def reverseString(self, s):
        n = len(s)
        i = 0
        j = len(s) - 1
        while(i <= n/2 and j >= (n - n/2)):
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        