class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        cont = {}
        for c in magazine:
            if c in cont:
                cont[c] += 1
            else:
                cont[c] = 1  
        
        for c in ransomNote:
            if c not in cont:
                return False
            elif cont[c] == 1:
                del cont[c]
            else:
                cont[c] -= 1
        return True
