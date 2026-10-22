class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # length should be same
        if len(s) != len(t):
            return False

        s_sorted = sorted(s)
        t_sorted = sorted(t)

        if s_sorted == t_sorted:
            return True
        else:
            return False

        # we can write this in one line
        # return sorted(s) == sorted(t)

