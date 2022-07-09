class Solution:
    def subsequence(self, n, arr):

        if n == 0:
            print(arr)
            return

        arr.append(n)
        take = self.subsequence(n-1, arr)
        arr.pop()
        skip = self.subsequence(n-1, arr)


if __name__ == "__main__":
    arr = []

    Solution().subsequence(5, arr)
