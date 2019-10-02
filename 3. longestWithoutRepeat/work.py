'''
    Given a string, find the length of the longest substring without repeating characters.

    Example 1:

    Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3. 
    Example 2:

    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3. 
                Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# def lengthOfLongestSubstring(s):
#     i = 0
#     count = 0
#     box = []
#     exist = []
#     while i < len(s):
#         count += 1
#         exist.append(s[i])
#         if i + 1 >= len(s) or s[i + 1] in exist:
#             print(exist, count)
#             box.append(count)
#             exist = [s[i]]
#             count = 1
#         i += 1
#     return max(box)

def lengthOfLongestSubstring(s):
    i = 0
    count = 0
    curr = []
    box = [0]

    while i < len(s):
        if s[i] in curr: # if the next letter is in current list "abc >a< d"
            box.append(count) # put the current count in the box

            s = s[s.index(s[i]) + 1:] # cut string

            curr = list(s[:s.index(s[i])]) # list current strings up to next after
            count = len(curr) # count current letters available
        else:
            count += 1 
            curr.append(s[i])
        
    return max(box)

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("dvdf"))

# print("boyy".index("y"))

# a = "ayenigga"
# curr = list(a[a.index("n") + 1:])
# print(curr)