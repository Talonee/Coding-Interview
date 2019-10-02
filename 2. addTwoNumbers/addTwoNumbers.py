'''
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
            
#
    # def addTwoNumbers(l1, l2):
    #     leftover = 0
    #     if (l1 != None and l2 != None):
    #         sum = l1.val + l2.val
    #         if (sum >= 10):
    #             sum = sum % 10
    #             leftover += 1
    #         l3 = ListNode(sum)
        
    #     holder = l3
    #     l1 = l1.next
    #     l2 = l2.next
    #     while (l1 != None and l2 != None):
    #         sum = l1.val + l2.val

    #         if leftover == 1:
    #             sum += 1
    #             leftover = 0

    #         if (sum >= 10):
    #             sum = sum % 10
    #             leftover += 1
                
    #         holder.next = ListNode(sum)

    #         l1 = l1.next
    #         l2 = l2.next
    #         holder = holder.next
        
    #     return l3

# Recursion
    # def addTwoNumbers(l1, l2):
    #     return helper(l1, l2, 0)

    # def helper(l1, l2, leftover):
    #     sum = (0 if not l1 else l1.val) + (0 if not l2 else l2.val) + leftover
    #     leftover = sum // 10
    #     ret = ListNode(sum % 10)
    #     if l1.next or l2.next or leftover != 0:
    #         if not l1.next:
    #             l1.next = ListNode(0)
    #         if not l2.next:
    #             l2.next = ListNode(0)

    #         ret.next = helper(l1.next, l2.next, leftover)
    #     return ret


# Non-recursion
def addTwoNumbers(l1, l2):
    ret = ListNode(0)
    curr = ret
    carry = 0
    while l1 or l2:
        sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + curr.val
        curr.val = sum % 10
        carry = sum // 10

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
        curr.next = ListNode(carry) if (l1 or l2 or carry != 0) else None
        curr = curr.next
    return ret

def speak(l1):
    while l1:
        print("{} -> ".format(l1.val))
        l1 = l1.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l4 = ListNode(5)
l5 = ListNode(5)

# speak(addTwoNumbers(l1, l2))
# speak(addTwoNumbers(l4, l5))

# print(divmod(5+5, 10))

print("asfa"[::-1])
