class Solution(object):
    def wordPattern(self, pattern, s):
        dic = {}
        w = s.split()   

        if len(pattern) != len(w):  
            return False

        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if w[i] in dic.values():
                    return False
                dic[pattern[i]] = w[i]
            elif (pattern[i] in dic and dic[pattern[i]] != w[i]):
                return False
        return True

        