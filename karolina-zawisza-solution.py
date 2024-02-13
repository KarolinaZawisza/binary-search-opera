from functools import reduce
from typing import List

import random


class Solution:

    def __init__(self):
        # In this solution we will use values below to generate array of random integers, the target and determine
        # arrays length.
        self.min_value = -5
        self.max_value = 5
        self.quantity = random.randint(0, 10)

    # generate_target - generates target integer between min_value and max_value.
    def generate_target(self):
        return random.randint(self.min_value, self.max_value)

    # generate_array - using reduce() and lambda, method appends random integers between min_value and
    # max-value to the list with length based of quantity.
    def generate_array(self) -> List[int]:
        return reduce(lambda fun, seq: fun + [random.randint(self.min_value, self.max_value)], range(self.quantity),
                      [])

    # sort_array - sorts previously generated array.
    @staticmethod
    def sort_array(integer_array: List[int]) -> List[int]:
        return sorted(integer_array)

    # find_index - method is looking for an index of a target number. First of all it determines the middle_index based
    # of the first index (always 0) and the last one (length of an array - 1). Then if target is found on that index
    # it returns middle_index. If not and a target is bigger than value of middle_index value it changes low_index
    # value to its value + 1. If not it checks if target is smaller than middle_index and changes high_index value to
    # its value - 1. Loop continues like this and if it can't find matching value then it returns -1.
    @staticmethod
    def find_index(nums: List[int], target: int) -> int:
        low_index = 0
        high_index = len(nums) - 1

        while low_index <= high_index:
            middle_index = low_index + ((high_index - low_index) // 2)

            if nums[middle_index] == target:
                return middle_index

            elif nums[middle_index] < target:
                low_index = middle_index + 1

            elif nums[middle_index] > target:
                high_index = middle_index - 1

        return -1


if __name__ == '__main__':
    solution = Solution()
    # -------------------
    sorted_random_array = solution.sort_array(solution.generate_array())
    random_target = solution.generate_target()
    print(f'Target: {random_target} \nSorted integer array: {sorted_random_array}')
    target_index = solution.find_index(sorted_random_array, random_target)
    if target_index != -1:
        print(f'Target position: {target_index}.')
    else:
        print('(-1) target not found.')
    # --------------------

    # !IMPORTANT!
    # This solution also works on custom lists and targets.
    # If you want to use custom input then please comment block between '----' and uncomment the one below and exchange
    # values for your own:
    # --------------------
    # custom_array = sorted(***put your array here***)
    # custom_target = ***put your target here***
    #
    # print(f'Target: {custom_target} \nSorted integer array: {custom_array}')
    # target_index = solution.find_index(custom_array, custom_target)
    # if target_index != -1:
    #     print(f'Target position: {target_index}.')
    # else:
    #     print('(-1) target not found.')
    # --------------------
