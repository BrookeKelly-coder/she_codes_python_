#Example

# for number in range(10): #iterate through the sequence of numbers, 0,1,2,3...9
#     print(number)

# letters = ["a", "b", "c", "d"]

# for letter in letters:
#     print(letter)

# #created a variable (letter) in the list.

# letters = ["a", "b", "c", "d"]

# result = ""

# for letter in letters:
#     result = result + letter
#     print(result)

#over written my result variable by adding itself and the letter
#if print is indented, it will print it. If not and outside the for loop it will just print it once
#giving me the result after the for loop, printed abcd

#Nested Loop

# numbers = [
#     [1,2,3], 
#     [4], 
#     [5,6]
#     ]
#     print(numbers[2][-1])

    # for number in numbers: #number -> [1,2,3]
    #     for digit in number: #digit -> 1 , 2
    #         print(digit) #1. 2

    # #two idents 

    #While loops - if we don't know how many times to repeat the action

count = 0

while count < 5:
    print("Hello")
    count = count + 1

    #overriding count itself, by itself plus 1