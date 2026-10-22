class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers)-1

        while left_index < right_index:
            i = numbers[left_index]
            j = numbers[right_index]
            if i + j == target:
                return [left_index + 1, right_index + 1]
            elif i + j <=target:
                left_index += 1
            else:
                right_index -=1
            

