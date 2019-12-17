''' Easy
    You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

    The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

    Example 1:

    Input: J = "aA", S = "aAAbbbb"
    Output: 3
    Example 2:

    Input: J = "z", S = "ZZ"
    Output: 0
    Note:

    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.
'''

def numJewelsInStones(J, S):
    # count = 0
    # for i in S:
    #     if i in J:
    #         count += 1
    # return count
    
    print(list(map(lambda x: S.count(x), J)))

    # return sum(map(lambda x:S.count(x),J)) 
    # map considers each i of the sequence J
    # map applies each i into the lambda funtion
    # the function returns the number of count


print(numJewelsInStones("aA", "aAAbbbb"))
# print(numJewelsInStones("z", "ZZ"))

# [print(i) for i in map("asas".count("a"), "what")]

# print(sum(print(i) for i in ["wheh".count(i) for i in list("huh, like wuh")]))

