class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False

        sub = ""
        j = 0
        i = 0
        while (i <= len(t) - 1) and (j <= len(s) - 1):
            if t[i] == s[j]:
                sub += t[i]
                j += 1
            i += 1

        #while j <= (len(s) - 1):
        #    for i in range(len(t)):
        #        if t[i] == s[j]:
        #            sub += t[i]
        #            j+= 1
        
        if len(s) == len(sub):
            return True
        else:
            return False

