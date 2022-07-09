class Solution:
    def reverseArray(self,l,r,arr):
        if l >= r:
            print(arr)
            return
            
        arr[l],arr[r] = arr[r],arr[l]
        self.reverseArray(l+1,r-1,arr)


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    Solution().reverseArray(0,len(arr)-1,arr)
