students = ["Angela", "Jen", "Bel"]
print (students[0])

#creating a dictionary, separated with coma
#Elements are key: Value pairs
#Keys need to be unique, keys can be only immutable
#Immutable data types -> String, Integer, Float, Bool, Lists ect.
#Values don't need to be unique, any data type
#Dictionaries are unordered, so when you print can appear in a different order

#word and then the definition - use this as a way to understand your data set
#item is always connected to the key

students_dict = {"Angela" : 1, "Jen" : 2, "Bel" : 3}
print(students_dict)

print(students_dict.get("Bel"))
print(students_dict["Asli"]) #this will throw an error because Asli doesn't exists
print(students_dict.get("Asli" , 15)) #this will give you the value of 15

#Get functions 

# print (students_dict["Angela"])
students_dict["Asli"] = 4
# print(students_dict)

students_dict["Jen"] = 10
# print(students_dict)

del students_dict["Asli"]
# print(students_dict)

print(students_dict.keys())
print(students_dict.items())

#Iteration (loops)
for key in students_dict: 
    print(key, students_dict[key])

for key,value in students_dict.items():
    print(key, value)
