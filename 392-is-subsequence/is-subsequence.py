class Solution(object):
    def isSubsequence(self, s, t):
        sub = ""
        j = 0
        i = 0
        while (i <= len(t) - 1) and (j <= len(s) - 1):
            if t[i] == s[j]:
                sub += t[i]
                j += 1
            i += 1

        return len(s) == len(sub)

