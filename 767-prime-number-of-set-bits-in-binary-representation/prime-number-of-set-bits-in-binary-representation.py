class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    return False
            return True

        count = 0
        for i in range (left,right+1):

            binary = bin(i)[2:]
            num =binary.count("1")
            if is_prime(num):
                count += 1
        return count
        