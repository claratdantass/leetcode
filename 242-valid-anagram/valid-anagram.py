class Solution(object):
    def isAnagram(self, s, t):
        dic = {}

        if len(s) != len(t):
            return False

        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        for c in t:
            if c not in dic:
                return False
            elif dic[c] == 1:
                del dic[c]
            else:
                dic[c] -= 1
        return True
        

        