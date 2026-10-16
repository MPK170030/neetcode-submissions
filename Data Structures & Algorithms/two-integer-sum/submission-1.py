class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index,num in enumerate(nums):
            search = target - num
            if search in hash_map:
                return [hash_map[search], index]
            hash_map[num] = index
        
        