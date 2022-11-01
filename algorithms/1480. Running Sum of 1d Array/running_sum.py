from typing import List


def runningSum(nums: List[int]) -> List[int]:
    return [sum(nums[:i]) for i, _ in enumerate(nums, start=1)]


test_input_1 = [1, 2, 3, 4]
test_input_2 = [1, 1, 1, 1, 1]
test_input_3 = [3, 1, 2, 10, 1]

assert runningSum(test_input_1) == [1,3,6,10]
assert runningSum(test_input_2) == [1,2,3,4,5]
assert runningSum(test_input_3) == [3,4,6,16,17]
print("Tests successful.")
