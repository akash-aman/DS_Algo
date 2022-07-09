class Solution:
    
    # Functional Way
    def factorial(self , n):
        if n == 0:
            return 1
        return n * self.factorial(n-1)

    # Parameter + Functional Way
    def factorial_parameter(self, n,factorial):
        if n == 0:
            return factorial
        return self.factorial_parameter(n-1,factorial*n)

if __name__ == "__main__":
    print(Solution().factorial(10))
    print(Solution().factorial_parameter(10,1))
