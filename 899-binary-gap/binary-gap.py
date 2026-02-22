class Solution:
    def binaryGap(self, n: int) -> int:
        a = []
        l = bin(n)[2:]
        for i in range(len(l)):
            if l[i] == "1":
                a.append(i)
        if len(a) <= 1:
            return 0
        Max = 0

        for i in range(len(a) - 1):
            Max = max(Max, int(a[i+1]) - int(a[i]))
        return Max