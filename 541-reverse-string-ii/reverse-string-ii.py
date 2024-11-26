class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)
        i = 0
        while i < len(s):
            if i + k <= len(s):
                for j in range(k // 2):
                    s[i + j], s[i + k - 1 - j] = s[i + k - 1 - j], s[i + j]
            else:
                for j in range((len(s) - i) // 2):
                    s[i + j], s[len(s) - 1 - j] = s[len(s) - 1 - j], s[i + j]
            i += 2 * k
        return ''.join(s)
