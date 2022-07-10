# https://leetcode.com/problems/permutations/
# --------------------------------------------------------------------------------------------------------
# Required parameter are :
# - index // in parameter its not needed
# - permutation
# - array
# - dict

class Solution:

    ## Extra space dict is used to calculate the permutation
    def permutation(self,dict,permutation,array):

        if len(permutation) == len(array):
            print(permutation)
            return 

        for currentIndex in range(len(array)):

            if dict[currentIndex] : 
                continue
            
            permutation.append(array[currentIndex])
            dict[currentIndex] = True
            self.permutation(dict,permutation,array)
            dict[currentIndex] = False
            permutation.pop()

    ## swap technique to generate permutation
    def permute(self,index,array):

        if index == len(array)-1:
            print(array)
            return 

        for currentIndex in range(index,len(array)):
            array[index],array[currentIndex] = array[currentIndex],array[index]
            self.permute(index+1,array)
            array[index],array[currentIndex] = array[currentIndex],array[index]



if __name__ == "__main__":
    array = [1,2,3]
    dict = [False] * len(array)
    permutation = []
    Solution().permutation(dict,permutation,array)
    Solution().permute(0,array)

   