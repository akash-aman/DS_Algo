class Solution:

    # Tail Recursion
    def print_number(self, n):
        if n == 0:
            return
        self.print_number(n-1)
        print(n-1)

    # Head Recursion
    def print_number_head(self, n, i=0):

        print(i)

        if n == i:
            return

        self.print_number_head(n, i+1)


if __name__ == "__main__":
    Solution().print_number(10)
    Solution().print_number_head(10)
