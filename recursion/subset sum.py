
## sum 
## array
## index 

class Solution:

    def subsetSum(self,sum,array,index):

        if(index == len(array)):
            print(sum)
            return 

        take = self.subsetSum(sum+array[index],array,index+1)

        skip = self.subsetSum(sum,array,index+1)
    

if __name__ == "__main__":

    arr = [5,2,1]
    index = 0 
    sum = 0 

    solution = Solution()
    solution.subsetSum(sum,arr,index)