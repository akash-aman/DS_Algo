## https://leetcode.com/problems/subsets-ii/
## -----------------------------------------------------------------------------------
## only non duplicate set should be result 
##  
## 
## 
## 
## index
## subset 
## array 
## 


class Solution:

    def __init__(self):
        self.result = []

    def subsetSum(self,index,subset,array):

        
        self.result.append(subset[:])

        for currentIndex in range(index,len(array)):
            if(currentIndex != index and array[currentIndex-1] == array[currentIndex]):
                continue
            

            subset.append(array[currentIndex])
            self.subsetSum(currentIndex+1,subset,array)
            subset.pop()


if __name__ == "__main__":
    arr = [1,2,2]
    subset = []
    index = 0 

    solution = Solution()

    solution.subsetSum(index, subset, sorted(arr))
    print(solution.result)