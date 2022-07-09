class Solution:

    # Head Recursion
    def print_number(self, n):
        if n == 0 :
            return 
        
        print(n-1)
        self.print_number(n-1)

    # Tail Recursion
    def print_number_tail(self, n, i=0):
        if n == i:
            return

        self.print_number_tail(n, i+1)
        print(i)

if __name__ == "__main__":
    Solution().print_number(10)
    Solution().print_number_tail(10)
