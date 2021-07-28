groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

# print(groceries)

#look at a specific value
# print(groceries["Baby Spinach"])

#Add an item
groceries["Avacado"] = 1.00
# print(groceries)

#Remove an item
del groceries["Bacon"]
# print(groceries)

# #Iterating over the dictionary
# for item in groceries: 
#     print(f"{item}: ${groceries[key]}")

#another way to iterate over the dictionary
# for item,price in groceries.items():
#     print(f"{item}: ${price}")

#Question 1
# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Bacon": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08
# }

# quantity = {
#     "Baby Spinach": 1,
#     "Hot Chocolate": 3,
#     "Crackers": 2,
#     "Bacon": 1,
#     "Carrots": 4,
#     "Oranges": 2
# }

# for key,value in groceries.items():
#     print(f"{quantity[key]} {key} @ ${value}= ${round(quantity[key]* value,2)}") 

#Question 2

colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0
}

colours = [
    "purple",
    "red",
    "yellow",
    "blue",
    "purple",
    "orange",
    "blue",
    "purple",
    "orange",
    "green"
]

#iterate over the list of colours
# for colour in colours:
    # print(colour)
    # find the coklour in the dictionary and increment its value by 1
#     # first iteration -> colour_counts["blue"] returns 0
#    colour_counts[colour] += 1

#    for colour in colour_counts:
#        print(f"{colour}: {colour_counts[colour]}")
