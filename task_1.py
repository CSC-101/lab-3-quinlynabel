def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           #Record each value of total and num at the end of the loop body. total: 0, 4, 13, 15, 16   4, 9, 2, 1, 1
    return total

result = tally([4, 9, 2, 1])
print(result)



def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])  #Record each value of new_list and idx at the end of the loop body. new_list: 4, 9, 2, 1 idx: 0, 1, 2, 3
    return new_list  #How does this loop differ from that above? The first loop uses the numbers directly whereas the second loop uses the position to get the numbers.

result = copy([4, 9, 2, 1])
print(result)



def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body. new_list: 5, 10, 3, 2 nums: 4, 9, 2, 1
    return new_list

result = increment_all([4, 9, 2, 1])
print(result)