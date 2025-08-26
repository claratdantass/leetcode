class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n  

        # passo 1: inverte toda a lista
        nums[:] = nums[::-1]

        # passo 2: inverte os primeiros k elementos
        nums[:k] = nums[:k][::-1]

        # passo 3: inverte os n-k elementos restantes
        nums[k:] = nums[k:][::-1]