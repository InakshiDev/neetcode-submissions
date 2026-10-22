class Solution:
    def isPalindrome(self, s: str) -> bool:
        initial = s.lower()
        palindrome1 = "".join(ch for ch in initial if ch.isalnum())
        palindrome2 = palindrome1[::-1]
        if palindrome1 == palindrome2:
            return True
        else:
            return False

        
        