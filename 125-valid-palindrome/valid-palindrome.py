class Solution:
    def isPalindrome(self, s):
        a = ""
        s = s.lower()
        al = "1234567890qwertyuiopasdfghjklzxcvbnm"

        for i in s:
            if i in al:
                a += i 
        
        return a == a[::-1]


        
        

        return True