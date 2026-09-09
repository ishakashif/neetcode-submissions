class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        output = []
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, frequency in dictionary.items():
            buckets[frequency].append(num)
        for i in range(len(nums), 0, -1):
            if len(output) == k:
                break
            else:
                output.extend(buckets[i])
        return output


            
        