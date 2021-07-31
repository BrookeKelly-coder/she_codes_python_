is_sunny = False
have_shoes = True
is_gym_open = True

# print(is_sunny and have_shoes)
# print(is_sunny or is_gym_open)
# print(not is_sunny)

print(5 < 3)
print( 5 > 3)
print(10 >= 10)
print( 4 <+ 10)
print(5 == 5)
print(5 != 4)

print(5.1 > 2.4)
print("Asli" == "asli") # if the text isn't completely the same it won't be equal


# syntax / semantics

var1 = 5
if var1 > 3:
    print("hello")

name = "Asli"
if name == "Asli":
    print("Hello Asli")
elif name == "Randall":
    print("Hi Randall")
else:
    print("Hello")

#elif is being checked, if the if statement before it is not true

#Lists

letters = ["a", "b", "c", "d"] #this is a list of strings called letters
print(letters [1])
print(letters [-1]) #minus 1 will always give us the last value in the list

print(letters[0:3]) #this will grab letter a - c. O is the start value, up until index 3, but will always exclude the last index
print(letters[3]) # will grab value d but can also do it like this

print(letters[1:3]) #will print b and c. If we use 2 it won't show because its stops on the last one, need to use 3 to capture c

#Adding an element into a list

letters.append("f")
print(letters)

letters.extend(["g", "m"])
print(letters)

letters.insert(1, "z")
print(letters)
# this is changing the 1st index, b, to a z

#can use append or extend. Would use extend, if you want to append multiple

letters.pop(2)
print(letters)
#pop removes the value from that index, so c is removed

letters.remove("d")
print(letters)
#removes the item, if you don't know the element
