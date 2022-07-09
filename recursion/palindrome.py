class Solution:
    def checkPalindrome(self,l,r,arr):
        if l >= r:
            return True
        if arr[l] != arr[r]:
            return False
        return self.checkPalindrome(l+1,r-1,arr)


if __name__ == "__main__":
    string = "madamimadam"
    arr = list(string)
    print(Solution().checkPalindrome(0,len(arr)-1,arr))
