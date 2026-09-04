class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        additionlist = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    additionlist.append(i)
                    additionlist.append(j)
                    break
        return additionlist
                


        
