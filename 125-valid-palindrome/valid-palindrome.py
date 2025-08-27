class Solution:
    def isPalindrome(self, s):
        if len(s) == 0 or len(s) == 1:
            return True

        a = ""
        s = s.lower()
        al = "1234567890qwertyuiopasdfghjklzxcvbnm"

        for i in s:
            if i in al:
                a += i 
        
        i = 0
        j = len(a) - 1

        while i < j:
            if a[i] != a[j]:
                return False
            i += 1
            j -= 1

        return True