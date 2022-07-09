
# https://leetcode.com/problems/combination-sum-ii/
# -----------------------------------------------------------------------------------
# array are not in sorted order
# sum with unique elements to be considered
# -----------------------------------------------------------------------------------
# 1,2,3,1,5,6,1,8,1,10
# 1,1,3,4,5,5,5,5,5,6,7,7
# -----------------------------------------------------------------------------------
# needed parameters are :-
# sum
# target Sum
# sorted Array
# index needed to start
# sequence


from array import array


class Solution:
    def __init__(self):
        self.result = []

    def combinationSum2(self, sum, target, array, index, sequence):

        if (sum == target):

            self.result.append(sequence[:])
            return

        for currentIndex in range(index, len(array)):
            if(currentIndex > index and array[currentIndex-1] == array[currentIndex]):
                continue
            if(array[currentIndex] > target):
                return

            sequence.append(array[currentIndex])
            self.combinationSum2(
                sum+array[currentIndex], target, array, currentIndex+1, sequence)
            sequence.pop()


if __name__ == "__main__":
    arr = [10, 1, 2, 7, 6, 1, 5]
    sequence = []
    sum = 0
    target = 8
    index = 0

    solution = Solution()
    solution.combinationSum2(sum, target, sorted(arr), index, sequence)
    print(solution.result)
