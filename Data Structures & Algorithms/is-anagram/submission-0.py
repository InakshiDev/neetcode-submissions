class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lists = sorted(list(s))
        listt = sorted(list(t))
        if lists == listt:
            return True
        else:
            return False