class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        big_list = []
        dictionary = {}
        for char in strs:
            key = tuple(sorted(char))
            if key in dictionary:
                dictionary[key].append(char)
            else:
                dictionary[key] = [char]
            
        return list(dictionary.values())