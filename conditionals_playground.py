# is_raining = False
# is_cold = True

# print(type(is_raining))
# print(is_cold)
# print(type(is_cold))
# print(is_raining)
# print(not is_raining)
# print(is_raining and is_cold)
# print(is_raining and not is_cold)

# print(is_raining) #F
# print(not is_raining) #T
# print(is_raining or is_cold) #T
# print(is_raining and not is_cold) #F
# print(is_raining or not is_cold) #F
# print(not is_raining and not is_cold) #F

# temperature = 16
# # print(temperature < 18)
# wind_chill = 3
# print(wind_chill > 4)
# print(temperature - wind_chill < 16)

# name = "Hayley"
# print(name == "Hayley")
# print(name != "Hayley")


# print("A" > "a")
# how the characters are stored in your computer are 'asky'
# characters, and each letter has a numerical value
# if its a capital letter it has a lower value than a lower case

#####################################
# if statements
# is_raining = False

#if
# if is_raining:
#     print("Take an umbrella.")

# #if and else
# if is_raining:
#     print("Take an umbrella.")
# else:
#     print("Do not take an umbrella.")

# #if, elif, else
# temperature = 16
# wind_chill = 3

# if temperature - wind_chill < 16:
#     print("Take a jumper.")
# elif temperature - wind_chill > 30:
#     print("Euck, its hot today")
# else:
#     print("Wow, what a lovely day")

# #nested if statements
# is_raining = False

# if temperature - wind_chill < 16 and is_raining:
#     print("Just stay home.")
# else: 
#     if is_raining:
#         print("You'll need an umbrella today.")
#     if temperature - wind_chill < 16:
#         print("You'll need a jumper today")

# this printed, youll need a jumper today
# because is rainining is fales, its ignoring first print
# in else, its going to look at temperature, because is raining is false

#Conditionals Exercises

#Q1
# moths_in_house = False

# if moths_in_house:
#     print("Get the moths!")
# else:
#     print("No threats detected")

#Q2
# moths_in_house = True
# mitch_is_home = True

# if moths_in_house and mitch_is_home:
#     print("Hooman! Help me get the moths.")
# elif not moths_in_house and not mitch_is_home:
#     print("No threats detected")
# elif moths_in_house and not mitch_is_home:
#     print("Meeeooooowww! Hiss!")
# else:
#     print("Climb on Mitch!")

#Q3
light_colour = "Red"
car_detected = False

if car_detected and light_colour == "Red":
    print("Flash!")


