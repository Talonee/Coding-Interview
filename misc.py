# s = [0, 4, 2, 3, 1, 7]

# for i in range(3):
#     if i not in s:
#         print("I'm here")
#         break
# else:
#     print("But I'm also here")

# res = range(5)
# a, *res, c = res
# print(res)

# print("you'll NEVER believe what that 'FrIeNd' of mine did!!1".title())
s = "We expect the %f%% growth this week"
# print(s.replace("\t", " "*2))
# print(s.split(" ", len(s)%8))
# print(len(str(3.15)))

# print("{:^16.2f}".format(3.1415926))
# s = "We expect the %f%% growth this week"
# print("%f%%%" in s)

# a, *b = "wut"
# print(b)

closet = list(s)
print(closet)
for i in range(len(closet)):
    if i + 1 < len(closet):
        if closet[i] == "%" and closet[i + 1] == "%":
            closet.pop(i + 1)
        elif closet[i] == "%" and closet[i + 1]:
            closet.pop(i + 1)
            closet[i] = "{}"
print(''.join(closet))