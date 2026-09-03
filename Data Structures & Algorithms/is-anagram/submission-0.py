class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        if len(s) != len(t):
            return False
        else:
            if countString(s) == countString(t):
                return True
        return False
 
def countString(string: str) -> dict:
    dictionary = {}
    for char in string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary
