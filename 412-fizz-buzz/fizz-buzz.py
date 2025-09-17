class Solution(object):
    def fizzBuzz(self, n):
        out = []
        for i in range(n):
            out.append(i + 1)
        for i in range(n):
            if out[i] % 3 == 0 and out[i] % 5 == 0:
                out[i] = "FizzBuzz"
            elif out[i] % 3 == 0:
                out[i] = "Fizz"
            elif out[i] % 5 == 0:
                out[i] = "Buzz"
            else:
                out[i] = str(out[i])  
        return out