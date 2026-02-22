class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stk =[]
        sol =[]

        for i in range(1,n+1):
            sol.append("Push")
            stk.append(i)
            if i not in target:
                sol.append("Pop")
                stk.remove(i)
            if len(stk) == len(target):
                break
        return sol