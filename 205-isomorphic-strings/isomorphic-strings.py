class Solution(object):
    def isIsomorphic(self, s, t):
        dic = {}


        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in dic.values():
                    return False
                dic[s[i]] = t[i]
            elif (s[i] in dic and dic[s[i]] != t[i]):
                return False
        return True
                
        