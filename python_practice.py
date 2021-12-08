print("hello world")
type(3)
class tuple: 
    ballots = 1,341
type(73.81)
type(True)

# Practice calculations
print(5 + 2 *3)
print(8// 5 - 3)
print(8 + 22*2 - 4)
print(16 - 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 *  3 / 2 - 4)
print((5 + 2) * 3)
print((8 // 5) - 3)
print(8 + (22 * (2 - 4)))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
print(5 + (9 * 3 / 2 - 4))
print(5 + (9 * 3 / (2 - 4)))

# Practice lists
counties = ["Araphoe", "Denver", "Jefferson"]
print(counties)

print(counties[0])

print(len(counties))

print(counties[1:])

counties.append("El Paso")
print(counties)

counties.insert(2, "El Paso")
print(counties)

counties.remove("El Paso")
print(counties)

counties.pop(3)
print(counties)

counties.insert(1, "El Paso")
counties.remove("Araphoe")
counties.append("Araphoe")
print(counties)

# Practice tuple
counties_tuple = ("Arapahoe", "Denver", "Jefferson")

print(len(counties_tuple))

print(counties_tuple[1])

# Practice dictionaries
counties_dict = {}
counties_dict["Araphoe"] = 422829
print(counties_dict)

counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)

print(len(counties_dict))

# Get all keys and values
print(counties_dict.items())

# Get keys
print(counties_dict.keys())

# Get values
print(counties_dict.values())

#Get a specific value
print(counties_dict.get("Denver"))

#List of dictionaries
voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)

#Pracitce if statements
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#Practice if/else statements
#temperature = int(input("What is thet emperature outside?"))

#if temperature > 80:
        #print("Turn on the AC.")
#else:
        #print("Open the windows")

#Pracitce nested if-else statements

#What is the score?
#score = int(input("What is your test score?"))

# Determine the grade
#if score >= 90:
    #print('Your grade is an A.')
#elif score >= 80:
    #print('Your grade is a B.')
#elif score >= 70:
    #print('Your grade is a C.')
#elif score >= 60:
    #print('Your grade is a D.')
#else:
    #print('Your grade is an F.')

# In example
counties = ["Arapahoe", "denver", "Jefferson"]

if "Arapahoe" in counties:
    print("True")
else:
    ("False")

counties = ["Arapahoe","Denver","Jefferson"]

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# Not in example
counties = ["Arapahoe", "Denver", "Jefferson"]

if "El Pase" not in counties:
    print("True")
else:
    print("False")

#And example
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso is not in the list of counties")

# Or example
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#Loop Pracitce

#While practice
x = 0
while x <= 5:
    print(x)
    x = x + 1

count = 7
while count < 1:
    print("Hello World")

# For loop practice
counties = ["Arapahoe", "Denver", "Jefferson"]

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

#Get the keys of a dictionary

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

#Get the values of a dictionary
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))

#Get the key-value pairs of a dictionary
for county, voters in counties_dict.items():
    print(county, voters)

# Get each dictionary in a list of dictionaries

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[1]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])

#Using F-strings practice

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# If Statement practice
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#If/Then Statement Practice
# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

#NEsted-If Statement Practice

#What is the score?
# score = int(input("What is your test score? "))

# Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')

#Membership Operators Practice
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#Logical oprators practice
if "Araphoe" in counties and "El PAso" in counties:
    print("Araphoe and El Paso are in the lis t of counties.")
else:
    print("Araphoe or El Paso is not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")

#Iterate through lists and tuples
for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

#Iterate through dictionaries
for county in counties_dict:
    print(county)

#Get value of a dictionary
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

#Get the Key-value pairs of a dictionary
for key, voters in counties_dict.items():
    print(key,value)

#Get each dictionary in a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#Get the values from a list of dicitonaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

#Using f-strings with dictionaries
counties_dict ={"Araphoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters. ")

candidate_votes = int(input("How many votes did the candidate get in the election? ")) 
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "     f"The total number of votes in the election was {total_votes}. "
     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

