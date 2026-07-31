#Brute Force Approach (O(n^2)):

# def twoSum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return [i,j]

#Optimized Approach (O(n)):
#We can do better using hash map (dictionary)

def twoSum(nums,target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target-num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
