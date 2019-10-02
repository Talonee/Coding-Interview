'''
    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:

    Input: 123
    Output: 321
    Example 2:

    Input: -123
    Output: -321
    Example 3:

    Input: 120
    Output: 21
    Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

def yoink(x):
    rev = int(str(x)[::-1]) if x >= 0 else (-int(str(x)[1:][::-1]))
    return rev if (rev < (2**31 - 1) and rev > (-2**31)) else 0

print(yoink(-123))
print(yoink(123))
print(yoink(120))
print(2**31 - 1)
print(1534236469)
print(yoink(1534236469))
print(yoink(-2147483648))