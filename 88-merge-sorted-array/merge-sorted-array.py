class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1          # último válido em nums1
        j = n - 1          # último de nums2
        k = m + n - 1      # última posição de nums1

        # enquanto ainda houver algo em nums2 para colocar
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1