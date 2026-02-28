class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulo = 10**9 + 7
        result = 0
        
        for i in range(1, n + 1):
            length = i.bit_length()
            result = ((result << length) | i) % modulo
        
        return result