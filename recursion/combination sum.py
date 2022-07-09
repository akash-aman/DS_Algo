## https://leetcode.com/problems/combination-sum/
## -----------------------------------------------------------------------------------
## Repetition of element is allowed
## element are distinct
## -----------------------------------------------------------------------------------
## sum is needed
## target Sum needed 
## Array needed 
## index needed to start
## subsequence Array needed for the current combination
## -----------------------------------------------------------------------------------
## Cases to consider:
##  pick element from same index multiple time
##  skip element 

class Solution:
    def __init__(self):
        self.sequence = []
        
    def combinationSums(self,sum,target,array,index,subsequence):
        if sum == target:
            self.sequence.append([x for x in subsequence])
            return 
        
        if sum > target or index >= len(array):
            return

        subsequence.append(array[index])
        take = self.combinationSums(sum+array[index], target, array, index, subsequence)
        subsequence.pop()
        skip = self.combinationSums(sum, target, array, index+1, subsequence)


if __name__ == "__main__":

    sum = 0 
    target = 7
    array = [2,3,6,7]
    index = 0
    subsequence = []

    solution = Solution()

    solution.combinationSums(sum,target,array,index,subsequence)
    print(solution.sequence)