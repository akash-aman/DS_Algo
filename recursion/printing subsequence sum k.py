## need an array to store sequence having taregt sum
## original array is needed
## sum of array is needed
## target sum is needed
## index is needed

class Solution:
    def targetSumSubsequence(self,index,sum,target,arr,subsequence):
        if sum == target:
            print(subsequence)
            return 

        if index == len(arr):
            return

        subsequence.append(arr[index])
        self.targetSumSubsequence(index+1,sum+arr[index],target,arr,subsequence)
        subsequence.pop()
        self.targetSumSubsequence(index+1,sum,target,arr,subsequence)


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    subsequence = []
    index = 0
    sum = 0
    target = 40
    Solution().targetSumSubsequence(index,sum,target,arr,subsequence)
   