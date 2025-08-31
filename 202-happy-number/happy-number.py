class Solution(object):
    def isHappy(self, n):
        visit = set()

        while n not in visit:
            visit.add(n)

            temp = 0
            num = n
            while num:
                digit = num % 10
                temp += digit ** 2
                num = num // 10

            n = temp
            
            if n == 1:
                return True

        return False