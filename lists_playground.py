chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboad box"]

# chilli_wishlist.append('dig mat')
# chilli_wishlist.extend(['kong', 'tennis ball', 'crocodile toy'])
# print(chilli_wishlist)

# #indexing
# print(len(chilli_wishlist))
# print(chilli_wishlist)
# print(type(chilli_wishlist))

# print(chilli_wishlist[0])
# print(chilli_wishlist[1])
# print(chilli_wishlist[-1])
# print(chilli_wishlist[0:2])
# print(chilli_wishlist[1:3])

# chilli_wishlist[1] = "carrot" 
# [print(chilli_wishlist)]
# this altered the element of the list, changeed chicken to carrot

#Small challenge page 1 - print sublist (sliced list from the original list) of items in positions 2 through to 3
# print item in index of -3
# #change the value of the first item in the list
# chilli_wishlist = ["igloo", "chicken","donut toy", "cardboard box"]

# print(chilli_wishlist[1:3])
# print(chilli_wishlist[-3])
# chilli_wishlist[0] = "iceburg"
# [print(chilli_wishlist)]

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboad box"]

# chilli_wishlist.append('dig mat')
# chilli_wishlist.extend(['kong', 'tennis ball', 'crocodile toy'])
# print(chilli_wishlist)

# chilli_wishlist.pop()
# print(chilli_wishlist)

# chilli_wishlist.pop(2)
# print(chilli_wishlist)

# chilli_wishlist.remove('igloo')
# print(chilli_wishlist)

# if "tennis ball" in chilli_wishlist:
#     print("Chilli would like a tennis ball.")
# else:
#     print("Chilli doesn't feel like playing fetch.")

# if len(chilli_wishlist) > 8:
#     print("Chilli wants a lot of stuff.")

#Sublists - lists of lists - nested lists

chilli_wishlist = [
    ["igloo"],
    ["donut toy", "tennis ball", "crocodile toy"],
    ["chicken", "peanut butter"],
    ["cardoard box", "box", "dig mat"]
]
print(len(chilli_wishlist))
print(chilli_wishlist[2][0])
print(chilli_wishlist[-1][-1])


