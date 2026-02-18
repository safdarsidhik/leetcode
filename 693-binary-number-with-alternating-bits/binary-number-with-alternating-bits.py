class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x=bin(n)[2:]
        #flag = 0
        for i in range(len(x)-1):
            if x[i] == x[i+1]:
                # flag = 1
                # break
                return False
        # if flag == 0:
        #     return True
        # else:
        #     return False
        return True
            
        

        