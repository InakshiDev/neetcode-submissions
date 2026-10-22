class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numcount = Counter(nums)
        value_list = list(numcount.values())
        value_sorted = sorted(value_list, reverse = True)
        values_needed = value_sorted[0:k]
        output = []
        used_keys = set()
        def reverse_lookup(dictionary, value):
            for key in dictionary:
                if dictionary[key] == value and key not in used_keys:
                    used_keys.add(key)
                    return key
        for value in values_needed:
            req = reverse_lookup(numcount, value)
            output.append(req)
            
        return output
