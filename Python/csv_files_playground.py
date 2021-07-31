#Import CSV

with open("2016_pilbara.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)

        import csv
population = []
# with open("2016_pilbara.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)
with open("2016_pilbara.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        population.append(line)
#print(population)
# for age_group in population:
#     print(f"{age_group[0]} {age_group[1]}")
# with open("population.csv", mode="w", newline="") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     for age_group in population:
#         csv_writer.writerow([age_group[0],age_group[1]])
# def create_greeting(name): #name = "Chilli", #name = "Angela"
#     greeting = f"Hello {name}"
#     return greeting
# print(create_greeting("Chilli"))
# print(create_greeting("Angela"))
#Create function that takes in an integer
#as a parameter and returns that integer
#multiplied by 3
def convert_cm_to_in(length_cm):
    length_in_inch = length_cm / 2.54
    return length_in_inch
# print(convert_cm_to_in(20))
# print(length_in_inch) #is not defined, local var
#Write a function that converts inches to
#centimeters
def calculate_mean(a, b):
    total = a + b
    mean = total / 2
    return mean
print(calculate_mean(3,4))