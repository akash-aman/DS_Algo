class Solution:

    # Functional Way
    def sum(self , n):
        if n == 0:
            return 0
        return n + self.sum(n-1)

    # Parameter + Functional Way
    def sum_parameter(self, n,sum):
        if n == 0:
            return sum
        return self.sum_parameter(n-1,sum+n)

if __name__ == "__main__":
    print(Solution().sum(10))
    print(Solution().sum_parameter(10,0))
