#code to find duplicate number


def findDuplicate(nums):
    dict = {}
    for i in nums:
        dict[i] = 1 + dict.get(i, 0)
    for k, i in dict.items():
        if i >= 2:
            return k

nums = [1,3,4,2,2]
print(findDuplicate(nums))
