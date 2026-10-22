from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total_product = prod(nums)
        zero_count = nums.count(0)

        if zero_count == 1:
            prod_without_zero = prod(x for x in nums if x != 0)
            return [prod_without_zero if x == 0 else 0 for x in nums]

        if zero_count > 1:
            return [0] * len(nums)

        for num in nums:
            output.append(int(total_product//num))
        
        return output