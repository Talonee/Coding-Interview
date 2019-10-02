''' Given a collection of numbers, determine whether there exists two distinct
elements in the array whose sum equals a target value.
'''

elements = [2,4,5,9,1]

# def fxn(ls, target):
#     for i in ls:
#         nex = ls.index(i) + 1
#         if len(ls[nex:]) != 0: 
#             for j in ls[nex:]:
#                 if i + j == target:
#                     return("Number: " + str(i) + " and " + str(j) + " has the sum value of " + str(target))
#     return("None found.")

# print(fxn(elements, 7))
# print(fxn(elements, 8))
# print(fxn(elements, 9))



# def fxn(ls, target, index = 0, last = 0):
#     if index < len(ls):
#         if target == 0:
#             print("Yuh")
#             # return("Yeet")
#         else:
#             fxn(ls, target - ls[index], index + 1)
#             fxn(ls, target, index + 1)

        
    
# # print(fxn(elements, 7))
# print(fxn(elements, 8))
# # print(fxn(elements, 9))




# def twoSum(nums, target):
#     index = 0
#     for i in nums:
#         hold = nums[index + 1:]
#         index2 = index
#         for j in hold:
#             if i + j == target:
#                 return list([index, index2 + 1])
#             index2 += 1
#         index += 1

def twoSum(nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            print(remaining)
            if remaining in seen:
                print(seen)
                return [seen[remaining], i]
            seen[v] = i
        return []

nums = [3, 2, 11, 7]
target = 9

print(twoSum(nums, target))