class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = []
        num2 = []
        for x in range(1,n+1):
            if x%m !=0:
                num1.append(x)
            else:
                num2.append(x)
        return sum(num1) - sum(num2)
