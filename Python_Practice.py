# print("Hellow World")

# # Data Structures: Lists
# counties = ["Arapahoe", "Denver", "Jefferson"]
# counties.append("El Paso")
# counties.insert(2, "El Paso")
# counties.remove("El Paso")
# counties[2] = "El Paso"
# counties.pop(3)
# print(counties)
# print(counties[1])
# print(len(counties))
# print(counties[0:2])
# print(counties[1:])
# print(counties[1:3])

# # Data Strucutres: Lists: Practice Question
# counties = ["Arapahoe", "Denver", "Jefferson"]
# counties.insert(1, "El Paso")
# counties.remove("Arapahoe")
# counties[2] = "Denver"
# counties[1] = "Jefferson"
# counties.append("Arapahoe")
# print(counties)

# # Data Structures: Dictionaries
# counties_dict = {}
# counties_dict["Arapahoe"] = 422829
# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438
# print(counties_dict)
# print(counties_dict)
# print(len(counties_dict))
# print(counties_dict.items())
# print(counties_dict.keys())
# print(counties_dict.values())

# # Data Structures: Dictionaries
# voting_data={
# 	"county": ["Arapahoe", "Denver", "Jefferson"],
# 	"registered_voters": [422829, 463353, 432438],
# }
# print(voting_data)

# # Data Structures: Dictionaries: Practice Question
# voting_data={
#     "county": ["Arapahoe", "Denver", "Jefferson"],
#     "registered_voters": [422829, 463353, 432438],
# }
# voting_data["county"].insert(2,"El Paso")
# voting_data["county"].remove("Arapahoe")
# voting_data["county"].remove("Denver")
# voting_data["county"].insert(3,"Denver")
# voting_data["county"].append("Arapahoe")
# print(voting_data)5

# # Decision Statements: If Statement
# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# # Decision Statements: If-Else Statement
# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

# # Decision Statements: Nested If-Else Statements
#     #What is the score?
# score = int(input("What is your test score? "))

#     # Determine the grade.
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

# # Decision Statements: elif Statements
#     # What is the score?
# score = int(input("What is your test score? "))

#     # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

# # Membership Operators
# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# #Logic Operators
# counties = ["Arapahoe","Denver","Jefferson"]

#     #and
# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

#     #or
# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties.")
# else:
#     print("Arapahoe and El Paso are not in the list of counties.")

# # While Loops
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

# # Iterate Through Lists and Tuples
# counties = ["Arapahoe","Denver","Jefferson"]
# for county in counties:
#     print(county)

# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

# # Iterate Through A Dictionary
# counties_dict = {}
# counties_dict["Arapahoe"] = 422829
# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438

# for county in counties_dict:
#     print(county)

#     # Get Keys in Dictionary
# for county in counties_dict.keys():
#     print(county)

#     # Get Values in Dictionary
# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

    # Get Key-Value Pairs in Dictionary
# for county, voters in counties_dict.items():
#     print(county, voters)

# # Iterate Through A List of Dictionaries
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

#     # Print Using range()
# for i in range(len(voting_data)): 
#     print(voting_data[i])

# # Get Values from a List of Dictionaries
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
        
# # Get Only Voter Values
# for county_dict in voting_data:
#      print(county_dict['registered_voters'])

# # Get Only County Values
# for county_dict in voting_data:
#     print(county_dict['county'])

# # Print()
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# # F-Strings Print
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# per_votes = my_votes / total_votes * 100
# print(per_votes)
# print(f"I received {per_votes}% of the total votes.")

# Using F-Strings With Dictionary
    # Print
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

    # F-String
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# # Multiline F-Strings
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")
# print(message_to_candidate)

# # Format Floating-Point Decimals
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)