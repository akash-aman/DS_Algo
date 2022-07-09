class Solution:
    def print_name(self, name, n):
        if n == 0 :
            return 
        
        print(name)
        self.print_name(name, n-1)


if __name__ == "__main__":

    Solution().print_name("John", 3)