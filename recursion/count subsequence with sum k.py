## count will be returned by the function
## sum 
## target sum
## index

class Solution:
    def countSubsequenceSumK(self,sum,target,index,arr):

        if index == len(arr):
            if sum == target:
                return 1
            return 0


        take = self.countSubsequenceSumK(sum+arr[index],target,index+1,arr)

        skip = self.countSubsequenceSumK(sum,target,index+1,arr)

        return take + skip


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    sum = 0
    target = 40
    index = 0
    print(Solution().countSubsequenceSumK(sum,target,index,arr))

